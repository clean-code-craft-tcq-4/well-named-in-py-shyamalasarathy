import definitions
import itertools

Pair_color = list(itertools.product(definitions.MAJOR_COLORS, definitions.MINOR_COLORS))
print(f"{'Pair number:'} {'Color:'}")
for index, value in enumerate(Pair_color, start=1):
    print(f'{index:<12} {value}')

def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'
