from zadacha_1 import matrix


def test_matrix(capfd):
    matrix()
    out, err = capfd.readouterr()

    assert (
        out == "1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25\n"
    )
