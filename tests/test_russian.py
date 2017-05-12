from sentimental import Sentimental


def test_negative():
    sent = Sentimental()

    sentence = 'Сегодня плохой день!'
    result = sent.analyze(sentence)

    assert result['score'] < 0
    assert result['positive'] == 0


def test_positive():
    sent = Sentimental()

    sentence = 'Сегодня хороший день!'
    result = sent.analyze(sentence)

    assert result['score'] > 0
    assert result['negative'] == 0


def test_neutral():
    sent = Sentimental()

    sentence = 'Ничего такого!'
    result = sent.analyze(sentence)

    assert result['score'] == 0
    assert result['negative'] == 0


def test_negation():
    sent = Sentimental()

    sentence = 'Было не плохо!'
    result = sent.analyze(sentence)

    assert result['score'] == 0
    assert result['negative'] == 0
