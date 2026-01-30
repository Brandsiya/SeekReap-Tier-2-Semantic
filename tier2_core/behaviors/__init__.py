"""
TIER-2 BEHAVIORS: Semantic Behavior Implementations

This package contains Tier-2 specific behaviors and constants
that complement Tier-1 atomic operations with semantic meaning.

ARCHITECTURAL ROLE:
- Provides semantic context for atomic operations
- Defines constants for orchestration logic
- Implements Tier-2 specific transformations
- Maintains clear separation from Tier-1

BOUNDARIES:
- Does not redefine Tier-1 behavior signatures
- Does not violate Tier-0 protocol invariants
- Does not claim authority over other tiers
"""

__all__ = ["constants"]
