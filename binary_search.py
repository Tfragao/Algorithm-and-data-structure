def binary_search(list, target):
    first = 0
    last = len(list) - 1   #position in the list, -1 because the list starts at 0

    while first <= last:
        midpoint = (first + last)//2  # // floor division operator in python

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,8,9,10]
result = binary_search(numbers, 12)
verify(result)

numbers = [1,2,3,4,5,6,8,9,10]
result = binary_search(numbers, 4)
verify(result)


