

def mergesort(array):
    my_sorted = []
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] > array[1]:
            array.insert(0, array.pop(1))
        return array
    else:
        # divide array into subarrays and recurse
        pivot = len(array) / 2
        first_array = mergesort( array[:pivot] )
        second_array = mergesort( array[pivot:] )
        while len(first_array) > 0 and len(second_array) > 0:
            if first_array[0] > second_array[0]:
                my_sorted.append(second_array.pop(0))
            else:
                my_sorted.append(first_array.pop(0))
        while len(first_array) > 0:
            my_sorted.append(first_array.pop(0))
        while len(second_array) > 0:
            my_sorted.append(second_array.pop(0))

    return my_sorted

print mergesort([7,4,2,5,3,6,1,2,6,6,2,6,8,9,5,4,2,7,6,10,11,67,3])