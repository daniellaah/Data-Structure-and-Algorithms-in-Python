'''Last Position of Target
Find the last position of a target number in a sorted array. Return -1 if target does not exist.
Example
Given [1, 2, 2, 4, 5, 5].
For target = 2, return 2.
For target = 5, return 5.
For target = 6, return -1.
'''
class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        # Write your code here
        if not A or not target:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            middle = start + (end - start) // 2
            if A[middle] <= target:
                start = middle
            else:
                end = middle
        if A[end] == target:
            return end
        if A[start] == target:
            return start
        return -1
