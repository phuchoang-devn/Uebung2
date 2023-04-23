# Part 2.1
# Create two lists: one containing square values and the other containing even values
numbers = []
for x in range(20):
    numbers.append(x + 1)

squares = []
for x in numbers:
    squares.append(x ** 2)

evenNumbers = []
for x in numbers:
    if x % 2 == 0:
        evenNumbers.append(x)


# Part 2.2
# create a sortable list and sort it
class SortingExample:
    # function of __init__ is like constructor in java
    def __init__(self, value):
        self.value = value

    # use __lt__ to instruct, how to sort the objects of this class
    def __lt__(self, other):
        return self.value < other.value


exampleList = [SortingExample(3), SortingExample(6), SortingExample(65),
               SortingExample(44), SortingExample(29), SortingExample(22)]
# sort the list above
resultList = sorted(exampleList)

for example in resultList:
    print(example.value)
