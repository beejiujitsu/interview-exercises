import re


class Solution:
    def reverseWords(self, s: str) -> str:

        def inner(total: str, left: str):
            if not left and total:
                return total

            match = re.match(r"\S+|\s+", left)

            if match:
                inner(
                    total + match.group(0)[::-1],
                    left[match.span()[1]:]
                )

        return inner("", s)


if __name__ == "__main__":
    solution = Solution()

    print(solution.reverseWords("Let's take LeetCode contest"))