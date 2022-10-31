#  Created by Simone Margio
#  www.simonemargio.im

# Problem: Make a Rectangle class with four parameters, an x, a y (representing the top-left corner of the rectangle),
#          a width and a height exclusively in that order
# Lastly, make a function intersecting that takes two Rectangle objects and returns True if those objects are
# intersecting (colliding), else return False.
#
# Es:
#   a = Rectangle(10, 20, 100, 20)
#   b = Rectangle(10, 40, 15, 20)
#   c = Rectangle(50, 50, 20, 30)
#   intersecting(a, b) -> True
#   intersecting(a, c) -> False
#   intersecting(b, c) -> False


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


def intersecting(a, b):
    return b.x - a.x <= a.w and b.y - a.y <= a.h


a = Rectangle(10, 20, 100, 20)
b = Rectangle(10, 40, 15, 20)
c = Rectangle(50, 50, 20, 30)

print(intersecting(a, b))
print(intersecting(a, c))
print(intersecting(b, c))
