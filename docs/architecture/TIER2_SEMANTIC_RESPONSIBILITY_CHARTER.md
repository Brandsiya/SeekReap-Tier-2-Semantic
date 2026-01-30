# Tier-2 Semantic Responsibility Charter

## Status
**Binding · Non-Optional · Enforced**

## Purpose

This charter formally defines and locks the exclusive responsibilities of **Tier-2 (Semantic Layer)** within the SeekReap architecture.

Tier-2 is the **sole authority for semantic meaning**.  
No other tier may create, alter, reinterpret, or bypass semantics.

---

## Core Mandate

Tier-2 is responsible for:

1. **Semantic Interpretation**
   - Transforming Tier-1 outputs into meaningful, structured representations.
   - Assigning semantic labels, categories, and intent.

2. **Semantic Validation**
   - Enforcing semantic correctness via pure, deterministic validation.
   - Validation MUST be idempotent and side-effect free.

3. **Semantic Immutability**
   - All produced semantic envelopes MUST be immutable.
   - Deep copies are mandatory to prevent mutation leakage.

4. **Semantic Traceability**
   - Every envelope MUST include:
     - Policy reference
     - Creation timestamp
     - Unique signature
     - Provenance metadata

---

## Explicit Prohibitions

Tier-2 MUST NOT:

- Execute runtime loops
- Spawn daemons, workers, or schedulers
- Perform I/O, networking, or persistence
- Maintain queues, buffers, or async state
- Call external services or APIs
- Interpret business outcomes or user intent

Tier-2 is **not** a service.  
Tier-2 is **not** an orchestrator of execution.  
Tier-2 is **not** a policy decider.

---

## Boundary Contract

### Inputs (Allowed)
- Tier-1 signals
- Tier-1 metadata
- Explicit semantic policies

### Outputs (Allowed)
- Semantic envelopes
- Validation results
- Structural metadata

### Outputs (Forbidden)
- Commands
- Actions
- Execution triggers
- Side effects

---

## Enforcement

Violations of this charter:

- Invalidate Tier-2 compliance
- Require immediate refactor or removal
- Block promotion to higher tiers

This charter supersedes implementation convenience.

**Tier-2 semantics are law.**
