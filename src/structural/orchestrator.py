#!/usr/bin/env python3
"""
TIER-2: Structural Transformation Library

ARCHITECTURAL CONTRACT:
- Input: Tier-1 atomic behavior (any dict)
- Output: Opaque envelope with structural guarantees ONLY
- Guarantee: Valid base64 payload that decodes to JSON (opaque serialization)
- Guarantee: Meta with id and timestamp
- NO Guarantee: Semantic meaning, validation, or interpretation

Tier-2 responsibility ends at structure.
Tier-3 responsibility begins at semantics.
"""
import json
import base64
from datetime import datetime
from typing import Dict, Any

# Internal constants (Tier-2 concern only, not exposed)
_STRUCTURAL_ENVELOPE_VERSION = "1.0"


class StructuralOrchestrator:
    """
    Pure library for structural transformation ONLY.
    
    Design Principles:
    1. No semantic guarantees to consumers
    2. No validation of business logic
    3. No interpretation of content
    4. Only structural transformation
    
    Architectural Position:
    - Between Tier-1 (atomic) and Tier-3 (consumption)
    - Output is structurally sound but semantically opaque
    - All meaning assigned by Tier-3
    """

    def __init__(self):
        """
        Initialize orchestrator.
        
        Note: No system dependencies, no I/O, no state.
        Pure library instantiation only.
        """
        # Library statistics (volatile, for monitoring only)
        self.transformations_performed = 0

    def create_envelope(self, tier1_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create opaque envelope from Tier-1 input.
        
        This is the ONLY output Tier-3 sees.
        Only structural guarantees are provided.
        
        Args:
            tier1_input: Any dictionary from Tier-1
            
        Returns:
            Opaque envelope with structural guarantees:
            {
                "payload": "base64_string",  # Opaque to Tier-3
                "meta": {                    # Structural only
                    "id": "unique_string",
                    "timestamp": "ISO8601_with_Z"
                }
            }
        """
        self.transformations_performed += 1

        # Create internal representation (Tier-2 concern only)
        internal_data = self._create_internal_representation(tier1_input)
        
        # Create envelope with structural guarantees ONLY
        envelope = {
            "payload": self._encode_payload(internal_data),
            "meta": self._create_meta()
        }

        return envelope

    # -----------------------------------------------------------------
    # Internal helper methods (Tier-2 concern only)
    # -----------------------------------------------------------------

    def _create_internal_representation(self, tier1_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create Tier-2's internal representation.
        
        This is PRIVATE to Tier-2. Tier-3 never sees this structure.
        Tier-2 can change this at any time without breaking Tier-3.
        """
        # Extract with defaults (Tier-2 internal logic)
        behavior_type = tier1_input.get("type", "generic")
        intensity = tier1_input.get("intensity", 0.5)
        duration = tier1_input.get("duration", 60)
        features = tier1_input.get("features", [])

        # Internal structure (Tier-2 concern only)
        # Field names are opaque and can change
        internal_data = {
            "a": behavior_type[:3] if behavior_type else "gen",  # Abbreviated
            "b": max(0.0, min(1.0, float(intensity))),          # Normalized
            "c": int(duration),                                 # Cast to int
            "d": list(features),                                # As list
            "_v": _STRUCTURAL_ENVELOPE_VERSION,                 # Internal version
            "_t": datetime.utcnow().isoformat() + "Z"           # Internal timestamp
        }

        # Add optional fields if present (opaque to Tier-3)
        optional_fields = ["metadata", "premium_indicator", "user_segment", "session_id"]
        field_mapping = {"metadata": "e", "premium_indicator": "f", 
                       "user_segment": "g", "session_id": "h"}
        
        for field in optional_fields:
            if field in tier1_input:
                internal_name = field_mapping.get(field, field)
                internal_data[internal_name] = tier1_input[field]

        return internal_data

    def _create_meta(self) -> Dict[str, Any]:
        """Create meta with required structural fields."""
        return {
            "id": self._generate_envelope_id(),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    def _generate_envelope_id(self) -> str:
        """Generate unique envelope ID (structural guarantee only)."""
        timestamp = datetime.utcnow().timestamp()
        microsecond = datetime.utcnow().microsecond
        return f"env_{timestamp}_{microsecond}"

    def _encode_payload(self, data: Dict[str, Any]) -> str:
        """
        Encode internal data as opaque payload.
        
        Structural guarantee: returns valid base64 that decodes to JSON.
        JSON is used as an opaque serialization format only.
        No semantic guarantees about the JSON content.
        """
        # Sort keys for deterministic encoding (internal concern)
        sorted_data = dict(sorted(data.items()))
        json_str = json.dumps(sorted_data, separators=(',', ':'))
        encoded = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
        return encoded

    def get_stats(self) -> Dict[str, int]:
        """Get library statistics (volatile, resets on instance destruction)."""
        return {
            "transformations_performed": self.transformations_performed
        }

    def reset_stats(self) -> None:
        """Reset library statistics (for testing/demo purposes)."""
        self.transformations_performed = 0


# ============================================================================
# Structural verification utility (the ONLY contract verification)
# ============================================================================

def verify_envelope_structure(envelope: Dict[str, Any]) -> bool:
    """
    Verify Tier-2 structural guarantees ONLY.
    
    This is the ONLY contract verification Tier-2 provides.
    Tier-3 is responsible for all other validation.
    
    Args:
        envelope: Potential Tier-2 output
        
    Returns:
        True if envelope meets structural guarantees:
        - Has "payload" and "meta" keys
        - Payload is valid base64
        - Decoded payload is valid JSON (opaque serialization)
        - Meta has "id" and "timestamp"
    """
    try:
        # 1. Must be dict with required keys
        if not isinstance(envelope, dict):
            return False
        
        required_keys = {"payload", "meta"}
        if not required_keys.issubset(envelope.keys()):
            return False
        
        # 2. Payload must be string and valid base64
        payload = envelope["payload"]
        if not isinstance(payload, str):
            return False
        
        decoded_bytes = base64.b64decode(payload, validate=True)
        
        # 3. Decoded must be valid UTF-8 JSON (opaque serialization)
        decoded_str = decoded_bytes.decode('utf-8')
        json.loads(decoded_str)  # Verify JSON structure only
        
        # 4. Meta must be dict with required fields
        meta = envelope["meta"]
        if not isinstance(meta, dict):
            return False
        
        meta_required = {"id", "timestamp"}
        if not meta_required.issubset(meta.keys()):
            return False
        
        # 5. timestamp should be ISO-8601 (best effort, not guaranteed)
        # This is a quality check, not a structural guarantee
        
        return True
        
    except Exception:
        # Any failure means structure is invalid
        return False


# ============================================================================
# NON-NORMATIVE EXAMPLE USAGE (Illustrative only, not part of contract)
# ============================================================================

def _example_usage():
    """
    ⚠️ NON-NORMATIVE EXAMPLE ⚠️
    
    This illustrates usage but does NOT imply any guarantees.
    Tier-3 implementations may vary.
    """
    # Create orchestrator
    orchestrator = StructuralOrchestrator()
    
    # Tier-1 input (any structure)
    tier1_input = {
        "type": "user_action",
        "intensity": 0.75,
        "duration": 120
    }
    
    # Create envelope (structural only)
    envelope = orchestrator.create_envelope(tier1_input)
    
    # Verify structure (Tier-2 responsibility ends here)
    is_valid = verify_envelope_structure(envelope)
    
    # Tier-3 would continue from here with their own semantics
    return envelope, is_valid
