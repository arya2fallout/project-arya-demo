# Benchmark methodology and evidence boundaries

## Public reproducible checks
Use the commands in [README.md](README.md). The Python baseline and Node checks use the repository's fictional records and purpose-built questions. The recorded baseline is seven Python unit tests, 35 deterministic retrieval fixtures and ten policy cases. These are smoke tests, not independently held-out model accuracy or a security audit.

## Optional local inference
Use an installed Ollama model, with Ollama already running locally:
```sh
python benchmark.py --model YOUR_INSTALLED_MODEL --repeats 1 --output new-results.csv
```
The harness uses 127.0.0.1 (default port 11434), disables proxies and redirects, and refuses to overwrite the output. It makes 70 non-streamed calls per repeat, alternating context-on/off order. Options: temperature 0, seed 42, context 2048, output cap 128. Record the exact model digest, runtime/driver versions, hardware, OS, background load, power settings and any model-specific defaults separately.

The CSV includes response text, errors, wall time, token counts, evaluation and prompt durations, load duration, completion reason, decode rate and phrase/source-ID screening. Decode tokens/s = evaluation token count divided by evaluation duration in seconds. This non-streamed harness does not measure TTFT, power or peak VRAM. Review actual answers and errors; phrase matches alone do not establish correctness.

## Separate historical experiment
The [November 26 public report](Measured_Results_2026-11-26.txt) describes 50 measured fixed-prompt calls per configuration on RTX 3060 Ti, separate paired retrieval runs and private bridge tests. Those streamed measurements, including TTFT, are not identical to the public harness. Raw private logs are not published. The 54.486-second outlier and output cap hits remain in the report.

## Matched GPU experimental design and subsequent results
Freeze the prompt set, exact model digests, settings, runtime, driver and machine conditions before testing. Verify which GPU actually runs inference. Use identical prompts and repetitions for each GPU, document placement/offload and background activity, alternate or counterbalance run order, and separate priming from measured runs. Record warm/cold conditions rather than assuming them. Keep all failures, timeouts and outliers. Report sample size, error counts, median, nearest-rank p95, maximum, token counts and cap hits; separate decode rate from end-to-end latency. If measuring TTFT or resource use, document instrumentation and sampling limits. The subsequent [matched GPU report](research/2026-11-26-matched-gpu.md) describes the completed 200-call baseline and its configuration-specific limitations; the historical report remains unchanged.

## Independent grounding evaluation
Freeze held-out synthetic cases before tuning. Separate answerable and absent-information cases, adjudicate factual correctness, unsupported additions, citations and abstention independently of phrase screening, and retain disagreements. Document selection and reviewer limitations. The subsequent [knowledge study](research/2026-11-26-knowledge.md) reports 60 trials with AI semantic adjudication, and the [execution study](research/2026-11-26-execution.md) reports 24 sandbox trials. Neither establishes independently authored held-out replication, independent human adjudication or mobile performance.
