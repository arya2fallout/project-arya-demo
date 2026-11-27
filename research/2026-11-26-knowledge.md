# Persistent knowledge and cross-session retrieval: experimental baseline

Project Arya | PA-FIX-001 v1.0 | 26 November 2026

## Design
A minimal local experimental runner (not the production Arya bridge) evaluated 30 questions against 15 fictional source records. Each question was run once with and once without context, yielding 60 actual model trials. Six categories had five questions each: exact retrieval, paraphrases, conflicting versions, multi-document synthesis, missing information and cross-session requirements. Fixtures and evaluator keys were frozen before initial trials; keys were excluded from model-facing inputs.

Model: qwen3.5:4b, digest d8b0f5e9760cd1682034f292d7ef72ec46f432149be0df7574bf2d6e92e38c04. Temperature 0, seed 2601126, context 8192, generation limit 1024, thinking disabled. A retrospective single AI adjudicator assessed semantic correctness and source attribution. No independent human review or independently authored held-out replication is claimed.

## Results
| Category | Context off | Context on |
|---|---:|---:|
| Exact retrieval | 0/5 | 5/5 |
| Paraphrase | 0/5 | 3/5 |
| Conflicting versions | 0/5 | 3/5 |
| Multi-document synthesis | 0/5 | 3/5 |
| Missing information (correct abstention) | 5/5 | 5/5 |
| Cross-session requirements | 0/5 | 0/5 |
| Overall task accuracy | 5/30 | 19/30 |

Overall factual/task accuracy rose from 16.7% to 63.3% (+46.7 percentage points using unrounded fractions). On answerable cases it rose from 0/25 to 14/25. Both factual correctness and exact source attribution were achieved on 12/25 answerable context-on cases. Context-off abstained 30/30; context-on abstained 13/30. Abstention is not synonymous with accuracy. The proposed 27/30 factual target was not met.

Adjudication accepts semantic equivalents that answer the actual question, without requiring unasked details. A correct component-fact answer that omits the requested total is partial, not fully correct. Extra irrelevant or malformed citation IDs fail exact source-set scoring. An unsupported assertion about the identity of an approving operator fails factual scoring even when other prerequisites are correct.

Observed weaknesses included unnecessary abstention, stale version selection, malformed source ID, incomplete calculation, and an unsupported approval-role inference.

## Cross-session result
A durable synthetic store was seeded by a separate process that terminated. Ten actual trials used separate processes and fresh conversations (five per condition). All five context-on trials answered unknown without invoking retrieval. The original ten blocked preflight records were retained but not counted as model trials. Successful persistent retrieval was not demonstrated, and no native model-memory claim is supported.

## Proposed engineering response
Require source acquisition for source-dependent requests, enforce current source authority, validate citations, check answer completeness and distinguish evidence from assumptions. These are proposed improvements, not verified corrective results.

## Limits
Small purpose-built fictional corpus; one model, one trial per question/condition, single desktop and AI adjudicator. No claim of general accuracy, human review, production reliability or causal generalization. Private evidence and evaluator keys are retained; this is not a complete independently runnable benchmark release. AI assistance was used in testing and reporting.

This research summary is publicly readable; no additional reuse license is granted for the report itself.
