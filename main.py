import testing

if __name__ == '__main__':
    testing.test_number_to_pair(4, 'White', 'Brown')
    testing.test_number_to_pair(5, 'White', 'Slate')
    testing.test_pair_to_number('Black', 'Orange', 12)
    testing.test_pair_to_number('Violet', 'Slate', 25)
    testing.test_pair_to_number('Red', 'Orange', 7)
    print('Done :)')
