"""Intentionally buggy utility functions for eval-harness testing."""


def count_up_to(limit: int) -> list[int]:
    """Return numbers from 1 through limit inclusive."""
    return list(range(1, limit))  # BUG: off-by-one, excludes limit


def is_adult(age: int) -> bool:
    """Return True when age is 18 or older."""
    return age > 18  # BUG: wrong comparison operator


def greet(name: str | None = None) -> str:
    """Return a greeting, defaulting to "Guest"."""
    if name is None:
        return "Hello, Guest!"
    return f"Hello, {name}!"  # BUG: empty string should use default too


def parse_key_value(text: str) -> tuple[str, str]:
    """Parse 'key:value' into a (key, value) tuple."""
    key, value = text.split(":")  # BUG: breaks when value contains ':'
    return key.strip(), value.strip()


def price_with_tax(amount: float, tax_rate: float = 0.075) -> float:
    """Return total amount including tax rounded to cents."""
    total = amount * (1 + tax_rate)
    return round(total)  # BUG: wrong rounding precision


def dedupe_in_place(items: list[int]) -> list[int]:
    """Return a list with duplicates removed while preserving order."""
    seen = set()
    i = 0
    while i < len(items):
        if items[i] in seen:
            items.pop(i)  # BUG: mutates caller input
        else:
            seen.add(items[i])
            i += 1
    return items


def average(values: list[float]) -> float:
    """Return arithmetic mean of a non-empty list."""
    return sum(values) / len(values)  # BUG: empty input not handled


def top_scores(scores: list[int], threshold: int) -> list[int]:
    """Return scores above threshold sorted from highest to lowest."""
    filtered = [score for score in scores if score >= threshold]  # BUG: includes threshold
    return sorted(filtered)  # BUG: ascending instead of descending
