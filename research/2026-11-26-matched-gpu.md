# Matched consumer GPU inference: a single-desktop study

Project Arya | Experimental baseline | 26 November 2026

## Method
A separate matched experiment used ten fixed prompts, five repetitions, two models and two GPUs: 200 measured calls, all without generation errors. Priming was excluded. Both models used Q4_K_M, temperature 0, seed 42, configured context 2048, output cap 128 and thinking disabled. Model digests were matched; Ollama 0.40.18 and NVIDIA driver 621.40 were used. Actual model-process GPU placement was verified. The RTX 4060 Ti continued to drive the desktop and normal background services remained active. This is not a fully isolated hardware comparison. The earlier [historical snapshot](../Measured_Results_2026-11-26.txt) used driver 621.14; its observations were not pooled.

## Results

| GPU | Model | Calls | Median decode (tokens/s) | Median wall (s) | p95 wall (s) | Max wall (s) |
|---|---|---:|---:|---:|---:|---:|
| RTX 3060 Ti 8 GB | Qwen 3.5 4B | 50 | 81.920 | 1.603 | 1.702 | 54.648 |
| RTX 4060 Ti 16 GB | Qwen 3.5 4B | 50 | 64.307 | 2.077 | 2.191 | 54.502 |
| RTX 3060 Ti 8 GB | Qwen 2.5 Coder 7B | 50 | 76.987 | 1.437 | 1.731 | 1.734 |
| RTX 4060 Ti 16 GB | Qwen 2.5 Coder 7B | 50 | 51.175 | 2.150 | 2.603 | 2.661 |

Decode rate is evaluated tokens divided by runtime evaluation duration; wall time is end-to-end latency. The 3060 Ti's observed median decode rates were approximately 27.4% and 50.4% higher respectively. The finding applies to this configuration and workload, not a universal GPU ranking. Successful generation does not establish answer correctness.

## Outlier investigation
The historical 54.485864 s delay was retained. The same first-pass prompt produced 54.648 s and 54.502 s delays on the respective GPUs; Ollama attributed almost all of these delays to prompt evaluation. That timing attribution does not establish a mechanism.

A separate 16-call Nsight Systems diagnostic capture recorded 70,731 CUDA runtime events and 16,378 kernel events. The long delay did not recur during profiling: the relevant sequence prompt took approximately 0.714 s and the first call after model reload took 8.817 s. CPU sampling and thread-scheduling capture were unavailable without elevated privileges. The cause remains unresolved. Community profiling advice informed separation of load, prompt and decode timing and retention of outliers; this is not vendor endorsement.

## Context capacity
Both models and GPUs were tested at configured contexts 2048, 4096, 8192, 16384 and 32768. Initial calibration recorded two Qwen 3.5 HTTP 400 rejections and ten Coder input-truncation observations; these were preserved, not discarded. All 20 corrected tests completed without generation errors and retained beginning, middle and ending markers. At configured 32768, actual tested inputs were 14,718 tokens (Qwen 3.5) and 14,700 (Coder) on each GPU. These are successful tested inputs, not full-window validation or reasoning-accuracy results. Oversized Coder inputs showed truncation to roughly half configured context; do not generalize this to other models.

## Evidence boundaries
Original configurations were reported unchanged and normal inference placement restored after testing. Raw prompts, model digests, measurements, telemetry and traces are retained privately. This report is a sanitized summary, not a full reproducibility package. Independent replication and elevated CPU/thread investigation remain open. No power-cost, mobile, general hardware superiority or sponsor claim is made. AI assistance was used in execution and documentation.

This research summary is publicly readable; no additional reuse license is granted for the report itself.
