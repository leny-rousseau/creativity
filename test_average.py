def average(values):
    return sum(values) / len(values)

def test_average():

    input1 = [1, 1, 1]
    result = average(input1)
    assert result == 1
    print(result(1))

    input2 = [1, 2, 3]
    result = average(input2)
    assert result == 2
    print(result(2))

    input2 = [10, 100, 1000]
    result = average(input2)
    assert result == 370
    print(result(370))