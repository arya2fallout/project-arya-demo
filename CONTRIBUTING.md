# Contributing to Project Arya

Independent review, reproducibility feedback and fictional test cases are welcome. This is a small, early-stage project maintained by its owner with AI assistance.

## Getting started
Read the [README](README.md), [roadmap](ROADMAP.md), [benchmark methodology](BENCHMARKS.md) and [security policy](SECURITY.md). Try the static demo at https://arya2fallout.github.io/project-arya-demo/ or open index.html locally. No account, model or API key is necessary for the static demo.

## Useful contributions
- Report reproducible bugs, ambiguous retrieval cases, accessibility issues, or misleading documentation.
- Suggest independent fictional held-out questions, with expected answers and sources or expected abstention. Keep proposed held-out sets separate from tuning fixtures until frozen.
- Propose narrowly scoped changes with tests. Do not include private code, model weights, credentials, personal data or operational logs.

For a non-sensitive issue, include version/commit, environment, steps, expected and actual result, and sanitized evidence. See SECURITY.md for sensitive reports.

## Checks before proposing changes
From the repository root, with Python 3.10+ and Node.js installed:
```sh
python benchmark.py
python -m unittest -v test_benchmark.py
node test_demo.js
```
Report actual outcomes, including failures. The optional Ollama experiment is not required and should be run only by explicit choice. Do not represent synthetic checks as model accuracy or production security certification.

Open a focused pull request explaining motivation, changes, tests, and limitations. Disclose material AI assistance and verify rights to submitted content. Contributions to demo source, fixtures, tests and associated usage documentation must be compatible with the MIT license; the separately published measured-results reports are not offered under a separate reuse license. The maintainer reviews and decides whether to accept changes. Be respectful, constructive and mindful of privacy.
