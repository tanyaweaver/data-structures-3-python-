from source.dictionary import Hash


def test_create_hash():
    newHash = Hash()
    assert len(newHash.container) == 255
