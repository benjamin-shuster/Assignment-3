# Provenance ledger

Use exactly this format for every entry. Write each entry when the work is done, one entry per reviewable change.

```text
## Entry <n>
artifact:  what this entry covers: a file, a commit SHA, a document, or an experiment
tool:      product name, model name, model version, and the date of use
prompts:   one-line summary each; the verbatim prompts live in prompts/ and are
           referenced here by file path
review:    what you read, what you changed, what you rejected, and why
checks:    the commands you ran and their results
evidence:  the requirement, test, or evidence ID this traces to
risk:      what remains unverified after this change

For an experiment, add three fields:
dataset:   task set identifier and its commit SHA or version
result:    metric, N, and the result table or its file path
changed:   what you did differently as a result
```

Add your entries below this line, starting with Entry 1.

---

## Entry 1
artifact: Assignment-3/results/ambiguity_audit.md
tool:      ChatGPT web UI, 2026-10-10
prompts:   Audit the attached interview transcript as a requirements reviewer. Find ambiguity, incompleteness, and direct contradictions that could cause an implementation team or coding agent to invent product behavior. Return at most 8 findings. For each finding, provide: a short label, the paragraph ID or IDs, a short excerpt, the defect type, and one sentence explaining what decision remains unsafe. Do not resolve the issue, do not add product facts, and do not use synthetic-user material as evidence.
review:    cross refrenced the transcript and the ambiguity audit, verified that each finding is supported by the transcript, and confirmed that no synthetic-user material was used as evidence. Rejected any findings that were not clearly supported by the transcript or that relied on synthetic-user material.
evidence:  Step 6
risk:      low, manualy verified that the ambiguity audit findings are supported by the transcript and do not rely on synthetic-user material.