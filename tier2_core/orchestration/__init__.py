"""
TIER-2 ORCHESTRATION: Workflow Composition Layer

This package contains orchestration logic that composes
Tier-1 atomic behaviors into semantic workflows with policy
and governance rules.

ARCHITECTURAL ROLE:
- Orchestrates Tier-1 behaviors into workflows
- Applies policy rules to behavior selection
- Creates semantic envelopes around outputs
- Provides deterministic composition patterns

NAMING CONVENTION:
All orchestration modules use the 'tier2_' prefix to clearly
identify their role and maintain architectural clarity.

EXAMPLES:
- tier2_orchestrator.py: Main orchestration logic
- tier2_policy_composer.py: Policy composition (future)
- tier2_workflow_builder.py: Workflow construction (future)

BOUNDARIES:
- Orchestrates, does not implement
- Composes, does not modify
- Adds meaning, does not redefine
- Provides patterns, does not claim authority
"""

__all__ = ["tier2_orchestrator"]
