from ex48 import lexicon


def test_verbs():
    assert lexicon.scan("go") == [("verb", "go")]
    result = lexicon.scan("go kill eat")
    assert result == [("verb", "go"),
                      ("verb", "kill"),
                      ("verb", "eat")]
