# A3 report template

Name: Ben Shuster
Commit SHA: 578d5d38f81d6a91d55e4dd9b70738f8c690234b

## Part 1. Evidence log

Insert 8 to 10 E, A, and Q entries using the table in `evidence/schema.md`.

## Part 2. Evidence audit

One row for each item: contradiction, ambiguity 1, ambiguity 2, missing stakeholder, compliment, prediction about future use, strongest past event.

<!-- Here is the seven-row audit table evaluating the transcript details against requirements engineering principles: -->

| Item                                   | Location                           | Classification                               | Why it matters                                                                                                                                                                                                                                                                               |
| -------------------------------------- | ---------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Direct Factual Contradiction**    | INT-01:P06, INT-01:P12             | Contradiction (Policy vs. User Expectation)  | Jordan states the grace period policy is 15 minutes, whereas Priya states students are told it is 20 minutes. Hardcoding or assuming either rule without stakeholder alignment risks building a system that unfairly penalizes users or violates operational policy.                         |
| **2. Ambiguous Statement 1**           | INT-01:P07                         | Ambiguity (Vague Time/Distance)              | Jordan notes that issues arise when someone is "only a little late" or walking from "another building." Unclear terms like "a little late" cannot be translated into functional logic or automated system triggers without precise thresholds.                                               |
| **3. Ambiguous Statement 2**           | INT-01:P10                         | Ambiguity (Unclear Actor/Recipient)          | Jordan states "They should get a message," but fails to clarify whether "they" refers to the original late borrower, the waitlisted student, or desk staff. Unclear actors create ambiguity regarding system notification workflows and destination roles.                                   |
| **4. Missing Stakeholder**             | INT-01:P09, INT-01:P19, INT-01:P21 | Missing Stakeholder Group                    | Equipment technicians process physical inventory, set kit readiness, and verify components, yet none were interviewed. Designing equipment readiness and checkout workflows without direct input from the technicians risks creating unusable or disruptive operational steps.               |
| **5. Compliment**                      | INT-01:P14                         | Compliment / Polite Praise                   | Priya remarks that a reservation dashboard fixing these issues "would be amazing." Flattery or general enthusiasm cannot be treated as evidence of actual software utility, user needs, or functional specifications.                                                                        |
| **6. Prediction About Future Use**     | INT-01:P15                         | Speculative Future Behavior                  | Priya claims she would "probably use" a "running late" button every time she is delayed. Stated future intentions in interviews are notoriously unreliable indicators of real-world adoption and must not be treated as empirical usage evidence.                                            |
| **7. Strongest Account of Past Event** | INT-01:P13                         | Concrete Historical Episode (Observed Event) | Priya provides a detailed, step-by-step account of her experience last Thursday, complete with precise times, specific locations, phone call attempts, and system breakdowns. Concrete past events reveal real process failures and actual user workarounds rather than idealized workflows. |

## Part 3. Requirements, INVEST, and acceptance criteria

### R-1: Configurable Grace Period

User Story: As a media lab checkout coordinator, I want the system to use the lab's configured grace period, so that late reservations are handled consistently when the policy changes.

Structured Requirement: The system shall mark a reservation as releasable when the configured grace period has elapsed after its scheduled start time, provided the student has not checked in and no active staff hold exists.

Evidence Trace: [P06], [P12], [P21]

Jordan reports a 15-minute grace period, while Priya reports 20 minutes. The system must use the configured value rather than hard-code either number.

### R-2: Check-In Protection

User Story: As a student borrower, I want my check-in to protect my reservation from automatic release, so that I do not lose my equipment reservation after arriving at the desk.

Structured Requirement: The system shall keep a checked-in reservation active and shall not mark it as releasable solely because the configured grace period has elapsed.

Evidence Trace: [P02], [P17], [P21]

Priya expects checked-in reservations to remain active, and Jordan confirms this rule.

### R-3: Staff-Recorded Temporary Hold

User Story: As a media lab checkout coordinator, I want to record a temporary hold with an expiration time and reason, so that a delayed student can retain a reservation when staff approve an extension.

