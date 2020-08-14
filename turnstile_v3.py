Price = 25  # price, defined globally
Tokens = [1, 5, 12]  # globally defined list of possible tokens
rTokens = sorted(Tokens, reverse=True)

A = [12, 12, 12, 12, 12, 1, 12, 5, 5, 5]
#    |      |  |    |  |     |
#    +=OPEN=+  +=O=+   +=OPEN+

# Example Output:
# OPEN[5,5,1]
# OPEN[]
# OPEN[1,1]

# everytime given entry to the system, print OPEN and change needed

from typing import List


def turnstile(given_tokens: List[int], total: int = 0):
    if not given_tokens:
        return
    new_total: int = total + given_tokens[0]
    if new_total >= Price:
        get_change(new_total - Price, [], rTokens)
        return turnstile(given_tokens[1:], 0)
    else:
        return turnstile(given_tokens[1:], new_total)


def get_change(remaining: int, change: List[int], tokens: List[int]):
    if remaining == 0:
        print(f"OPEN{change}")
        return
    if not tokens:
        return get_change(remaining, change, rTokens)

    token = tokens[0]

    if token > remaining and remaining != 0:
        if len(tokens) == 1:
            return get_change(remaining, change, rTokens)
        else:
            return get_change(remaining, change, tokens[1:])

    if token <= remaining:
        return get_change(remaining - token, change + [token], tokens[1:])


if __name__ == "__main__":
    turnstile(A)