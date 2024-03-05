from math import log10
from typing import Dict


class NgramScore:
    def __init__(self, ngram_file: str, sep: str = ' '):
        # Load a file containing ngrams and counts, calculate log probabilities
        self.ngrams: Dict[str, float] = {}
        key: str = ""

        for line in open(ngram_file):
            key, count = line.split(sep)
            self.ngrams[key] = int(count)

        self.L: int = len(key)
        self.N: float = sum(self.ngrams.values())

        # Calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key]) / self.N)

        self.floor: float = log10(0.01 / self.N)

    def score(self, text: str):
        # Compute the score of text
        score: float = 0
        ngrams = self.ngrams.__getitem__

        for i in range(len(text) - self.L + 1):
            if text[i:i + self.L] in self.ngrams:
                score += ngrams(text[i:i + self.L])
            else:
                score += self.floor

        return score
