# Architecture Decision Records

## Recorded Decisions

### ADR-001: Deep Copy Implementation
**Status**: Accepted  
**Context**: Need to ensure envelope immutability guarantees  
**Decision**: Use `copy.deepcopy()` for all envelope contents  
**Consequences**: Increased memory usage, true immutability  
**Alternatives**: Shallow copy, serialization, immutable data classes

### ADR-002: Signature Format
**Status**: Accepted  
**Context**: Need unique, traceable envelope identifiers  
**Decision**: `tier2-structural-{policy}-{timestamp_ms}-{random}`  
**Consequences**: Policy traceability, temporal ordering, uniqueness  
**Alternatives**: Simple UUID, cryptographic hash, sequential IDs

### ADR-003: Required Fields Structure
**Status**: Accepted  
**Context**: Need consistent envelope structure for validation  
**Decision**: Fixed set of required fields for all envelopes  
**Consequences**: Uniform validation, clear separation of concerns  
**Alternatives**: Flexible schema, tagged union, versioned schemas

### ADR-004: Validation Strategy
**Status**: Accepted  
**Context**: Need reliable envelope validation without side effects  
**Decision**: Pure validation function with no side effects  
**Consequences**: Idempotent validation, safe for multiple calls  
**Alternatives**: Mutating validation, exception-based, async validation

### ADR-005: Tier Separation Principle
**Status**: Accepted (Fundamental Law)  
**Context**: Need architectural boundaries to prevent contamination  
**Decision**: Each tier can only read from tiers below, never modify  
**Consequences**: Clear separation, prevents circular dependencies  
**Alternatives**: Bidirectional communication, shared models
