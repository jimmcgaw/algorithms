

def selectionsort(array):
    """ 
    pretty terrible sort algorithm with quadratic best case
    loop over array values, find the largest, append largest
    to beginning of another sorted list.
    Loop invariant: second list we are constructing is always
    in sorted order.

    Best: O(n^2)
    Average: O(n^2)
    Worst: O(n^2)

    """
    my_sorted = []
    while len(array) > 1:
        largest = array[0]

        for index, item in enumerate(array):
            if index == 0:
                continue
            if item > largest:
                largest = item
        array.remove(largest) # returns None, so insert in 2nd step below
        my_sorted.insert(0, largest)
    return my_sorted

print selectionsort([7,4,2,5,3,6,1,2,6,6,2,6,8,9,5,4,2,7,6,10,11,67,3])