# Project Arya: synthetic personal-AI research demo

An independent, AI-assisted research prototype by Kirk / arya2fallout. This repository contains a portable fictional-data demo, repeatable fixture checks, an optional local Ollama harness, and a sanitized desktop-results snapshot dated 26 November 2026.

## Try it

Download this repository and open `index.html` in a browser. The standalone page needs no server, API key or model. It performs deterministic keyword retrieval and simulates permission decisions. It cannot read real files or execute commands. It is **not** a live Arya 2 integration, a language model or proof of production security.

## Run the checks

Python 3.10 or later; no third-party Python packages required:

```sh
python benchmark.py
python -m unittest -v test_benchmark.py
```

With Node.js installed:

```sh
node test_demo.js
```

The current checks pass seven Python tests, 35 deterministic retrieval fixtures and ten policy scenarios. Ten fictional records and 35 purpose-built questions are provided. These are smoke tests, not an independently held-out accuracy benchmark.

## Optional local-model experiment

If Ollama is already running locally, replace the placeholder with an installed model:

```sh
python benchmark.py --model YOUR_INSTALLED_MODEL --repeats 1 --output new-results.csv
```

This explicitly requested run makes 70 generation calls per repeat to IPv4 loopback, alternating context-on and context-off conditions. It disables proxies and redirects, and refuses to overwrite the output CSV. It does not install models or contact a hosted API. It records fact-phrase/source-ID screening and runtime timings; it does not measure time to first token, power or peak VRAM. Review errors and actual answer text before interpreting scores.

## Measured desktop findings

Read [the public results PDF](Measured_Results_2026-11-26.pdf) or its [text version](Measured_Results_2026-11-26.txt). The separate live phase measured 50 fixed-prompt calls each for Qwen 3.5 4B and Qwen 2.5 Coder 7B on an RTX 3060 Ti, plus 70 paired retrieval calls and bridge reliability/safety tests. The public demo does not reproduce the private operational bridge tests.

One inference call took 54.49 seconds. Many answers reached the 128-token cap. Synthetic retrieval exposed an unsupported addition, an invented source without context, and phrase-scoring limitations. The first repair regression had an OpenCode-health failure that was corrected before the final 30/30 healthy run. Negative outcomes remain part of the record.

No mobile benchmark, matched comparison with the installed RTX 4060 Ti, independent human adjudication, long-duration stability test or energy-cost result is claimed. Full private operational logs are not included. The summary alone does not independently reproduce every desktop measurement.

## Scope and contributions

Useful next work includes an independently authored held-out dataset, repeatability and stall diagnosis, and fair comparisons of existing hardware. Please use fictional examples in issues; never post credentials, private conversations or operational logs. No sponsor award, affiliation, institutional eligibility, service level or delivery schedule is claimed.

### Community and maintenance

- [Development roadmap](ROADMAP.md)
- [Security policy and reporting](SECURITY.md)
- [Contribution guidelines](CONTRIBUTING.md)
- [Benchmark methodology](BENCHMARKS.md)
- [Independent testing invitation (issue #1)](https://github.com/arya2fallout/project-arya-demo/issues/1)

## License and disclosure

The demo source, fixture data, tests and associated usage documentation are released under the [MIT License](LICENSE), as approved by the owner. The separately authored measured-results PDF and text are public for reading; their inclusion does not grant a separate reuse license for those reports. No third-party model weights, game assets or private project code are distributed.

Code, tests and documentation were prepared with AI assistance and reviewed through the checks described above. The work has not had independent peer review or a comprehensive security audit.
