import string


def greet(names):
    if names is None or len(names) == 0 or any(not isinstance(ele, str) for ele in names):
        return "Hello, my friend."
    if len(names) > 2 and any(ele.isupper() for ele in names):
        return f"Hello, {names[0]} and {names[2]}. AND HELLO {names[1]}!"
    if len(names) > 2:
        return f"Hello, {names[0]}, {names[1]}, and {names[2]}."
    if len(names) > 1:
        return f"Hello, {names[0]} and {names[1]}."
    elif names[0].isupper():
        return f"HELLO {names[0]}!"
    else:
        return f"Hello, {names[0]}."
