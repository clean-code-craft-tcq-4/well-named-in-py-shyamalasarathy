import Main

def GetNumberFromColor(major_color, minor_color):
    try:
        major_index = Main.MAJOR_COLORS.index(major_color)
    except ValueError:
        raise Exception('Major index out of range')
    try:
        minor_index = Main.MINOR_COLORS.index(minor_color)
    except ValueError:
        raise Exception('Minor index out of range')
    return major_index * len(Main.MINOR_COLORS) + minor_index + 1
