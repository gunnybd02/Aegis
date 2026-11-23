def greet(name):
    """Return a greeting for name; an empty name greets a stranger."""
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"
