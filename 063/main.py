#  Created by Simone Margio
#  www.simonemargio.im

# Problem: delete the second column from a given array and insert the following new column in its place.
# Input: numpy.array([[22, 43, 60], [44, 22, 12], [52, 94, 66]])
# Input new column: newColumn = numpy.array([[0,0,0]])
# Output:
# Original array
# [[22 43 60]
#  [44 22 12]
#  [52 94 66]]
#
# Delete column 2 on axis 1
# [[22 60]
#  [44 12]
#  [52 66]]
#
# Insert column 2 on axis 1
# [[22 10 60]
#  [44 10 12]
#  [52 10 66]]
import numpy as numpy

newColumn = numpy.array([[0, 0, 0]])

print("Original array")
sampleArray = numpy.array([[22, 43, 60], [44, 22, 12], [52, 94, 66]])
print(sampleArray)

print("Delete column 2 on axis 1")
sampleArray = numpy.delete(sampleArray, 1, axis=1)
print(sampleArray)

print("Insert column 2 on axis 1")
sampleArray = numpy.insert(sampleArray, 1, newColumn, axis=1)
print(sampleArray)
