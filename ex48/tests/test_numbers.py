from ex48 import lexicon


def test_numbers():
    assert lexicon.scan("1234") == [("number", 1234)]
    result = lexicon.scan("3 91234")
    assert result == [("number", 3),
                      ("number", 91234)]
