
def test_line_equation():
    from line_equation import y_val
    answer = y_val((1,2), (2,4), 10)
    expected = 20
    assert answer == expected

