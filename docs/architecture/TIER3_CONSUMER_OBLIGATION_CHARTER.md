# Tier-3 Consumer Obligation Charter

## Status
Binding · Enforced · Non-Negotiable

## Purpose

This charter defines the mandatory obligations of **Tier-3 (Decision Layer)**
when consuming outputs from Tier-2.

Tier-3 is a **consumer only** of semantics.

---

## Mandatory Obligations

Tier-3 MUST:

1. Treat Tier-2 envelopes as immutable truth
2. Never reinterpret semantic meaning
3. Never mutate semantic payloads
4. Apply decisions strictly based on semantic fields
5. Preserve semantic provenance in all downstream outputs

---

## Prohibited Actions

Tier-3 MUST NOT:

- Modify semantic labels
- Infer alternative meaning
- Re-validate semantics
- Bypass Tier-2 validation
- Construct its own semantic structures

Tier-3 decides **actions**, not **meaning**.

---

## Contractual Flow

Tier-2 → Meaning  
Tier-3 → Decision  
Tier-4 → Execution  

Breaking this flow is a **hard architectural violation**.

---

## Enforcement

Any Tier-3 system found altering semantic content:

- Loses Tier-3 compliance
- Must be refactored or removed
- Cannot proceed to execution layers

Tier-2 semantics are final.
