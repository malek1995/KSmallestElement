"""
This code implements a variation of quickselect algorithm to find the kth-smallest element in an unsorted array.
The algorithm is divided into multiple functions: kthSmallest, updatePositioningDic, partition.
"""

import WorstCaseGenerator as gen
import time
from IntClass import Int
from Abschlussarbeit import median_functions

"""
The kthSmallest function takes an array, start and end indices, an integer k, and a chunk size as input and returns
 the k-th smallest element in the array. 
It first divides the array into chunks of size chunk_size and finds the median of each chunk. 
It then finds the median of the medians and uses it as the pivot to partition the array. 
It calls itself recursively on the left or right subarray based on the position of the pivot.
"""


def kthSmallest(array, start, end, k, chunk_size):
    # Number of elements in arr[start...end]
    n = end - start + 1

    # If k is smaller than number of elements in array
    if 0 < k <= n:
        # Divide arr[] in groups of size chunk_size,
        # calculate median of every group and store it in median[] array.
        # dic = {median1 : median_1's list,  ..., median_l : median_l's : list}, where l = len(arr) // chunk size
        dic = {}
        median = []
        j = 0
        while j < n // chunk_size:
            median.append(findMedian(array, start + j * chunk_size, chunk_size, dic))
            j += 1
        # For last group with less than chunk_size elements
        if j * chunk_size < n:
            median.append(findMedian(array, start + j * chunk_size, n % chunk_size, dic))
            j += 1

        # Find median of all medians using recursive call.
        # If median[] has only one element, then no need of recursive call
        if j == 1:
            med_of_med = median[0]
        else:
            index = j // 2 if j % 2 == 0 else ((j // 2) + 1)
            # TODO change j // 2 to index
            med_of_med = kthSmallest(median, 0, j - 1, index, chunk_size)

        # Partition the array[start...end] around a med_of_med element and get position of pivot element.
        pos = partition(array, start, med_of_med, median, dic)

        # If position is same as k
        if pos - start == k - 1:
            return array[pos]
        if pos - start > k - 1:  # If position is more,
            updatePositioningDic([med_of_med], True)
            # recursive for left subarray
            return kthSmallest(array, start, pos - 1, k, chunk_size)
        updatePositioningDic([med_of_med], False)
        # Else recursive for right subarray
        return kthSmallest(array, pos + 1, end, k - pos + start - 1, chunk_size)
    # If k is more than the number of elements in the array
    raise ValueError("K is greater than the length of the list")


"""
The partition function partitions the array around a pivot element by dividing the elements into two parts,
 one with elements smaller than the pivot and the other with elements greater than the pivot. 
It then updates the array in place and returns the index of the pivot element.
"""


def partition(array, start, pivot, medians, dic):
    left_part, right_part = [], []
    index_of_pivot = medians.index(pivot)

    # Handle medians that smaller than pivot in the medians list
    handle_smaller_medians(pivot, medians, index_of_pivot, dic, left_part, right_part)

    # Handle medians that greater than pivot
    handle_greater_medians(pivot, medians, index_of_pivot, dic, left_part, right_part)

    # Handle dic[pivot] and add the elements in medians to right and left
    handle_pivot_median(pivot, medians, index_of_pivot, dic, left_part, right_part)

    updatePositioningDic(left_part, False)
    updatePositioningDic(right_part, True)

    new_array = left_part + [pivot] + right_part
    for j in range(len(new_array)):
        array[start + j] = new_array[j]

    return start + len(left_part)


"""
A function to find median of arr[] from index start to start+n with optimal number of comparisons and store the median
 in dic. 
For example arr[start:start + n] = [2, 3, 5, 7, 1] -> dic[3] = [elements < 3, 3, elements > 3]
"""


def findMedian(array, start, n, dic):
    lis = array[start:start + n]
    median = median_functions.functions[n](lis)
    dic[median] = lis
    return median


def handle_smaller_medians(pivot, medians, index_of_pivot, dic, left_part, right_part):
    for medianSmallerPivot in medians[:index_of_pivot]:
        median_list = dic[medianSmallerPivot]
        index_of_median = median_list.index(medianSmallerPivot)
        # Elements in median_list[:index_of_median] are smaller than pivot since medianSmallerPivot < pivot
        left_part.extend(median_list[:index_of_median + 1])

        # It is unknown if these median_list[index_of_median+1:] are < or > than pivot
        compareElementsWithPivot(pivot, median_list[index_of_median + 1:], left_part, right_part)


def handle_greater_medians(pivot, medians, index_of_pivot, dic, left_part, right_part):
    for medianGreaterPivot in medians[index_of_pivot + 1:]:
        median_list = dic[medianGreaterPivot]
        index_of_median = median_list.index(medianGreaterPivot)
        # Elements in median_list[index_of_median + 1:] are greater than pivot since medianGreaterPivot > pivot
        right_part.extend(median_list[index_of_median:])

        # It is unknown if these median_list[:index_of_median] are < or > than pivot
        compareElementsWithPivot(pivot, median_list[:index_of_median], left_part, right_part)


def handle_pivot_median(pivot, medians, index_of_pivot, dic, left_part, right_part):
    # Add the elements in pivot list, because the pivot is also a median
    pivot_list = dic[pivot]
    pivot_index = pivot_list.index(pivot)
    left_part.extend(pivot_list[:pivot_index])
    right_part.extend(pivot_list[pivot_index + 1:])

    # Add the medians, that smaller than pivot to left and to right for medians that greater than the pivot
    # left_part.extend(medians[:index_of_pivot])
    # right_part.extend(medians[index_of_pivot + 1:])


"""
The compareElementsWithPivot function compares a list of elements with a pivot element and appends them to 
either the left_part or right_part list depending on whether the elements are smaller or greater than the pivot.
"""


def compareElementsWithPivot(pivot, elements, left_part, right_part):
    for element in elements:
        if compareElementWithPivot(pivot, element):  # element > pivot
            right_part.append(element)
            updatePositioningDic([element], True)
        else:  # element < pivot
            left_part.append(element)
            updatePositioningDic([element], False)


def compareElementWithPivot(pivot, element):
    if element > pivot:
        return True
    return False


"""
The updatePositioningDic function updates a global positioningDic which keeps
 track of the relative ordering of the elements in the array.
@param state is either true or falls.
 - True means that the elements are greater than kth-smallest element.
 - False means that the elements are smaller than kth-smallest element.
"""


def updatePositioningDic(elements, state):
    global positioningDic
    for element in elements:
        positioningDic[element] = state


positioningDic = {}

if __name__ == '__main__':
    # limit = 2e10
    # n = 105
    # i = 0
    # print("Length, Comparisons, Time")
    # while n < limit:
    #     m = n - n % 105 + i % 105
    #     list_1 = gen.generateListOfElements(m)
    #     list_2 = gen.createChangerList(list_1)
    #     gen.generateWorstCaseForSeven(list_2)
    #     start = time.time()
    #     k_element = kthSmallest(list_1.copy(), 0, m - 1, 1, 7)
    #     end = time.time()
    #     run_time = end - start
    #     print(str(m) + ", " + str(Int.count) + ", " + str(round(run_time, 5)))
    #     Int.resetCount()
    #     n *= 2
    #     i = (i + 1) % 105
    for i in range(1, 100):
        list_ = [i - x for x in range(1, i)]
        for j in range(1, i):
            k_element = kthSmallest(list_.copy(), 0, len(list_) - 1, j, 7)
            assert k_element == j, f'{k_element = }, {j = }'
