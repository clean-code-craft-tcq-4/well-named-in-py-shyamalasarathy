import GetNumberFromColor

def TestColorToNumber(major_color, minor_color, expected_pair_number):
    pair_number = GetNumberFromColor.GetNumberFromColor(major_color, minor_color)
    assert (pair_number == expected_pair_number)
