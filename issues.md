# Issues

## Issue 1: Off-by-one in range endpoint
- **Title:** `count_up_to` excludes the limit value
- **Description:** The function is expected to include the upper bound in the returned sequence.
- **Expected behavior:** `count_up_to(4)` returns `[1, 2, 3, 4]`.
- **Actual behavior:** `count_up_to(4)` returns `[1, 2, 3]`.
- **Acceptance criteria:** Returned list includes `limit` when `limit >= 1`.
- **Affected function:** `count_up_to`

## Issue 2: Wrong comparison boundary for adulthood
- **Title:** `is_adult` rejects exactly 18
- **Description:** Adulthood threshold should include age 18.
- **Expected behavior:** `is_adult(18)` is `True`.
- **Actual behavior:** `is_adult(18)` is `False`.
- **Acceptance criteria:** Function returns `True` for ages >= 18.
- **Affected function:** `is_adult`

## Issue 3: Incorrect default handling for empty name
- **Title:** `greet` does not fallback on empty string
- **Description:** Empty name input should use the default guest greeting.
- **Expected behavior:** `greet("")` returns `"Hello, Guest!"`.
- **Actual behavior:** `greet("")` returns `"Hello, !"`.
- **Acceptance criteria:** `None` and empty string both use default guest name.
- **Affected function:** `greet`

## Issue 4: String parser fails when value contains colon
- **Title:** `parse_key_value` breaks on extra colons
- **Description:** Input values may legitimately include `:` and should not crash.
- **Expected behavior:** `parse_key_value("path:/usr/local:bin")` returns `( "path", "/usr/local:bin" )`.
- **Actual behavior:** Raises `ValueError` due to unpacking too many parts.
- **Acceptance criteria:** Split only on first colon and preserve remainder in value.
- **Affected function:** `parse_key_value`

## Issue 5: Rounding bug in tax calculation
- **Title:** `price_with_tax` rounds to whole number
- **Description:** Currency result should keep cents precision.
- **Expected behavior:** `price_with_tax(10, 0.075)` returns `10.75`.
- **Actual behavior:** Returns `11`.
- **Acceptance criteria:** Round final total to two decimal places.
- **Affected function:** `price_with_tax`

## Issue 6: Input mutation bug in dedupe helper
- **Title:** `dedupe_in_place` mutates caller list
- **Description:** Helper should return deduplicated result without altering input argument.
- **Expected behavior:** Original list remains unchanged.
- **Actual behavior:** Input list is modified via `pop`.
- **Acceptance criteria:** Function leaves provided list untouched and returns deduped list.
- **Affected function:** `dedupe_in_place`

## Issue 7: Empty-input handling in average
- **Title:** `average` crashes on empty input
- **Description:** Empty list currently causes division by zero.
- **Expected behavior:** Empty input returns `0.0`.
- **Actual behavior:** Raises `ZeroDivisionError`.
- **Acceptance criteria:** Handle empty list without exception.
- **Affected function:** `average`

## Issue 8: Incorrect filtering/sorting for top scores
- **Title:** `top_scores` includes threshold and sorts ascending
- **Description:** Function should include only strictly greater scores and sort high-to-low.
- **Expected behavior:** `top_scores([50,60,70,80], 70)` returns `[80]`.
- **Actual behavior:** Returns `[70, 80]` in ascending order.
- **Acceptance criteria:** Filter using `>` and return descending sort order.
- **Affected function:** `top_scores`
