from zadacha_2 import my_range


def test_my_range():
    result = my_range(5, 0)
    assert result == [0, 1, 2, 3, 4, 5]
