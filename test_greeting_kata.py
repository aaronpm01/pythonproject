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


def test_mix_of_shouting_2():
    expected = "Hello, Amy and BRIAN. AND HELLO Charlotte!"
    names = ["Amy", "Charlotte", "BRIAN", ]
    actual = greeting_kata.greet(names)
    assert actual == expected


# This behavior has not yet been implemented.
def test_edge_case_1():
    expected = "Hello, JERRY and ."
    names = ["JERRY", ""]
    actual = greeting_kata.greet(names)
    assert actual == expected


# This behavior has not yet been implemented.
def test_edge_case_2():
    expected = "Hello, JERRY and #$^&%^."
    names = ["JERRY", "#$^&%^"]
    actual = greeting_kata.greet(names)
    assert actual == expected


def test_edge_case_3():
    expected = "Hello, my friend."
    names = []
    actual = greeting_kata.greet(names)
    assert actual == expected


def test_edge_case_4():
    expected = "Hello, my friend."
    names = [b"200"]
    actual = greeting_kata.greet(names)
    assert actual == expected


def test_edge_case_5():
    expected = "Hello, my friend."
    names = [0]
    actual = greeting_kata.greet(names)
    assert actual == expected


def test_edge_case_6():
    expected = "Hello, 😵."
    names = ["😵"]
    actual = greeting_kata.greet(names)
    assert actual == expected


def test_edge_case_7():
    expected = "Hello, Añita."
    names = ["Añita"]
    actual = greeting_kata.greet(names)
    assert actual == expected


def test_edge_case_8():
    expected = "Hello, my friend."
    names = [{"potato": "cheese"}]
    actual = greeting_kata.greet(names)
    assert actual == expected
