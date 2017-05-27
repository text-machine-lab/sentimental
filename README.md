# Sentimental

Python port of [github.com/Wobot/Sentimental](https://github.com/Wobot/Sentimental) 
with some improvements

A simple dictionary-based sentiment analysis system with Russian language support.

## Installation
```
pip install -U git+https://github.com/text-machine-lab/sentimental.git
```
or
```
pip install -U git+ssh://git@github.com/text-machine-lab/sentimental.git
```


## Usage
```python
from sentimental import Sentimental

sent = Sentimental()

sentence = 'Today is a good day!'
result = sent.analyze(sentence)
```
The `result` is a dictionary with four fields:

```python
{'negative': 0.0, 'positive': 3.0, 'score': 3.0, 'comparative': 0.6}
```

The filed `score` reflects the overall sentiment of the input data, 
and the `comparative` field is normalized by the length of the input, 
so it can be used to compare the sentiment of different texts.
