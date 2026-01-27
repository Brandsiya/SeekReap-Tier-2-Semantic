#!/usr/bin/env python3
"""
Tier-2 Semantic Orchestrator
Transforms atomic behaviors into semantic envelopes for Tier-3
"""
import json
import base64
import hashlib
from datetime import datetime
from typing import Dict, Any

from ..constants import (
    TIER3_ENVELOPE_VERSION,
    BEHAVIOR_TYPES,
    INTENSITY_MIN,
    INTENSITY_MAX,
    ENVELOPE_ID_PREFIX,
    SIGNATURE_PREFIX,
    DEFAULT_BEHAVIOR_TYPE,
    DEFAULT_INTENSITY,
    DEFAULT_DURATION,
)


class SemanticOrchestrator:
    """Creates semantic envelopes from atomic behaviors"""

    def __init__(self):
        self.envelopes_created = 0
        self.transformations_performed = 0

    def transform_to_semantic(self, atomic_behavior: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform atomic behavior data to semantic format

        Args:
            atomic_behavior: Raw atomic behavior from Tier-1

        Returns:
            Semantic data ready for envelope creation
        """
        self.transformations_performed += 1

        # Extract basic fields
        behavior_type = atomic_behavior.get("type", DEFAULT_BEHAVIOR_TYPE)
        intensity = atomic_behavior.get("intensity", DEFAULT_INTENSITY)
        duration = atomic_behavior.get("duration", DEFAULT_DURATION)
        features = atomic_behavior.get("features", [])

        # Create semantic data structure
        semantic_data = {
            "behavior_type": self._map_behavior_type(behavior_type),
            "intensity": self._normalize_intensity(intensity),
            "duration": int(duration),
            "features_used": list(features),
            "_version": TIER3_ENVELOPE_VERSION,
            "_semantic": True,
            "_timestamp": datetime.utcnow().isoformat() + "Z"
        }

        # Add optional fields if present
        optional_fields = ["metadata", "premium_indicator", "user_segment", "session_id"]
        for field in optional_fields:
            if field in atomic_behavior:
                semantic_data[field] = atomic_behavior[field]

        return semantic_data

    def create_envelope(self, semantic_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create opaque envelope from semantic data

        Args:
            semantic_data: Semantic data from transform_to_semantic()

        Returns:
            Opaque envelope for Tier-3 consumption
        """
        # Validate and prepare semantic data
        validated_data = self._validate_semantic_data(semantic_data)

        # Create envelope
        envelope = {
            "envelope_id": self._generate_envelope_id(),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "payload": self._encode_payload(validated_data),
            "signature": self._generate_signature(validated_data)
        }

        self.envelopes_created += 1
        return envelope

    def _map_behavior_type(self, atomic_type: str) -> str:
        """Map atomic behavior type to semantic type"""
        return BEHAVIOR_TYPES.get(atomic_type, atomic_type)

    def _normalize_intensity(self, intensity: float) -> float:
        """Ensure intensity is within valid bounds"""
        return max(INTENSITY_MIN, min(intensity, INTENSITY_MAX))

    def _validate_semantic_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Ensure semantic data has all required fields"""
        validated = data.copy()

        # Ensure required fields exist
        required = ["behavior_type", "intensity", "duration", "features_used"]
        for field in required:
            if field not in validated:
                if field == "behavior_type":
                    validated[field] = DEFAULT_BEHAVIOR_TYPE
                elif field == "intensity":
                    validated[field] = DEFAULT_INTENSITY
                elif field == "duration":
                    validated[field] = DEFAULT_DURATION
                elif field == "features_used":
                    validated[field] = []

        # Ensure version and semantic marker
        if "_version" not in validated:
            validated["_version"] = TIER3_ENVELOPE_VERSION
        if "_semantic" not in validated:
            validated["_semantic"] = True

        return validated

    def _generate_envelope_id(self) -> str:
        """Generate unique envelope ID"""
        timestamp = datetime.utcnow().timestamp()
        microsecond = datetime.utcnow().microsecond
        return f"{ENVELOPE_ID_PREFIX}{timestamp}_{microsecond}"

    def _encode_payload(self, data: Dict[str, Any]) -> str:
        """Encode semantic data as opaque payload"""
        # Sort keys for deterministic encoding
        sorted_data = dict(sorted(data.items()))
        json_str = json.dumps(sorted_data, separators=(',', ':'))
        encoded = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
        return encoded

    def _generate_signature(self, data: Dict[str, Any]) -> str:
        """Generate signature for data integrity"""
        data_str = json.dumps(data, separators=(',', ':'))
        hash_obj = hashlib.sha256(data_str.encode())
        return f"{SIGNATURE_PREFIX}{hash_obj.hexdigest()[:8]}"

    def get_stats(self) -> Dict[str, int]:
        """Get orchestrator statistics"""
        return {
            "envelopes_created": self.envelopes_created,
            "transformations_performed": self.transformations_performed
        }
