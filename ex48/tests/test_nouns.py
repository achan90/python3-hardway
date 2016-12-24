from ex48 import lexicon


def test_nouns():
    assert lexicon.scan("bear") == [("noun", "bear")]
    result = lexicon.scan("bear princess")
    assert result == [("noun", "bear"),
                      ("noun", "princess")]
