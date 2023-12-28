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


def test_2_names():
    expected = "Hello, Jill and Jane."
    names = ["Jill", "Jane"]
    actual = greeting_kata.greet(names)
    assert actual == expected


def test_multiple_names_with_and():
    expected = "Hello, Amy, Brian, and Charlotte."
    names = ["Amy", "Brian", "Charlotte"]
    actual = greeting_kata.greet(names)
    assert actual == expected


def test_mix_of_shouting():
    expected = "Hello, Amy and Charlotte. AND HELLO BRIAN!"
    names = ["Amy", "BRIAN", "Charlotte"]
    actual = greeting_kata.greet(names)
    assert actual == expected
