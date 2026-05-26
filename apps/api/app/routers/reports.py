from fastapi import APIRouter

from app.domain.rules import validate_fillable_tab_entries, validate_report_finalization
from app.repositories.in_memory import load_fillable_tabs
from app.schemas import (
    FillableTabTemplate,
    FillableTabsValidationRequest,
    FillableTabsValidationResponse,
    ReportFinalizationRequest,
    ReportFinalizationResponse,
    ReportSection,
)

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("/validate-finalization", response_model=ReportFinalizationResponse)
def validate_finalization(
    request: ReportFinalizationRequest,
) -> ReportFinalizationResponse:
    issues = validate_report_finalization(request)
    return ReportFinalizationResponse(
        can_finalize=not any(issue.severity == "blocker" for issue in issues),
        issues=issues,
    )


@router.get("/templates/full", response_model=list[ReportSection])
def full_report_template() -> list[ReportSection]:
    return [
        ReportSection(
            key="identification",
            title="Identificacao",
            required=True,
            guidance="Dados do avaliado, responsaveis, escola e contexto.",
        ),
        ReportSection(
            key="procedures",
            title="Procedimentos e instrumentos",
            required=True,
            guidance="Listar entrevistas, observacoes, protocolos e documentos, sem reproduzir materiais protegidos.",
        ),
        ReportSection(
            key="findings",
            title="Achados observados",
            required=True,
            guidance="Separar observacao direta, relato familiar, relato escolar, documento e resultado de instrumento.",
        ),
        ReportSection(
            key="interpretation",
            title="Interpretacao neuropsicopedagogica",
            required=True,
            guidance="Usar linguagem cautelosa e vinculada a evidencias.",
        ),
        ReportSection(
            key="hypotheses",
            title="Hipoteses neuropsicopedagogicas",
            required=False,
            guidance="Nao emitir diagnostico fechado ou CID; sugerir encaminhamento quando extrapolar a area.",
        ),
        ReportSection(
            key="recommendations",
            title="Recomendacoes",
            required=True,
            guidance="Separar recomendacoes para familia, escola, professor, intervencao e equipe multiprofissional.",
        ),
        ReportSection(
            key="limitations",
            title="Limitacoes da avaliacao",
            required=True,
            guidance="Registrar limites de dados, instrumentos, tempo, contexto e inferencia.",
        ),
        ReportSection(
            key="reviewed_conclusion",
            title="Conclusao tecnica revisada pelo profissional",
            required=True,
            guidance="Conclusao final assinada pelo responsavel tecnico.",
        ),
    ]


@router.get("/fillable-tabs", response_model=list[FillableTabTemplate])
def fillable_tabs() -> list[FillableTabTemplate]:
    return load_fillable_tabs()


@router.post("/fillable-tabs/validate", response_model=FillableTabsValidationResponse)
def validate_fillable_tabs(
    request: FillableTabsValidationRequest,
) -> FillableTabsValidationResponse:
    issues = validate_fillable_tab_entries(request.entries, load_fillable_tabs())
    return FillableTabsValidationResponse(
        valid=not any(issue.severity == "blocker" for issue in issues),
        issues=issues,
    )