Structured Requirement: The system shall allow authorized desk staff to record a temporary hold expiration time and reason and shall prevent automatic release while the recorded hold is active.

Evidence Trace: [P04], [P19], [P21]

Jordan describes extending a reservation until 2:25 PM and identifies the hold expiration time and reason as information the system should preserve.

### R-4: Waitlist Kit Readiness

User Story: As a waitlisted student, I want to be offered only kits that are ready for checkout, so that I do not travel to the desk for equipment that is still being prepared.

Structured Requirement: The system shall permit a released kit to be offered to the waitlist only when its preparation status indicates that it is ready for checkout.

Evidence Trace: [P09], [P17], [P19], [P21]

Assumption: The system receives a kit-readiness status, but the interview does not establish how technicians provide that status.

Clarifying Question: What event or technician action should mark a kit as ready for checkout?

### Four requirement slices

For each of R-1 to R-4: user story, structured requirement, and evidence trace, or `Assumption` plus a clarifying question.

### INVEST check

| Requirement | I    | N    | V    | E    | S    | T    | Named problem for any fail |
| ----------- | ---- | ---- | ---- | ---- | ---- | ---- | -------------------------- |
| R-1         | Pass | Pass | Pass | Pass | Pass | Pass | None                       |
| R-2         | Pass | Pass | Pass | Pass | Pass | Pass | None                       |
| R-3         | Pass | Pass | Pass | Pass | Pass | Pass | None                       |
| R-4         | Pass | Pass | Pass | Pass | Pass | Pass | None                       |

### Three acceptance criteria

AC-1 to AC-3 in Given-When-Then form, each traced to a different requirement.

### AC-1: Grace Period Expiration

Traces to: R-1

Given a reservation starts at 2:00 PM, the lab's configured grace period is G = 15 minutes, the student has not checked in, and no active staff hold exists,

When the system evaluates the reservation at 2:15 PM,

Then the reservation is marked as releasable.

### AC-2: Staff Hold Protection

Traces to: R-3

Given a reservation starts at 2:00 PM, the configured grace period is G = 15 minutes, the student has not checked in, and staff have recorded a hold expiring at 2:25 PM with the reason "Student delayed by class,"

When the system evaluates the reservation at 2:20 PM,

Then the reservation remains active and is not marked as releasable.

### AC-3: Kit Not Ready for Waitlist

Traces to: R-4

Given a reservation has been released, its associated kit has a preparation status of "not ready," and a student is on the waitlist,

When the system evaluates whether the kit may be offered to the waitlist,

Then the kit is not eligible to be offered to the waitlisted student.

## Part 4. Implementation-ready specification

Paste your completed `spec/spec_template.md`.

## Part 5. Tests

| Test name                           | AC ID | Requirement ID | Evidence ID |
| ----------------------------------- | ----- | -------------- | ----------- |
| test_ac1_grace_period_expiration    | AC-1  | R-1            | INT-01:P06  |
| test_ac2_staff_hold_protection      | AC-2  | R-3            | INT-01:P07  |
| test_ac3_kit_not_ready_for_waitlist | AC-3  | R-4            | INT-01:P09  |

## Part 6. AI audit and synthetic-user critique

### Audit adjudication

