# Implementation-ready specification template

## Selected requirement

**Requirement ID:** R-4 — Waitlist Kit Readiness

**Evidence trace:** Part 1, Item 4 (Missing Stakeholder), Item 7 (Strongest Account of Past Event); INT-01:P09, P13, P17, P19, P21.

## Behavior and scope

The system shall permit a released equipment kit to be offered to the waitlist only when the kit is ready for checkout.

This specification covers determining whether a kit is eligible to be offered based on its reservation status and preparation status. A released reservation alone does not guarantee that the physical equipment is ready.

## Typed interface or function signature

```python
from typing import Literal

ReservationStatus = Literal["active", "released"]
KitReadiness = Literal["ready", "not_ready"]

def may_offer_to_waitlist(
    reservation_status: ReservationStatus,
    kit_readiness: KitReadiness
) -> bool: ...
```

## Preconditions

1. The caller must provide a valid reservation status of either `"active"` or `"released"`.
2. The caller must provide a valid kit readiness status of either `"ready"` or `"not_ready"`.
3. Both statuses must refer to the same reservation and associated equipment kit.
4. The caller must provide the current authoritative statuses when evaluating eligibility.

## Postconditions

1. The function returns `True` when the reservation status is `"released"` and the kit readiness status is `"ready"`.
2. The function returns `False` for every other valid combination of statuses.
3. The function does not modify the reservation status, kit readiness status, or waitlist records.
4. A `True` result indicates that the kit is eligible to be offered, not that an offer has actually been made.

## Invariant

For every eligibility evaluation, a kit must never be considered eligible for the waitlist unless its reservation is released and its preparation status is ready.

This rule must remain true across repeated evaluations using the current statuses.

## Edge cases

1. **Released but not ready:** If the reservation is `"released"` but the kit is `"not_ready"`, return `False` because technicians may still be preparing the equipment.
2. **Ready but reservation active:** If the kit is `"ready"` but its reservation is `"active"`, return `False` because the existing reservation must remain protected.
3. **Released and ready:** If the reservation is `"released"` and the kit is `"ready"`, return `True`.
4. **Status changes:** If either status changes after an evaluation, the caller must obtain updated statuses and evaluate eligibility again before relying on the result.
5. **Missing or invalid status:** Inputs outside the specified types violate the preconditions and must not be interpreted as evidence that a kit is available.

## Non-goal

This function does not send notifications or make offers to waitlisted students; it only determines whether a kit is eligible to be offered.

## Settled decisions

1. A released reservation does not automatically mean the equipment is ready for another student. (INT-01:P09)
2. Equipment must be ready for checkout before it can be offered to the waitlist. (INT-01:P17, P21)
3. Waitlist eligibility requires both a released reservation and a ready kit.
4. The function uses supplied statuses without defining or changing the technician preparation workflow.

## Open questions the implementation agent may not answer

1. What specific action or event should equipment technicians use to mark a kit as ready for checkout? Technicians were not interviewed, so their workflow must not be invented. (INT-01:P19, P21)
2. Which system component provides the authoritative reservation and kit readiness statuses, and how are changes handled between eligibility evaluation and an actual waitlist offer? This must be clarified before integrating the function into a complete reservation workflow.