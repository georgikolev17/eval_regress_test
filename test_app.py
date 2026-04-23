import pytest

import app


def test_count_up_to_includes_limit():
    assert app.count_up_to(4) == [1, 2, 3, 4]


def test_is_adult_accepts_18():
    assert app.is_adult(18) is True


def test_greet_empty_string_uses_default():
    assert app.greet("") == "Hello, Guest!"


def test_parse_key_value_allows_colon_in_value():
    assert app.parse_key_value("path:/usr/local:bin") == ("path", "/usr/local:bin")


def test_price_with_tax_keeps_two_decimal_places():
    assert app.price_with_tax(10.00, 0.075) == 10.75


def test_dedupe_in_place_does_not_mutate_input_list():
    original = [1, 1, 2, 3]
    snapshot = original[:]
    result = app.dedupe_in_place(original)
    assert original == snapshot
    assert result == [1, 2, 3]


def test_average_empty_input_returns_zero():
    assert app.average([]) == 0.0


def test_top_scores_excludes_threshold_and_sorts_descending():
    assert app.top_scores([50, 60, 70, 80], 70) == [80]
