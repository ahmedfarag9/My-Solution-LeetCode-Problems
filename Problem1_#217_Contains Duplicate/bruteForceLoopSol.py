# Problem 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Solution using Brute Force Algorithm
# Time Complexity worst case O(n^2)
# LeetCode Runtime Result is around 60 ms

from typing import List

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 15, -5, 5]


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:

        new_list = []

        for i in nums:
            if not new_list:
                new_list.append(i)
            else:
                for x in new_list:
                    if i == x:
                        return True
                new_list.append(i)
        return False


if __name__ == "__main__":
    Test = Solution()
    print(Test.containsDuplicate(test))
