import re
import os
import sys
import csv
from collections import defaultdict

class Sentimental(object):
    def __init__(self, word_list=None, negation=None):
        self.word_list = {}
        self.negations = set()

        for wl_filename in self.__to_arg_list(word_list):
            self.load_word_list(wl_filename)
        for negations_filename in self.__to_arg_list(negation):
            self.load_neagations(negations_filename)

        self.__negation_skip = set(['a', 'an', 'so', 'too'])

    def __to_arg_list(self, obj):
        if obj is not None:
            if not isinstance(obj, list):
                obj = [obj]
        else:
            obj = []
        return obj

    def __is_prefixed_by_negation(self, token_idx, tokens):
#         True if i != 0 and tokens[i - 1] in self.negations else False
        prev_idx = token_idx - 1
        if tokens[prev_idx] in self.__negation_skip:
            prev_idx -= 1

        is_prefixed = False
        if token_idx > 0 and  prev_idx >= 0 and tokens[prev_idx] in self.negations:
            is_prefixed = True

        return is_prefixed

    def load_neagations(self, filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            negations = set([row['token'] for row in reader])
        self.negations |= negations


    def load_word_list(self, filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            word_list = {row['word']:float(row['score']) for row in reader}
        self.word_list.update(word_list)

    def analyze(self, sentence):
        sentence_clean = re.sub(r'[^\w ]', ' ', sentence.lower())
        tokens = sentence_clean.split()

        scores = defaultdict(float)
        words = defaultdict(list)

        for i, token in enumerate(tokens):
            is_prefixed_by_negation = self.__is_prefixed_by_negation(i, tokens)
            if token in self.word_list and not is_prefixed_by_negation:
                score = self.word_list[token]

                type = 'negative' if score < 0 else 'positive'
                scores[type] += score
                words[type].append(token)

        result = {
            'score': scores['positive'] + scores['negative'],
            'positive': scores['positive'],
            'negative': scores['negative'],
            'comparative': (scores['positive'] + scores['negative']) / len(tokens),
        }

        return result


def main():
    sent = Sentimental(word_list=['./word_list/afinn.csv', './word_list/russian.csv'], negation='./word_list/negations.csv')

    sentences = [
        'Today is a very good day!',
        'Today is not a bad day!',
        'Today is a bad day!',
        'Сегодня хороший день!',
        'Сегодня не плохой день!',
        'Сегодня плохой день!',
        'во весь западный демократический страна в тот число в сша запрещать реклама табачный и водочный изделие',
    ]

    for s in sentences:
        result = sent.analyze(s)
        print(s, result)


if __name__ == '__main__':
    main()
