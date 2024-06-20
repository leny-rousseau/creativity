def average(values):
    return sum(values) / len(values)

def test_average():

    input1 = [1, 2, 3]
    result = average(input1)

    assert result == 2

    input2 = [1, 2, 3, 4]
    result = average(input2)

    assert result == 2.5