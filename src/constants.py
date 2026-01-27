"""
Semantic constants for Tier-2 - Envelope creation and semantic transformation
"""

# Tier-3 envelope configuration
TIER3_ENVELOPE_VERSION = "1.0"

# Envelope schema definition
ENVELOPE_SCHEMA = {
    "envelope_id": str,
    "timestamp": str,
    "payload": str,
    "signature": str
}

# Required semantic fields for Tier-3
SEMANTIC_FIELDS = [
    "behavior_type",
    "intensity",
    "duration",
    "features_used",
    "_version",
    "_semantic"
]

# Optional semantic fields
OPTIONAL_SEMANTIC_FIELDS = [
    "metadata",
    "premium_indicator",
    "user_segment"
]

# Behavior type mappings (Tier-1 atomic → Semantic)
BEHAVIOR_TYPES = {
    "calculate": "computation",
    "process_data": "data_processing",
    "custom_behavior": "custom_action",
    "search": "research",
    "click": "interaction",
    "scroll": "navigation"
}

# Intensity normalization
INTENSITY_MIN = 0.0
INTENSITY_MAX = 1.0

# Envelope ID prefix
ENVELOPE_ID_PREFIX = "env_"

# Signature prefix  
SIGNATURE_PREFIX = "sig_"

# Default values
DEFAULT_BEHAVIOR_TYPE = "unknown"
DEFAULT_INTENSITY = 0.5
DEFAULT_DURATION = 0
