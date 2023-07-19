from collections import deque, defaultdict
from functools import cache
from random import shuffle
from typing import List, Optional, Dict, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self._memo: Dict[Tuple, int] = {}

    def minDistance(self, s1: str, s2: str) -> int:
        return self._minDistance(s1, len(s1) - 1, s2, len(s2) - 1)

    # 返回子串 s1[0..i] s2[0..j] 的最小删除步数
    def _minDistance(self, s1: str, i: int, s2: str, j: int) -> int:
        # 删除 s2[0..j]
        # s1""
        # s2[0..j]
        if i < 0:
            return j + 1

        # 删除 s1[0..i]
        # s1[0..i]
        # s2""
        if j < 0:
            return i + 1

        if (i, j) not in self._memo:
            if s1[i] == s2[j]:
                # s1[0..i-1][i]
                # s2[0..j-1][j]
                self._memo[(i, j)] = self._minDistance(s1, i - 1, s2, j - 1)
            else:
                # 删除 s1[i] s2[j]
                # s1[0..i-1][i]
                # s2[0..j-1][j]
                sp1 = self._minDistance(s1, i - 1, s2, j - 1) + 2
                # 删除 s2[j]
                # s1[0..i]
                # s2[0..j-1][j]
                sp2 = self._minDistance(s1, i, s2, j - 1) + 1
                # 删除 s1[i]
                # s1[0..i-1][i]
                # s2[0..j]
                sp3 = self._minDistance(s1, i - 1, s2, j) + 1
                self._memo[(i, j)] = min(sp1, sp2, sp3)

        return self._memo[(i, j)]
