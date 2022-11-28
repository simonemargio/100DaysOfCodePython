#  Created by Simone Margio
#  www.simonemargio.im

# Problem: given a keypad that has the following layout
#
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
#
# Your secret agent Bond has already given you a pincode. However, he also said it's possible that each of the digits
# he saw could be another adjacent digit (horizontally or vertically, but not diagonally)
#
# Suppose the secret agent has given you the code: 46:
# Instead of the 4 it could also be 1, 5, or 7.
# Instead of the 6 it could also be 3, 5, or 9.
#
# Input: crack_pincode("46")
# Output: ["13","15","16","19","43","45","46","49","53","55","56","59","73","75","76","79"]


def crack_pincode(pincode):
    # Dictionary with values and its neighbors
    combination_adj = {'0': '08', '1': '124', '2': '1235', '3': '236', '4': '1457', '5': '24568', '6': '3569', '7': '478', '8': '57890', '9': '689'}

    posses = ['']

    # For each number given in input, take its adjs and enter them in the new combination,
    # in turn the new combination is analyzed to find its adjs
    for single_number in pincode:
        new_posses = []
        for code in posses:
            for nex in combination_adj[single_number]:
                new_posses.append(code + nex)
        posses = new_posses

    return sorted(posses)


pin_code = crack_pincode("46")
print(f"Output:  {pin_code}")
