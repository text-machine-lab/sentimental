from sentimental import Sentimental


def test_negative():
    sent = Sentimental()

    sentence = 'Today is a bad day!'
    result = sent.analyze(sentence)

    assert result['score'] < 0
    assert result['positive'] == 0


def test_positive():
    sent = Sentimental()

    sentence = 'Today is a good day!'
    result = sent.analyze(sentence)

    assert result['score'] > 0
    assert result['negative'] == 0


def test_neutral():
    sent = Sentimental()

    sentence = 'Nothing special!'
    result = sent.analyze(sentence)

    assert result['score'] == 0
    assert result['negative'] == 0


def test_negation():
    sent = Sentimental()

    sentence = 'It was not bad!'
    result = sent.analyze(sentence)

    assert result['score'] == 0
    assert result['negative'] == 0
