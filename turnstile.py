Price = 25  # price, defined globally
Tokens = [1, 5, 12]  # globally defined list of possible tokens

A = [12, 12, 12, 12, 12, 1, 12, 5, 5, 5]
#    |      |  |    |  |     |
#    +=OPEN=+  +=O=+   +=OPEN+

# Example Output:
# OPEN[5,5,1]
# OPEN[]
# OPEN[1,1]

# everytime given entry to the system, print OPEN and change needed


def turnstile(given_tokens):  # OPEN[5, 1]
    # given_tokens = [12,12,12,12,12,1,12,5,5,5]
    total = 0
    for token in given_tokens:
        total = total + token
        if total == Price:
            print(f"OPEN[]")
            total = 0
        elif total > Price:
            change_needed = total - Price  # 5
            change = get_change(change_needed)
            print(f"OPEN{change}")
            total = 0


# 10 => [5, 5]
def get_change(change_needed: int):
    change = []  # [5]
    seen = {}
    for token in Tokens:
        remaining = change_needed - token
        if remaining in seen:
            change.extend((seen[remaining], token))
        seen[token] += 1
    return change


if __name__ == "__main__":
    turnstile(A)
