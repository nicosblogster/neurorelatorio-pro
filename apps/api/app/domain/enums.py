from enum import StrEnum


class UserRole(StrEnum):
    ADMIN = "admin"
    CLINICAL_NPP = "clinical_npp"
    INSTITUTIONAL_NPP = "institutional_npp"
    ASSISTANT = "assistant"
    SUPERVISOR = "supervisor"
    EXTERNAL_READER = "external_reader"


class ProfessionalContext(StrEnum):
    CLINICAL = "clinical"
    INSTITUTIONAL = "institutional"
    BOTH = "both"


class ProtocolAccessLevel(StrEnum):
    OPEN = "open"
    NON_PRIVATE = "non_private"
    PRIVATE = "private"
    VERIFY_SATEPSI = "verify_satepsi"


class EvidenceSource(StrEnum):
    DIRECT_OBSERVATION = "direct_observation"
    FAMILY_REPORT = "family_report"
    SCHOOL_REPORT = "school_report"
    INSTRUMENT_RESULT = "instrument_result"
    DOCUMENT = "document"


class ReportStatus(StrEnum):
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    FINAL = "final"
