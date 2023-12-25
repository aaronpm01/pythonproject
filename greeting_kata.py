def greet(names):
    if names is None:
        return "Hello, my friend."
    elif names[0].isupper():
        return f"HELLO {names[0]}!"
    else:
        return f"Hello, {names[0]}."

