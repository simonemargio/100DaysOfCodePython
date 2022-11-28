#  Created by Simone Margio
#  www.simonemargio.im

# Problem: extend nested list by adding the sublist
# Sublist to add: ["h", "i", "j"]
# Input: input_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n", "o", "p", "q"]
# Output: ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n', 'o', 'p', 'q']


input_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n", "o", "p", "q"]
sub_list = ["h", "i", "j"]

# input_list[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# input_list[2][1] = ['d', 'e', ['f', 'g'], 'k']
# input_list[2][1][2] = ['f', 'g']
input_list[2][1][2].extend(sub_list)
print(input_list)
