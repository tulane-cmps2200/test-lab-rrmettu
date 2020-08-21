def sum_of_squares(a):
	return sum([x*x for x in a])

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
    assert sum_of_squares([0]) == 0

def test_three():
    assert sum_of_squares([1, 2, 3, 4]) == 30
    