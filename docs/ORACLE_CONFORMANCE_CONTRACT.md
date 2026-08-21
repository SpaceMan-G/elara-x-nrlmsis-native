# Oracle Conformance Contract

## Scope

This document defines the **verification boundary** for the native NRLMSIS component.
It does not contain translated NRLMSIS equations, coefficients, parameter payloads, or
official NRL test vectors.

The native implementation is not scientifically accepted merely because it executes,
imports, agrees with a third-party wrapper, or produces physically plausible values.

## Primary authority

The primary implementation-verification authority is the official NRLMSIS 2.1 source
and its official double-precision reference-output workflow acquired and locked outside
this repository.

Locked provenance:

- Official NRLMSIS 2.1 source archive SHA-256:
  `4b2ef2e9989681d3d5c1eade0c7f91f2050e839b4492d56ba9de21231d635fd8`
- Official double-precision reference output SHA-256:
  `59210a442f175b6b3f9e15034856989eea46d54ddb4fe3057a289a77512b7ce3`
- Official reference record count: `200`

The official Fortran source, parameter payload, and reference-output payload are not
copied into this private pre-translation repository by this infrastructure phase.

## Verification hierarchy

1. Repository and interface tests.
2. Module-level native equivalence tests as translation proceeds.
3. Native full-model comparison against the official NRL authority.
4. AMVS Layer 1 implementation-verification acceptance.
5. External density validation and later scientific benchmarking.

A third-party package such as `pymsis` may be used only as a secondary development
comparator. It is not the scientific acceptance oracle.

## Fixture governance

`tests/fixtures/` currently contains schema and governance metadata only.

Before any official or derived numerical fixture is added, a later controlled phase
must record:

- provenance and authority;
- source hashes;
- generation method;
- licence/distribution status;
- exact payload hash;
- units and field semantics;
- record count;
- comparison tolerances and rationale.

The numerical tolerance for native Python versus the official NRL implementation is
**not locked in this phase**. It must be established before scientific acceptance and
must not be inferred from the exact-byte reproduction criterion used to verify the
official Fortran reference run.

## Current gate

The repository is private. Scientific translation from the NRL source remains blocked
until a later explicit phase makes the component public and independently verifies the
public remote state.