For every finding in `results/ambiguity_audit.md`: true positive or false positive, the paragraph IDs, and one sentence explaining the decision.
| # | Finding | Decision | Paragraph IDs | One-sentence explanation |
| - | --------------------------------- | ------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Conflicting grace periods | True Positive | P06, P12 | Jordan states the grace period is 15 minutes, while Priya reports being told it is 20 minutes, creating a direct conflict between staff policy and student-facing communication. |
| 2 | Undefined release timing | True Positive | P06, P07, P21 | Although release is permitted after the configured grace period, the evidence does not establish whether release is automatic, discretionary, or requires explicit staff action. |
| 3 | Incomplete temporary-hold rules | True Positive | P04, P19, P21 | The interview confirms that staff can record and extend temporary holds but does not define authorization, extension limits, or behavior when a hold expires. |
| 4 | Undefined check-in semantics | True Positive | P06, P17, P21 | Check-in is identified as a condition preventing release, but the interview does not define what constitutes check-in, how it is recorded, or when it becomes effective. |
| 5 | Undefined notification behavior | True Positive | P10 | Jordan requests notification before a kit goes to the waitlist without specifying the recipient, triggering event, delivery requirements, or exact timing. |
| 6 | Release versus physical readiness | True Positive | P09, P19, P21 | The interview distinguishes reservation release from equipment readiness but does not define the readiness criteria or state transition required before waitlist availability. |
| 7 | Unspecified technician workflow | True Positive | P19, P21 | Jordan explicitly acknowledges that technicians have not been consulted, leaving their preparation actions, permissions, status transitions, and confirmation workflow undefined. |
| 8 | Undefined waitlist allocation | True Positive | P08, P09, P13, P21 | Although the interview establishes that waitlisted borrowers should only see ready equipment, it does not specify allocation priority, assignment timing, or how release and readiness affect assignment. |

### Synthetic-user critique

Every claim in `synthetic/synthetic_user_output.md` that INT-01 does not establish. Quote the claim and explain why the interview does not support it.
| # | Synthetic claim (exact quote) | Relevant INT-01 paragraphs | Why the real transcript does not support it |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | “A likely student borrower wants the media lab reservation process to require as little staff contact as possible.” | P02, P04, P13, P15 | The interview describes students contacting desk staff and checking IDs at pickup, but no participant expresses a general preference for minimizing staff interaction. |
| 2 | “Students probably prefer text-message alerts over email” | P10, P13, P17 | Jordan mentions messages, phone calls, and email, while Priya wants reservation-status information; neither identifies text messages as a preferred notification channel. |
| 3 | “because they are moving between classes.” | P12, P13 | Priya describes traveling across campus and experiencing class delays, but the interview never establishes that movement between classes causes students to prefer text-message alerts. |
| 4 | “A 10-minute grace period would likely feel fair for late arrivals.” | P06, P12 | Jordan identifies a current 15-minute policy, and Priya reports being told 20 minutes; neither participant proposes or evaluates a 10-minute grace period. |
| 5 | “The strongest feature would be a QR-code self-check-in” | P02, P15, P17, P19 | The interview mentions staff checking IDs, reservation check-in, and a speculative running-late button, but contains no evidence supporting QR-code check-in or ranking it as the strongest feature. |
| 6 | “so a borrower can preserve a reservation without waiting for a desk worker.” | P02, P06, P17, P21 | The transcript establishes that check-in protects a reservation from release, but does not establish that borrowers can check in independently or that avoiding desk-worker involvement is a desired requirement. |
| 7 | “Students who lose a reservation are likely willing to accept a different brand of camera or light automatically, as long as the general equipment category is the same.” | P13 | Priya describes receiving another lighting kit after her original reservation was released, but never states that she accepts automatic substitutions, different brands, or category-based equivalence. |
| 8 | “Equipment technicians would probably prefer to receive one batch of released-reservation updates every 30 minutes instead of individual updates.” | P09, P19, P21 | Jordan explicitly says technicians have not been interviewed, so there is no evidence of their notification preferences, batching requirements, or a 30-minute interval. |

## Part 7. Traceability and ledger

Paste the completed matrix from `traceability/template.csv`. The ledger stays in `LEDGER.md` in the repository.
evidence_id,requirement_id,acceptance_criterion_id,test_name
"INT-01:P06",R-1,AC-1,test_ac1_grace_period_expiration
INT-01:P07,R-3,AC-2,test_ac2_staff_hold_protection
INT-01:P09,R-4,AC-3,test_ac3_kit_not_ready_for_waitlist

## Verification

Paste the final output of `python -m pytest -q`.

```
python -m pytest -q
....                                                                                                                                                                                             [100%]
4 passed in 0.01s
```
