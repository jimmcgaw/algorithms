

def mediansort(array):
    length = len(array)
    if length == 1:
        return array
    if length % 2 == 1:
        median_index = length/2
    else:
        # there are actually 2 median indices: length/2 AND length/2+1
        median_index = length/2 - 1
        if array[median_index] > array[median_index+1]:
            # swap values are median indices into sorted order
            array.insert(median_index, array.pop(median_index+1))
    for index, item in enumerate(array[:median_index]):
        pass
    return array

#print mediansort([7,4,2,5,3,6,1,2,6,6,2,6,8,9,5,4,2,7,6,10,11,67,3])
print mediansort([7,2,5,3,6,1])