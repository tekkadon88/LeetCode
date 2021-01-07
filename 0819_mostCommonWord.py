"""
819. Most Common Word

URL: https://leetcode.com/problems/most-common-word/
Level: Easy
"""
from typing import List
import string
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub('[{}]'.format(string.punctuation), ' ', paragraph.lower()).split()
        word_counts = {}

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        sorted_list = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        for w, c in sorted_list:
            if w in banned:
                continue

            return w


if __name__ == '__main__':
    solution = Solution()
    paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
    paragraph = "Bob. hIt, baLl"
    banned = ["hit"]
    banned = ['bob', 'hit']
    print(solution.mostCommonWord(paragraph, banned))