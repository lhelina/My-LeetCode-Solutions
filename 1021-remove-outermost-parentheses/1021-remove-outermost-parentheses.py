
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        output = []
        output1 = []

        for i in s:
            if i == "(":
                if len(output) != 0:
                    output1.append(i)
                output.append(i)

            elif i == ")" and len(output) != 1:
                output.pop()
                output1.append(i)
            elif i == ")" and len(output) == 1:
                output.pop()

            else:
                return ""

        return "".join(output1)




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna