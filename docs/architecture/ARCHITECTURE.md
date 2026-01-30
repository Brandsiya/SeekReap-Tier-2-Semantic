# Tier-2 Structural Envelope Architecture

## Overview

Tier-2 Structural Envelopes provide a structured approach to workflow composition and orchestration in multi-tier systems. This architecture enables semantic meaning to be added to data flows while maintaining strict boundaries between architectural tiers.

## Core Architectural Principles

### 1. Tier Separation (The Fundamental Law)
**"Each tier can only read from tiers below, never modify or redefine their meaning."**

- **Tier-0**: Protocol definitions (immutable, normative)
- **Tier-1**: Atomic behaviors (read-only from Tier-0)
- **Tier-2**: Workflow composition (read-only from Tier-1)
- **Tier-3+**: Application logic (read-only from Tier-2)

### 2. Immutability by Design
- All envelope contents are deep copied at creation
- Original input data remains untouched
- Envelopes form immutable audit trails
- Historical states are preserved, not overwritten

### 3. Semantic Layering
- **Structural Layer**: Required fields (id, timestamp, schema_version)
- **Semantic Layer**: Policy, signature, orchestration context
- **Domain Layer**: Application-specific metadata and payload
- **Validation Layer**: Cross-cutting validation rules

## Architecture Decisions

### AD-1: Deep Copy Implementation
**Decision**: Use `copy.deepcopy()` for all envelope contents
**Rationale**: 
- Prevents accidental mutation of original data
- Ensures true immutability guarantees
- Allows safe sharing of envelope references
- Supports nested data structures

**Alternatives Considered**:
- Shallow copy: Insufficient for nested structures
- Serialization/deserialization: Overhead without benefits
- Immutable data classes: Breaks backward compatibility

### AD-2: Signature Format
**Decision**: `tier2-structural-{policy}-{timestamp_ms}-{random}`
**Rationale**:
- Policy traceability in signature
- Millisecond precision for temporal ordering
- Random component ensures uniqueness
- Clear semantic structure

**Format Details**:
- `tier2-semantic-`: Prefix identifying Tier-2 structural envelopes
- `{policy}`: Orchestration policy applied (e.g., "default")
- `{timestamp_ms}`: Millisecond timestamp for ordering
- `{random}`: Random UUID component for uniqueness guarantee

### AD-3: Required Fields Structure
**Decision**: Fixed set of required fields for all envelopes
**Rationale**:
- Consistent structure enables predictable processing
- Validation can be performed uniformly
- Interoperability between different envelope producers
- Clear separation of concerns

**Required Fields**:
```python
{
    "id": "tier2-envelope-{uuid}",          # Unique identifier
    "timestamp": float,                     # Creation timestamp
    "payload": any,                         # Original data (deep copied)
    "schema_version": "tier2-envelope-v1",  # Schema identifier
    "orchestration_policy": string,         # Applied policy
    "signature": string,                    # Envelope signature
    # Optional:
    "metadata": dict                        # Domain-specific metadata
}
