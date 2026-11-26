# Security policy

## Scope and support
The public repository is an experimental fictional-data demonstration, not a production security boundary. The latest public release is the primary target for best-effort review; no response SLA or ongoing support guarantee is offered. The private Arya prototype and its operational infrastructure are outside this repository.

The JavaScript policy checks simulated operation, path, explicit write approval, expiry and supplied replay state. It does not execute actions or provide durable replay protection, authenticated requests, or real filesystem isolation. The optional Python model harness explicitly contacts an already running IPv4 loopback Ollama endpoint and writes a newly chosen CSV. Do not treat either component as certified secure.

## Reporting
For suspected vulnerabilities, do not publish exploit details, credentials, personal data, private logs, or information about real systems in public issues. Use GitHub's private vulnerability reporting option under the repository Security tab if available. If unavailable, open a minimal issue asking the maintainer to arrange a private reporting channel; include no sensitive details.

In a private report, include affected version or commit, component, synthetic reproduction steps, expected and observed behavior, potential impact, and relevant sanitized environment details. Test only your own authorized environment. Do not probe other users or the private prototype.

Ordinary non-sensitive defects and proposed synthetic tests can be reported in [GitHub issues](https://github.com/arya2fallout/project-arya-demo/issues). The maintainer will review reports on a best-effort basis, coordinate disclosure where practical, and document fixes and limitations. No bounty or financial reward is promised.
