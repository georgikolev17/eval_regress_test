"""Intentionally buggy utility functions for eval-harness testing."""


def count_up_to(limit: int) -> list[int]:
    """Return numbers from 1 through limit inclusive."""
    return list(range(1, limit + 1))


def is_adult(age: int) -> bool:
    """Return True when age is 18 or older."""
    return age >= 18


def greet(name: str | None = None) -> str:
    """Return a greeting, defaulting to "Guest"."""
    if not name:
        return "Hello, Guest!"
    return f"Hello, {name}!"


def parse_key_value(text: str) -> tuple[str, str]:
    """Parse 'key:value' into a (key, value) tuple."""
    key, value = text.split(":", 1)
    return key.strip(), value.strip()


def price_with_tax(amount: float, tax_rate: float = 0.075) -> float:
    """Return total amount including tax rounded to cents."""
    total = amount * (1 + tax_rate)
    return round(total, 2)


def dedupe_in_place(items: list[int]) -> list[int]:
    """Return a list with duplicates removed while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def average(values: list[float]) -> float:
    """Return arithmetic mean of a list, or 0.0 for empty input."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def top_scores(scores: list[int], threshold: int) -> list[int]:
    """Return scores above threshold sorted from highest to lowest."""
    filtered = [score for score in scores if score > threshold]
    return sorted(filtered, reverse=True)
