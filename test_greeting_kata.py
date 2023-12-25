import greeting_kata


def test_return_hello_bob():
    expected = "Hello, Bob."
    names = ["Bob"]
    actual = greeting_kata.greet(names)
    assert actual == expected


def test_return_hello_bob_lowercase():
    expected = "Hello, bob."
    names = ["bob"]
    actual = greeting_kata.greet(names)
    assert actual == expected


def test_return_hello_my_friend():
    expected = "Hello, my friend."
    actual = greeting_kata.greet(None)
    assert actual == expected


def test_shouting():
    expected = "HELLO JERRY!"
    names = ["JERRY"]
    actual = greeting_kata.greet(names)
    assert actual == expected


