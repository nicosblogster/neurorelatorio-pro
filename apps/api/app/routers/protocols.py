from fastapi import APIRouter, HTTPException

from app.domain.rules import validate_protocol_use
from app.repositories.in_memory import get_protocol, load_protocols
from app.schemas import (
    Protocol,
    ProtocolUseValidationRequest,
    ProtocolUseValidationResponse,
)

router = APIRouter(prefix="/protocols", tags=["protocols"])


@router.get("", response_model=list[Protocol])
def list_protocols() -> list[Protocol]:
    return load_protocols()


@router.post("/{protocol_id}/validate-use", response_model=ProtocolUseValidationResponse)
def validate_use(
    protocol_id: str,
    request: ProtocolUseValidationRequest,
) -> ProtocolUseValidationResponse:
    protocol = get_protocol(protocol_id)
    if protocol is None:
        raise HTTPException(status_code=404, detail="Protocol not found")

    issues = validate_protocol_use(protocol, request.professional)
    return ProtocolUseValidationResponse(
        allowed=not any(issue.severity == "blocker" for issue in issues),
        issues=issues,
    )
