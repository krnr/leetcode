#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.
"""

import typing as t
import functools as ft

@ft.total_ordering
class Player:

    __slots__ = ('score', 'age')

    def __init__(self, score, age):
        self.score = score
        self.age = age
    def __repr__(self): return f"P{self.age}: {self.score}"
    def __eq__(self, other):
        return self.age == other.age
    def __lt__(self, other):
        if self.age == other.age:
            return self.score < other.score
        return self.age < other.age


class Solution:
    def bestTeamScore(self, scores: t.List[int], ages: t.List[int]) -> int:
        players = [Player(s, a) for s, a in zip(scores, ages)]
        players.sort()
        print("players:", players)

        amount = len(players)
        ans = [0] * amount
        for i in range(amount):
          score_i = players[i].score
          ans[i] = score_i 
          for j in range(i):
              score_j = players[j].score
              if score_i >= score_j: 
                  ans[i] = max(ans[i], score_i + ans[j])
        print('ans:    ', ans)
        return max(ans)


scores = [1,3,5,10,15]
ages = [1,2,3,4,5]
assert Solution().bestTeamScore(scores, ages) == 34

scores = [4,5,6,5]
ages = [2,1,2,1]
assert Solution().bestTeamScore(scores, ages) == 16 

scores = [1,2,3,5]
ages = [8,9,10,1]
assert Solution().bestTeamScore(scores, ages) == 6

scores = [1,2,3,4,5]
ages = [1,1,1,1,1]
assert Solution().bestTeamScore(scores, ages) == 15

scores = [319776,611683,835240,602298,430007,574,142444,858606,734364,896074]
ages = [1,1,1,1,1,1,1,1,1,1]
assert Solution().bestTeamScore(scores, ages) == 5431066

