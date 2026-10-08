class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(path, remaining):
            if len(remaining) == 0:
                result.append(path)
                return

            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], 
                          remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna