"""
Pure, idempotent validation of semantic envelopes.
ADR-004: Validation functions are pure with no side effects
"""
from typing import Dict, Any
import time

def validate_envelope_structure(envelope: Dict) -> bool:
    """
    Validate that an envelope has all required fields.
    Pure function - no side effects, idempotent.
    
    Args:
        envelope: The envelope to validate
    
    Returns:
        True if valid, False otherwise
    """
    # ADR-003: Required fields
    required_fields = [
        "id", "timestamp", "payload",
        "schema_version", "orchestration_policy", "signature"
    ]
    
    for field in required_fields:
        if field not in envelope:
            return False
    
    return True


def validate_envelope_semantics(envelope: Dict) -> bool:
    """
    Validate semantic correctness of envelope contents.
    Pure function - no side effects, idempotent.
    
    Args:
        envelope: The envelope to validate
    
    Returns:
        True if semantically valid, False otherwise
    """
    # Check structure first
    if not validate_envelope_structure(envelope):
        return False
    
    # ADR-002: Validate signature format
    sig = envelope["signature"]
    if not isinstance(sig, str):
        return False
    
    if not sig.startswith("tier2-semantic-"):
        return False
    
    parts = sig.split("-")
    if len(parts) < 4:  # Should have at least: tier2, semantic, policy, timestamp, random
        return False
    
    # Validate timestamp is reasonable (not in future, not too old)
    now = time.time()
    ts = envelope["timestamp"]
    if not isinstance(ts, (int, float)):
        return False
    
    # Timestamp should be within reasonable bounds (e.g., last 30 days)
    if ts > now + 3600 or ts < now - 30 * 24 * 3600:
        return False
    
    # Validate schema version
    if envelope["schema_version"] != "tier2-envelope-v1":
        return False
    
    return True


def validate_policy_compliance(envelope: Dict, required_policy: str) -> bool:
    """
    Validate that envelope complies with a specific policy.
    Pure function - no side effects.
    
    Args:
        envelope: The envelope to validate
        required_policy: The policy that must be present
    
    Returns:
        True if envelope uses the required policy
    """
    if not validate_envelope_structure(envelope):
        return False
    
    return envelope.get("orchestration_policy") == required_policy
