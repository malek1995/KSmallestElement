"""
This code implements the QuickSelect algorithm, a selection algorithm that finds the kth-smallest element
 in an unordered list. QuickSelect uses the same overall approach as QuickSort, but it only recurse into one partition
 of the list and returns the pivot element when the pivot's index is equal to the target index.
"""


import random


"""
The function partition takes a list and an index, and moves the element at the index to the end of the list. 
It then uses this element as the pivot to partition the list into two parts: elements smaller than the pivot, 
 and elements greater than the pivot. 
The pivot is then placed in the correct position in the list and its index is returned.
"""


def partition(list, index):
    list[-1], list[index] = list[index], list[-1]
    pivot = list[-1]
    i = 0
    for j in range(len(list) - 1):
        if compare_partition(list[j], pivot):   # True if list[j] < pivot
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[-1] = list[-1], list[i]
    return i


"""
The quickselect function takes a list and an index as input and uses the partition function to find the element 
 at the target index. If the pivot's index is equal to the target index, the pivot is returned. 
If the target index is less than the pivot's index, the function is recursively called on the first partition. 
If the target index is greater, the function is recursively called on the second partition with 
 the target index adjusted accordingly.
"""


def quickselect(list, index):
    if len(list) == 1:
        return list[0]
    pivot = random.randint(0, len(list) - 1)
    index_of_pivot = partition(list, pivot)
    if index_of_pivot == index:
        return list[index_of_pivot]
    if index < index_of_pivot:
        return quickselect(list[:index_of_pivot], index)
    else:
        return quickselect(list[index_of_pivot:], index - index_of_pivot)


"""
The compare_partition function compares two elements, and returns True if the first element is smaller than the second.
"""


def compare_partition(e1, e2):
    if e1 < e2:
        return True
    return False



