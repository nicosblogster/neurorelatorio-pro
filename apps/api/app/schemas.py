from pydantic import BaseModel, Field

from app.domain.enums import (
    EvidenceSource,
    ProfessionalContext,
    ProtocolAccessLevel,
    ReportStatus,
    UserRole,
)


class ValidationIssue(BaseModel):
    code: str
    severity: str = Field(pattern="^(info|warning|blocker)$")
    message: str


class ProfessionalAuthorization(BaseModel):
    role: UserRole
    context: ProfessionalContext
    has_restricted_instrument_authorization: bool = False
    authorized_protocol_ids: list[str] = Field(default_factory=list)


class Protocol(BaseModel):
    id: str
    name: str
    assessed_area: str
    objective: str
    age_or_grade: str
    type: str
    context: str
    authorized_professional: str
    usage_restriction: str
    access_level: ProtocolAccessLevel
    reference: str | None = None
    technical_notes: str
    manual_attachment_policy: str
    result_entry_policy: str
    requires_validity_check: bool = True
    active: bool = True


class ProtocolUseValidationRequest(BaseModel):
    professional: ProfessionalAuthorization


class ProtocolUseValidationResponse(BaseModel):
    allowed: bool
    issues: list[ValidationIssue]


class EvidenceSummary(BaseModel):
    source: EvidenceSource
    description: str


class ReportFinalizationRequest(BaseModel):
    assessee_is_minor: bool
    has_legal_guardian: bool
    has_valid_consent: bool
    responsible_professional_id: str | None = None
    status: ReportStatus = ReportStatus.DRAFT
    conclusion: str | None = None
    limitations: str | None = None
    evidences: list[EvidenceSummary] = Field(default_factory=list)
    ai_generated_blocks_pending_review: bool = False


class ReportFinalizationResponse(BaseModel):
    can_finalize: bool
    issues: list[ValidationIssue]


class ReportSection(BaseModel):
    key: str
    title: str
    required: bool
    guidance: str


class FillableTabTemplate(BaseModel):
    scope: str
    tab_key: str
    tab_label: str
    predefined_options: list[str]
    allow_campo44: bool = True
    required_source_for_campo44: bool = True


class FillableOptionEntry(BaseModel):
    label: str
    value: str | None = None
    source: str | None = None


class Campo44Entry(BaseModel):
    label: str | None = None
    type: str | None = None
    value: str | None = None
    source: str | None = None
    reason: str | None = None
    evidence_id: str | None = None


class FillableTabEntry(BaseModel):
    tab_key: str
    selected_options: list[FillableOptionEntry] = Field(default_factory=list)
    campo44: list[Campo44Entry] = Field(default_factory=list)


class FillableTabsValidationRequest(BaseModel):
    entries: list[FillableTabEntry] = Field(default_factory=list)


class FillableTabsValidationResponse(BaseModel):
    valid: bool
    issues: list[ValidationIssue]
