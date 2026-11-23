def farewell(name):
    """Return a goodbye message for the person named; an empty name is a stranger."""
    if not name:
        name = "stranger"
    return f"Goodbye, {name}!"
