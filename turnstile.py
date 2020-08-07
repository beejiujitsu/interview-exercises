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


def turnstile(given_tokens):
    total = 0
    for token in given_tokens:
        total = total + token
        if total >= Price:
            change = get_change(total - Price)
            print(f"OPEN{change}")
            total = 0


def get_change(change_needed: int):
    change = []
    remaining = change_needed
    while remaining != 0:
        for token in sorted(Tokens, reverse=True):
            if token <= remaining:
                change.append(token)
                break
        remaining = change_needed - sum(change)
    return change


if __name__ == "__main__":
    turnstile(A)
