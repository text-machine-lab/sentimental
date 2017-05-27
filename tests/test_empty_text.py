from sentimental import Sentimental


def test_empty_string():
    sent = Sentimental()

    sentence = ''
    result = sent.analyze(sentence)

    assert result['score'] == 0
    assert result['positive'] == 0
    assert result['negative'] == 0
    assert result['comparative'] == 0
