import Main

def GetColorFromNumber(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(Main.MINOR_COLORS)
    if major_index >= len(Main.MAJOR_COLORS):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(Main.MINOR_COLORS)
    if minor_index >= len(Main.MINOR_COLORS):
        raise Exception('Minor index out of range')
    return Main.MAJOR_COLORS[major_index], Main.MINOR_COLORS[minor_index]
