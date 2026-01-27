# Tier-2: Library-Only Architecture

## Architecture Declaration
**Effective:** 2026-01-27  
**Authority:** Tier-1 lock (v1.0.0-tier1-lock)  
**Version:** v0.1.0-tier2  

## Core Principle
Tier-2 is exclusively a **semantic transformation library**. It contains no runtime, service, orchestration, or monitoring logic.

## Library Responsibilities
1. **Semantic Transformation**
   - Convert Tier-1 atomic behaviors → semantic objects
   - Normalize intensity, type, and duration
   - Map atomic types to semantic types

2. **Envelope Creation**
   - Produce opaque envelopes for Tier-3 consumption
   - Include signatures and timestamps
   - Ensure schema compliance

3. **Contract Enforcement**
   - Consume Tier-1 atomic behavior dictionaries only
   - Produce Tier-3 envelope schema only
   - Maintain deterministic behavior

## Prohibited in Tier-2
 Long-running processes or daemons  
 Signal handling or process management  
 Queue or stream consumption/production  
 Metrics collection or export  
 Monitoring or alerting logic  
 Service orchestration  
 Integration with external systems (beyond library calls)

## Library Interface
```python
from semantic.orchestrator import SemanticOrchestrator

# Instantiate library
orchestrator = SemanticOrchestrator()

# Transform Tier-1 → semantic
semantic = orchestrator.transform_to_semantic(atomic_behavior)

# Create envelope for Tier-3
envelope = orchestrator.create_envelope(semantic)

# Volatile statistics (for debugging)
stats = orchestrator.get_library_stats()
