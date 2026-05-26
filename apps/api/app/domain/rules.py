from app.domain.enums import ProtocolAccessLevel, ReportStatus, UserRole
from app.schemas import (
    FillableTabEntry,
    FillableTabTemplate,
    ProfessionalAuthorization,
    Protocol,
    ReportFinalizationRequest,
    ValidationIssue,
)


def validate_protocol_use(
    protocol: Protocol,
    professional: ProfessionalAuthorization,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    if not protocol.active:
        issues.append(
            ValidationIssue(
                code="protocol_inactive",
                severity="blocker",
                message="O protocolo esta inativo e nao pode ser usado neste caso.",
            )
        )

    if protocol.access_level == ProtocolAccessLevel.PRIVATE:
        if not professional.has_restricted_instrument_authorization:
            issues.append(
                ValidationIssue(
                    code="private_instrument_without_authorization",
                    severity="blocker",
                    message="Instrumento marcado como privativo/restrito exige profissional autorizado.",
                )
            )

    if protocol.access_level == ProtocolAccessLevel.VERIFY_SATEPSI:
        issues.append(
            ValidationIssue(
                code="satepsi_verification_required",
                severity="warning",
                message="Verifique manual, licenca, faixa etaria, padronizacao, autorizacao de uso e SATEPSI antes da aplicacao.",
            )
        )

    if professional.role in {UserRole.ASSISTANT, UserRole.EXTERNAL_READER}:
        issues.append(
            ValidationIssue(
                code="role_cannot_apply_protocol",
                severity="blocker",
                message="Este perfil nao pode registrar aplicacao de instrumentos ou protocolos.",
            )
        )

    return issues


def validate_report_finalization(
    request: ReportFinalizationRequest,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    if not request.responsible_professional_id:
        issues.append(
            ValidationIssue(
                code="missing_responsible_professional",
                severity="blocker",
                message="Nenhum relatorio pode ser finalizado sem profissional responsavel identificado.",
            )
        )

    if request.assessee_is_minor and not request.has_legal_guardian:
        issues.append(
            ValidationIssue(
                code="minor_without_legal_guardian",
                severity="blocker",
                message="Relatorio de menor de idade exige responsavel legal cadastrado.",
            )
        )

    if request.assessee_is_minor and not request.has_valid_consent:
        issues.append(
            ValidationIssue(
                code="minor_without_valid_consent",
                severity="blocker",
                message="Relatorio de menor de idade exige consentimento/base legal valida registrada.",
            )
        )

    if not request.evidences:
        issues.append(
            ValidationIssue(
                code="conclusion_without_evidence",
                severity="blocker",
                message="Toda conclusao deve se basear em evidencias registradas.",
            )
        )

    if not request.limitations:
        issues.append(
            ValidationIssue(
                code="missing_limitations",
                severity="blocker",
                message="Relatorios finais devem explicitar limitacoes da avaliacao.",
            )
        )

    if request.ai_generated_blocks_pending_review:
        issues.append(
            ValidationIssue(
                code="ai_blocks_pending_review",
                severity="blocker",
                message="Blocos gerados por IA precisam de revisao e aprovacao humana antes da finalizacao.",
            )
        )

    if request.status == ReportStatus.FINAL:
        issues.append(
            ValidationIssue(
                code="already_final",
                severity="warning",
                message="Relatorio ja esta marcado como final; alteracoes devem gerar nova versao ou termo aditivo.",
            )
        )

    return issues


def validate_fillable_tab_entries(
    entries: list[FillableTabEntry],
    templates: list[FillableTabTemplate],
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    template_by_key = {template.tab_key: template for template in templates}
    seen_tab_keys: set[str] = set()

    if not entries:
        issues.append(
            ValidationIssue(
                code="empty_fillable_tabs",
                severity="warning",
                message="Nenhuma aba preenchivel foi enviada para validacao.",
            )
        )
        return issues

    for entry in entries:
        template = template_by_key.get(entry.tab_key)
        if template is None:
            issues.append(
                ValidationIssue(
                    code="unknown_fillable_tab",
                    severity="blocker",
                    message=f"A aba '{entry.tab_key}' nao existe no modelo de abas preenchiveis.",
                )
            )
            continue

        if entry.tab_key in seen_tab_keys:
            issues.append(
                ValidationIssue(
                    code="duplicated_fillable_tab",
                    severity="warning",
                    message=f"A aba '{template.tab_label}' foi enviada mais de uma vez.",
                )
            )
        seen_tab_keys.add(entry.tab_key)

        allowed_options = set(template.predefined_options)
        for selected_option in entry.selected_options:
            if selected_option.label not in allowed_options:
                issues.append(
                    ValidationIssue(
                        code="unknown_predefined_option",
                        severity="blocker",
                        message=f"A opcao '{selected_option.label}' nao pertence a aba '{template.tab_label}'.",
                    )
                )
                continue

            if not selected_option.source:
                issues.append(
                    ValidationIssue(
                        code="selected_option_without_source",
                        severity="warning",
                        message=f"A opcao '{selected_option.label}' da aba '{template.tab_label}' esta sem fonte registrada.",
                    )
                )

            if not selected_option.value:
                issues.append(
                    ValidationIssue(
                        code="selected_option_without_value",
                        severity="warning",
                        message=f"A opcao '{selected_option.label}' da aba '{template.tab_label}' foi selecionada sem valor preenchido.",
                    )
                )

        if entry.campo44 and not template.allow_campo44:
            issues.append(
                ValidationIssue(
                    code="campo44_not_allowed",
                    severity="blocker",
                    message=f"A aba '{template.tab_label}' nao permite inclusao de campo44.",
                )
            )
            continue

        seen_campo44_labels: set[str] = set()
        for index, campo44 in enumerate(entry.campo44, start=1):
            campo_name = campo44.label or f"campo44 #{index}"
            if campo44.label in seen_campo44_labels:
                issues.append(
                    ValidationIssue(
                        code="duplicated_campo44_label",
                        severity="warning",
                        message=f"O campo44 '{campo_name}' aparece mais de uma vez na aba '{template.tab_label}'.",
                    )
                )
            if campo44.label:
                seen_campo44_labels.add(campo44.label)

            missing_fields = [
                label
                for label, value in {
                    "rotulo": campo44.label,
                    "tipo": campo44.type,
                    "valor": campo44.value,
                    "fonte": campo44.source,
                    "justificativa": campo44.reason,
                }.items()
                if not value
            ]
            if missing_fields:
                issues.append(
                    ValidationIssue(
                        code="campo44_missing_required_fields",
                        severity="blocker",
                        message=(
                            f"O campo44 '{campo_name}' da aba '{template.tab_label}' esta sem "
                            f"{', '.join(missing_fields)}."
                        ),
                    )
                )

    return issues
