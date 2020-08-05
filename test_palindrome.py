from palindrome import is_palindrome


def test_basic():
    assert is_palindrome("racecar") == True


def test_upper():
    assert is_palindrome("raceCar") == True


def test_punctuation():
    assert is_palindrome("##$racecar!@$#") == True


def test_long():
    assert is_palindrome("A man, a plan, a canal, Panama!") == True


def test_longest_single():
    assert is_palindrome("tattarrattat") == True
