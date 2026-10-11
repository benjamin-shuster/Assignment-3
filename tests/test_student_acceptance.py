"""Write exactly three pytest tests in this file.

TODO 1: Add one test derived from acceptance criterion AC-1.
TODO 2: Add one test derived from acceptance criterion AC-2.
TODO 3: Add one test derived from acceptance criterion AC-3.

Use only the public functions in ``reference``: reservation_disposition and
can_offer_to_waitlist. Do not edit the reference module. Call them with named
arguments, as in tests/test_reference_smoke.py.

Name each test so the acceptance criterion it checks is visible from the test
name or an adjacent comment, for example: def test_ac1_<what_it_checks>().

Put any policy value, such as the grace period, in a named constant marked as
a configured value, as in the at-risk example from the Week 5 lecture.
"""

"""Acceptance tests for AC-1, AC-2, and AC-3."""

from reference.reservation import (
    reservation_disposition,
    can_offer_to_waitlist,
)

# Configured policy values
CONFIGURED_GRACE_MINUTES = 15
CONFIGURED_STAFF_HOLD_UNTIL = 25


# AC-1 | R-1 | INT-01:P06
def test_ac1_grace_period_expiration():
    result = reservation_disposition(
        minutes_after_start=15,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=False,
        staff_hold_until=None,
    )

    assert result == "releasable"


# AC-2 | R-3 | INT-01:P07
def test_ac2_staff_hold_protection():
    result = reservation_disposition(
        minutes_after_start=20,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=False,
        staff_hold_until=CONFIGURED_STAFF_HOLD_UNTIL,
    )

    assert result != "releasable"
    assert result in ("active", "held")


# AC-3 | R-4 | INT-01:P09
def test_ac3_kit_not_ready_for_waitlist():
    result = can_offer_to_waitlist(
        disposition="releasable",
        preparation_complete=False,
    )

    assert result is False
