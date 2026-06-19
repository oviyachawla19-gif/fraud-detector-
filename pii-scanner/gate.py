from enum import Enum
from scanner import ScanResult

BLOCKED_TYPES = {"CREDIT_CARD", "US_SSN", "BANK_ACCOUNT"}
REDACT_TYPES = {"PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER", "LOCATION"}

class GateDecision(Enum):
    ALLOW = "allow"
    REDACT = "redact"
    BLOCK = "block"

def evaluate(result: ScanResult):
    if not result.has_pii:
        return GateDecision.ALLOW, ""

    types = {e.entity_type for e in result.entities}

    if types & BLOCKED_TYPES:
        return GateDecision.BLOCK, ""

    if types & REDACT_TYPES:
        return GateDecision.REDACT, result.redacted_text or ""

    return GateDecision.ALLOW, ""
