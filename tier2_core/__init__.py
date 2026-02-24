"""
SeekReap Tier-2 Semantic Orchestration Layer
Version: 0.1.0-dev

This layer consumes Tier-1 atomic behaviors and produces semantic envelopes
for consumption by Tier-3 decision layers.
"""

__version__ = "0.1.0-dev"

from .orchestration.envelope import (
    create_envelope,
    create_envelope_from_tier1,
)

from .orchestration.validation import (
    validate_envelope_structure,
    validate_envelope_semantics,
    validate_policy_compliance,
)

__all__ = [
    # Envelope creation
    "create_envelope",
    "create_envelope_from_tier1",
    
    # Validation
    "validate_envelope_structure",
    "validate_envelope_semantics",
    "validate_policy_compliance",
]
