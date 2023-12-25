import greeting_kata


def test_return_hello_bob():
    expected = "Hello, Bob."
    actual = greeting_kata.greet("Bob")
    assert actual == expected


def test_return_hello_bob_lowercase():
    expected = "Hello, bob."
    actual = greeting_kata.greet("bob")
    assert actual == expected


def test_return_hello_my_friend():
    expected = "Hello, my friend."
    actual = greeting_kata.greet(None)
    assert actual == expected
