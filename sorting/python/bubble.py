import time

def bubblesort(array):
    is_sorted = False
    while not is_sorted:
        swapped = False
        for index, item in enumerate(array):
            if index == len(array)-1:
                break # last item
            next_item = array[index+1]
            print index, item, next_item
            if next_item < item:
                # swap elements
                array.insert(index, array.pop(index+1))
                swapped = True

        if not swapped:
            # we didn't swap any elements, terminate loop
            is_sorted = True
            
    return array


print bubblesort([7,4,2,5,3,6,1,2,6,6,2,6,8,9,5,4,2,7,6,10,11,67,3])