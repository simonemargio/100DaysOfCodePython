#  Created by Simone Margio
#  www.simonemargio.im

# Problem: create a balanced binary search tree using an array where the elements are sorted in ascending order
# Array: arr = [1, 2, 3, 4, 5, 6, 7]
# Tree:
#                   4
#             2            6
#          1     3        5   7
#
# Output:
# 4
# 2
# 1
# 3
# 6
# 5
# 7

arr = [1, 2, 3, 4, 5, 6, 7]


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid_val = len(nums) // 2
    node = TreeNode(nums[mid_val])
    node.left = sorted_array_to_bst(nums[:mid_val])
    node.right = sorted_array_to_bst(nums[mid_val + 1:])
    return node


def pre_order(node):
    if not node:
        return
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)


result = sorted_array_to_bst(arr)
pre_order(result)
