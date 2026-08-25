class Solution:
    def missingMultiple(self, nums, k):
        contains = [False] * 201

        for ele in nums:
            contains[ele] = True

        ans = k

        while contains[ans]:
            ans += k

        return ans
        