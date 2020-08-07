Price = 25  # price, defined globally
Tokens = [1, 5, 12]  # globally defined list of possible tokens
etokens = dict(enumerate(sorted(Tokens, reverse=True)))

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
            get_change(total - Price, [], 0)
            total = 0


def get_change(remaining, change, i):
    if remaining == 0:
        print(f"OPEN{change}")
        return change

    token = etokens.get(i, 0)

    if token > remaining and remaining != 0:
        get_change(remaining, change, i + 1)

    if token <= remaining:
        get_change(remaining - token, change + [token], i)


if __name__ == "__main__":
    turnstile(A)
