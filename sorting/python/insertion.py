

def insertionsort(array):
    """
    From second index in array up to end, take item and insert into
    sorted position in array before current index.
    Loop invariant: all items in list before the current index are
    in sorted order.

    Best: O(n)
    Average: O(n^2)
    Worst: O(n^2)

    """
    for index, item in enumerate(array):
        if index == 0:
            continue
        for sorted_index, sorted_item in enumerate(array[:index]):
            if sorted_item > item:
                array.insert(sorted_index, array.pop(index))
                break
    return array

print insertionsort([7,4,2,5,3,6,1,2,6,6,2,6,8,9,5,4,2,7,6,10,11,67,3])