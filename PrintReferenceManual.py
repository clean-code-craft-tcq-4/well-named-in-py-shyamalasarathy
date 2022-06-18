import Main
import itertools

def print_color_pair_manual():
    ListPairColor = list(itertools.product(Main.MAJOR_COLORS, Main.MINOR_COLORS))
    print(f"{'Pair number:'} {'Color:'}")
    for index, value in enumerate(ListPairColor, start=1):
        print(f'{index:<12} {value}')

print_color_pair_manual()
