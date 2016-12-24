from ex48 import lexicon


def test_errors():
    assert lexicon.scan("ASDFADFASDF") == [("error", "asdfadfasdf")]
    result = lexicon.scan("bear 1 princess")
    assert result == [("noun", "bear"),
                      ("number", 1),
                      ("noun", "princess")]
