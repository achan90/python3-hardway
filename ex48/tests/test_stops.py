from ex48 import lexicon


def test_stops():
    assert lexicon.scan("the") == [("stop", "the")]
    result = lexicon.scan("the in of")
    assert result == [("stop", "the"),
                      ("stop", "in"),
                      ("stop", "of")]
