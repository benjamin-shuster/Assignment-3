# Evidence log schema

Use 8 to 10 entries. IDs must begin with E, A, or Q.

- E: real evidence from the interview transcript.
- A: an assumption that is not established by the interview.
- Q: an unresolved question that must be answered before the related decision is treated as settled.

Use this table shape:

<!-- | E-1 | OBS-02 | Rider waited 18 minutes for the next bus after a missed connection. | Observed | Student | -->

| ID  | Source     | Claim                                                                                                                                               | Status     | Owner      |
| --- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- |
| E-1 | INT-01:P02 | When a student checks out a kit, the technician needs to verify its battery is charged and has all components, and validate the students ID & name. | Observed   | Technician |
| E-2 | INT-01:P06 | There is a 15 min grace period before a kit is released, but the policy is subject to change.                                                       | Stated     | Manager    |
| A-3 | INT-01:P12 | The last time the grace period was updated, it was not well communicated to the students.  | Assumption | Student |
| E-4 | INT-01:P12 | Students are routinely told by staff that the grace period is 20 minutes, creating a discrepancy with the official 15-minute policy. | Stated | Priya Shah |
| E-5 | INT-01:P09 | Released or returned physical kits require equipment technicians to verify parts, replace missing batteries, and check accessories before reassignment. | Stated | Jordan Lee |
| E-6 | INT-01:P13 | Priya waited until 3:38 for a returned kit to become available, began her setup at 3:52, and started her interview session ten minutes late. | Observed | Priya Shah |
| A-7 | INT-01:P15 | Students will reliably use a digital "running late" button every time they experience a delay rather than attempting phone calls. | Assumption | Student Borrowers |
| Q-8 | INT-01:P19 | What specific screen workflow or interface design will equipment technicians prefer for marking equipment preparation steps? | Open | Equipment Technicians |
| Q-9 | INT-01:P06 | How should the system handle and reconcile differing grace period rules (15-minute staff policy vs. 20-minute student expectation)? | Open | Media Lab Manager |

Status says how the claim is known: `Observed` for a specific past event someone described, `Stated` for a rule or fact a speaker asserted, `Assumption` for an A entry, and `Open` for a Q entry. Owner is the person or group who could confirm the claim or answer the question.

The worked row above is unrelated to the media-lab case. For this assignment, transcript sources must use the form `INT-01:Pxx`, for example `INT-01:P13`.

Do not cite `SYN-01` as real-user evidence. Synthetic-user material can generate a hypothesis, but it cannot establish actual user behavior, willingness, priorities, or requirements.

