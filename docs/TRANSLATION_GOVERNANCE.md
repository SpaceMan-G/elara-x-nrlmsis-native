# Translation Governance

1. Translate one authoritative Fortran module at a time.
2. Record the exact source counterpart in every translated file.
3. Preserve scientific formulation and double-precision intent.
4. Add unit tests before downstream integration.
5. Compare completed layers against the independent official NRL oracle.
6. pymsis is not the production engine.
7. Scientific deviations must be explicit; silent deviations are prohibited.
8. Do not call the implementation verified until locked acceptance tests pass.
9. MR06/C01/NP4 remain outside this development programme.

## Public Release Gate

The repository may remain private while it contains only non-derived scaffolding,
governance, tests, continuous-integration configuration, and other pre-translation
infrastructure.

Before translation of NRLMSIS 2.1 scientific source begins:

1. this component repository must be intentionally made public;
2. the public remote must be independently verified;
3. the public commit and tree must match the accepted release baseline;
4. the NRLMSIS licence, required notices, provenance, and change-governance material
   must remain present; and
5. a controlled translation phase must explicitly unlock the scientific
   implementation gate.

Scientific translation must not begin while the repository remains private.

Changing repository visibility is a separate controlled action and requires explicit
authorization. Public visibility alone does not constitute scientific verification.
