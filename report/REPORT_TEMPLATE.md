# A3 report template

Name: Ben Shuster
Commit SHA: 578d5d38f81d6a91d55e4dd9b70738f8c690234b

## Part 1. Evidence log

Insert 8 to 10 E, A, and Q entries using the table in `evidence/schema.md`.

## Part 2. Evidence audit

One row for each item: contradiction, ambiguity 1, ambiguity 2, missing stakeholder, compliment, prediction about future use, strongest past event.

<!-- Here is the seven-row audit table evaluating the transcript details against requirements engineering principles: -->
| Item | Location | Classification | Why it matters |
| --- | --- | --- | --- |
| **1. Direct Factual Contradiction** | INT-01:P06, INT-01:P12 | Contradiction (Policy vs. User Expectation) | Jordan states the grace period policy is 15 minutes, whereas Priya states students are told it is 20 minutes. Hardcoding or assuming either rule without stakeholder alignment risks building a system that unfairly penalizes users or violates operational policy. |
| **2. Ambiguous Statement 1** | INT-01:P07 | Ambiguity (Vague Time/Distance) | Jordan notes that issues arise when someone is "only a little late" or walking from "another building." Unclear terms like "a little late" cannot be translated into functional logic or automated system triggers without precise thresholds. |
| **3. Ambiguous Statement 2** | INT-01:P10 | Ambiguity (Unclear Actor/Recipient) | Jordan states "They should get a message," but fails to clarify whether "they" refers to the original late borrower, the waitlisted student, or desk staff. Unclear actors create ambiguity regarding system notification workflows and destination roles. |
| **4. Missing Stakeholder** | INT-01:P09, INT-01:P19, INT-01:P21 | Missing Stakeholder Group | Equipment technicians process physical inventory, set kit readiness, and verify components, yet none were interviewed. Designing equipment readiness and checkout workflows without direct input from the technicians risks creating unusable or disruptive operational steps. |
| **5. Compliment** | INT-01:P14 | Compliment / Polite Praise | Priya remarks that a reservation dashboard fixing these issues "would be amazing." Flattery or general enthusiasm cannot be treated as evidence of actual software utility, user needs, or functional specifications. |
| **6. Prediction About Future Use** | INT-01:P15 | Speculative Future Behavior | Priya claims she would "probably use" a "running late" button every time she is delayed. Stated future intentions in interviews are notoriously unreliable indicators of real-world adoption and must not be treated as empirical usage evidence. |
| **7. Strongest Account of Past Event** | INT-01:P13 | Concrete Historical Episode (Observed Event) | Priya provides a detailed, step-by-step account of her experience last Thursday, complete with precise times, specific locations, phone call attempts, and system breakdowns. Concrete past events reveal real process failures and actual user workarounds rather than idealized workflows. |


## Part 3. Requirements, INVEST, and acceptance criteria

### Four requirement slices

For each of R-1 to R-4: user story, structured requirement, and evidence trace, or `Assumption` plus a clarifying question.

### INVEST check

| Requirement | I | N | V | E | S | T | Named problem for any fail |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Three acceptance criteria

AC-1 to AC-3 in Given-When-Then form, each traced to a different requirement.

## Part 4. Implementation-ready specification

Paste your completed `spec/spec_template.md`.

## Part 5. Tests

| Test name | AC ID | Requirement ID | Evidence ID |
| --- | --- | --- | --- |

## Part 6. AI audit and synthetic-user critique

### Audit adjudication

For every finding in `results/ambiguity_audit.md`: true positive or false positive, the paragraph IDs, and one sentence explaining the decision.

### Synthetic-user critique

Every claim in `synthetic/synthetic_user_output.md` that INT-01 does not establish. Quote the claim and explain why the interview does not support it.

## Part 7. Traceability and ledger

Paste the completed matrix from `traceability/template.csv`. The ledger stays in `LEDGER.md` in the repository.

## Verification

Paste the final output of `python -m pytest -q`.
