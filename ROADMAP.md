# Project Arya roadmap

This is a volunteer, independently maintained research demonstration. Priorities are proposals, not delivery dates, funded commitments, or evidence of adoption. The owner makes final scope, licensing and release decisions; AI-assisted contributions are reviewed by the maintainer.

## Established baseline
- [v0.2.0](https://github.com/arya2fallout/project-arya-demo/releases/tag/v0.2.0): fictional-data deterministic retrieval and policy simulation.
- [Public measured results](Measured_Results_2026-11-26.txt): separate desktop inference and private bridge experiments, with negative results retained.
- [Matched GPU baseline](research/2026-11-26-matched-gpu.md), [knowledge baseline](research/2026-11-26-knowledge.md) and [execution baseline](research/2026-11-26-execution.md): subsequent experimental summaries with limitations.
- No real command execution, live private bridge, or production security guarantees in the public demo.

## Next priorities
1. **Independent evaluation:** recruit volunteers through GitHub issues; freeze independently authored fictional held-out questions before tuning; report failures, abstentions, and human adjudication separately from fixture smoke tests.
2. **Security:** expand synthetic denial, malformed-input, expiry, replay and approval cases; document threat assumptions and review dependencies and browser behavior. Do not connect the demo to real files or credentials.
3. **Reproducibility:** the matched GPU baseline is complete; the long delay remains causally unresolved despite targeted CUDA profiling. Pursue separately scoped CPU/thread profiling, independent replication and fuller context-window tests. Do not replace the original baseline.
   - Corrective engineering priorities include mandatory source acquisition, version precedence, citation validation, byte preservation, independent completion checks and transaction recovery. Validate with separately labeled regression and fresh held-out tests before claiming improvements.
4. **Mobile:** document device, app version, model, settings and measurement controls before publishing mobile results.
5. **Maintenance:** triage genuine feedback, review contributions, run relevant checks, and record substantive changes and limitations in future releases.

See [benchmark methodology](BENCHMARKS.md), [contributing](CONTRIBUTING.md), and [security reporting](SECURITY.md). No community adoption or funding is asserted.
