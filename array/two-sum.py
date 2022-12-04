"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    return [1]

testCases = (
  ([2,7,11,15], 9),
  ([3,2,4], 6),
  ([3,3], 6)
)

s = Solution()
for x in testCases:
  print("nums= ",x[0], " target= ", x[1])