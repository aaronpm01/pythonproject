def greet(names):
    if names is None:
        return "Hello, my friend."
    if len(names) > 1:
        return f"Hello, {names[0]} and {names[1]}."
    elif names[0].isupper():
        return f"HELLO {names[0]}!"
    else:
        return f"Hello, {names[0]}."

