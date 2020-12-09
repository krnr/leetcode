"""
In an alien language, surprisingly they also use english lowercase letters,
 but possibly in a different order. The order of the alphabet is some
 permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the
 alphabet, return true if and only if the given words are sorted
 lexicographicaly in this alien language.

Example 1:

Input: words = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word", "world", "row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1],
 hence the sequence is unsorted.

Example 3:

Input: words = ["apple", "app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false

Explanation: The first three characters "app" match, and the second string is shorter
 (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅',
 where '∅' is defined as the blank character which is less than any other character.
"""
from typing import *
import itertools as it
import functools as ft

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self._hash_table = dict(zip(order, range(len(order))))
        is_sorted = True

        w1, w2, *words_left = words
        while is_sorted and w1 and w2:
            is_sorted = self._compare_words(w1, w2)
            w1, w2 = w2, words_left[0] if words_left else None
        return is_sorted
    
    def _compare_words(self, w1, w2):
        for l1, l2 in it.zip_longest(w1, w2):
            if l1 and l2 and l1 == l2:
                continue
            return self._hash_table.get(l1, -1) < self._hash_table.get(l2, -1)


def smallest_memory(words: List[str], order: str):
    indexList = list(order)
    for wordIndex in range(len(words)-1):
        letterIndex = 0
        while letterIndex != len(words[wordIndex]):
            if letterIndex == len(words[wordIndex+1]):
                return False
            if words[wordIndex][letterIndex] == words[wordIndex+1][letterIndex]:
                letterIndex += 1
            else:
                if indexList.index(words[wordIndex][letterIndex]) < indexList.index(words[wordIndex+1][letterIndex]):
                    break
                else:
                    return False
        return True


def fastest(words: List[str], order: str) -> bool:
    order_idx = {c:i for i,c in enumerate(order)}
    for i in range(len(words)-1):
        min_len = min(len(words[i]), len(words[i+1]))
        for ch_idx in range(min_len):
            if words[i][ch_idx] == words[i+1][ch_idx]:
                continue
            else:
                if order_idx[words[i][ch_idx]] > order_idx[words[i+1][ch_idx]]:
                    return False
                break
        if words[i][:min_len] == words[i+1][:min_len] and len(words[i]) > len(words[i+1]):
            return False
    return True


def shortest(words: List[str], order: str) -> bool:
    m = {c: i for i, c in enumerate(order)}
    words = [[m[c] for c in w] for w in words]
    return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
