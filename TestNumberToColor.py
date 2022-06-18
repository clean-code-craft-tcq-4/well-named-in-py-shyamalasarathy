import GetColorFromNumber

def TestNumberToColor(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = GetColorFromNumber.GetColorFromNumber(pair_number)
    assert (major_color == expected_major_color)
    assert (minor_color == expected_minor_color)
