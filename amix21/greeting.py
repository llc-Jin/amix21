"""Build friendly greeting messages."""


def greeting(name: str) -> str:
    """Return a friendly greeting for ``name``.

    Args:
        name: The person to greet. Surrounding whitespace is ignored.

    Returns:
        A greeting string such as ``"Hello, World!"``.

    Raises:
        ValueError: If ``name`` is empty or only whitespace.
    """
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}!"
