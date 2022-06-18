import TestColorToNumber
import TestNumberToColor

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

if __name__ == '__main__':
    TestNumberToColor.TestNumberToColor(4, 'White', 'Brown')
    TestNumberToColor.TestNumberToColor(5, 'White', 'Slate')
    TestColorToNumber.TestColorToNumber('Black', 'Orange', 12)
    TestColorToNumber.TestColorToNumber('Violet', 'Slate', 25)
    TestColorToNumber.TestColorToNumber('Red', 'Orange', 7)
    print('Done :)')
