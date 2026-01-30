# Tier Responsibility Contrast

## Overview

This document defines **non-overlapping responsibilities** across SeekReap tiers.
Overlap is considered a design failure.

---

## Tier-1 — Signal Layer

**Role:** Signal generation and normalization

- Produces raw events
- Applies no meaning
- Performs no interpretation
- Knows nothing about intent

Tier-1 answers:  
> “What happened?”

---

## Tier-2 — Semantic Layer

**Role:** Meaning assignment and validation

- Interprets signals
- Creates semantic envelopes
- Enforces semantic rules
- Guarantees immutability

Tier-2 answers:  
> “What does it mean?”

---

## Tier-3 — Decision Layer

**Role:** Decision-making and policy application

- Consumes semantic envelopes
- Applies business logic
- Selects actions
- Produces decisions

Tier-3 answers:  
> “What should be done?”

---

## Tier-4 — Execution Layer

**Role:** Action execution

- Executes commands
- Performs I/O
- Interacts with systems
- Causes real-world effects

Tier-4 answers:  
> “Do it.”

---

## Absolute Rule

- Higher tiers may **read** lower tiers
- Lower tiers may **never depend on** higher tiers
- Semantic meaning NEVER flows upward or downward incorrectly

Tier-2 is the **semantic firewall** of the system.
