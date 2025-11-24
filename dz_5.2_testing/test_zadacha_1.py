from zadacha_1 import matrix


def test_matrix(capfd):
    matrix()
    out, err = capfd.readouterr()

    assert out == "12345\n678910\n1112131415\n1617181920\n2122232425\n"
