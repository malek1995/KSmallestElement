"""
This code implements a series of functions that compute the median of a list of elements
 with optimal number of comparisons.
The functions handle different lengths of input lists and return the median value.

Each function compares elements in the list and swaps them if necessary to place the largest elements in higher indices.
For example, compare_and_swap compares two elements and swaps them if the first is greater than the second.
swap_elements swaps two elements directly.

The functions with names like median_of_four and median_of_five apply the swapping and comparison logic to compute
the median of a list with the corresponding number of elements.

For example, median_of_five uses several swap and comparison operations to place the median element of the list
 at index 2.
It then returns the value of that element, which is the median of the list.
"""


def compare_and_swap(list, index1, index2):
    if list[index1] > list[index2]:
        swap_elements(list, index1, index2)


def swap_elements(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]


"""
The order_four_elements function reorders the elements in the list so that the specified elements are in the order
 list[0], list[1], list[2], and list[3]. The order_seven_elements function does the same for seven elements.

For example, if the input list list is [10, 20, 30, 40] and the elements to be ordered are at indices 1, 3, 2, and 0,
 then after calling order_four_elements(list, 1, 3, 2, 0), the list will become [20, 40, 30, 10].
"""


def order_four_elements(list, e1, e2, e3, e4):
    list[0], list[1], list[2], list[3] = list[e1], list[e2], list[e3], list[e4]


def order_seven_elements(list, e1, e2, e3, e4, e5, e6, e7):
    list[0], list[1], list[2], list[3], list[4], list[5], list[6] = \
        list[e1], list[e2], list[e3], list[e4], list[e5], list[e6], list[e7]


"""
Optimal number of comparisons: 
    - 2 elements -> 1 comparison
    - 3 elements -> 3 comparisons
    - 4 elements -> 4 comparisons
    - 5 elements -> 6 comparisons
    - 6 elements -> 8 comparisons
    - 7 elements -> 10 comparisons, for some lists it is even just 9 comparisons  
"""


def median_of_one(list):
    return list[0]


def median_of_two(list):
    compare_and_swap(list, 0, 1)
    return list[0]


def median_of_three(list):
    compare_and_swap(list, 0, 1)
    compare_and_swap(list, 1, 2)
    compare_and_swap(list, 0, 1)
    return list[1]


def median_of_four(list):
    compare_and_swap(list, 0, 1)  # a_0 < a_1
    compare_and_swap(list, 2, 3)  # a_2 < a_3
    if list[2] > list[0]:  # a_2, a_1 > a_0
        if list[1] > list[2]:  # a_1, a_3 > a_2 > a_0
            order_four_elements(list, 0, 2, 1, 3)
            return list[1]
        order_four_elements(list, 0, 1, 2, 3)
        return list[1]  # a_3 > a_2 > a_1 > a_0
    else:  # a_2 < a_0, a_1
        if list[0] > list[3]:  # a_1 > a_0 > a_3 > a_2
            order_four_elements(list, 2, 3, 0, 1)
            return list[1]
        order_four_elements(list, 2, 0, 1, 3)
        return list[1]  # a_3, a_1 > a_0 > a_2


def median_of_five(list):
    compare_and_swap(list, 0, 1)
    compare_and_swap(list, 2, 3)
    if list[0] > list[2]:
        swap_elements(list, 1, 3)
        swap_elements(list, 2, 0)
    swap_elements(list, 0, 4)
    compare_and_swap(list, 0, 1)
    if list[2] > list[0]:
        swap_elements(list, 1, 3)
        swap_elements(list, 0, 2)
    swap_elements(list, 1, 4)
    if list[3] > list[0]:
        swap_elements(list, 0, 2)
    else:
        swap_elements(list, 2, 3)
        swap_elements(list, 0, 3)
    return list[2]


def median_of_six(list):
    compare_and_swap(list, 0, 1)
    compare_and_swap(list, 2, 3)
    compare_and_swap(list, 4, 5)
    if list[1] > list[3]:  # a_3 > a_0 , a_1 , a_2 ==> a_3 is not the median
        swap_elements(list, 1, 3)
        swap_elements(list, 0, 2)
    swap_elements(list, 2, 4)
    swap_elements(list, 3, 5)
    if list[1] > list[3]:  # a_3 > a_0 , a_1 , a_2 ==> a_3 is not the median
        swap_elements(list, 1, 3)
        swap_elements(list, 0, 2)
    swap_elements(list, 3, 4)
    compare_and_swap(list, 2, 3)
    if list[1] > list[3]:  # a_3 > a_0 , a_1 , a_2 ==> a_3 is not the median
        swap_elements(list, 1, 3)  # a_0 < a_1 , a_3 , a_4 , a_5 ==> a_0 is not the median
        swap_elements(list, 0, 2)
    compare_and_swap(list, 1, 2)
    return list[2]


def median_of_seven(list):  # Taken from the art of computer programming
    compare_and_swap(list, 0, 1)
    compare_and_swap(list, 2, 3)
    compare_and_swap(list, 4, 5)
    if list[1] > list[3]:
        swap_elements(list, 1, 3)
        swap_elements(list, 0, 2)
    if list[1] > list[5]:
        if list[2] > list[6]:
            if list[2] > list[5]:
                if list[0] > list[6]:
                    if list[0] > list[2]:
                        order_seven_elements(list, 4, 5, 6, 2, 0, 1, 3)
                        return list[3]
                    compare_and_swap(list, 0, 5)
                    order_seven_elements(list, 0, 4, 6, 5, 2, 3, 1)
                    return list[3]
                if list[1] > list[6]:
                    compare_and_swap(list, 5, 6)
                    order_seven_elements(list, 0, 4, 5, 6, 1, 2, 3)
                    return list[3]
                order_seven_elements(list, 0, 4, 5, 1, 6, 2, 3)
                return list[3]
            if list[0] > list[5]:
                order_seven_elements(list, 6, 4, 2, 5, 0, 1, 3)
                return list[3]
            if list[0] > list[4]:
                compare_and_swap(list, 0, 2)
                order_seven_elements(list, 6, 4, 0, 2, 5, 1, 3)
                return list[3]
            compare_and_swap(list, 2, 4)
            order_seven_elements(list, 0, 6, 2, 4, 5, 1, 3)
            return list[3]
        if list[5] > list[6]:
            if list[0] > list[5]:
                order_seven_elements(list, 4, 2, 6, 5, 0, 1, 3)
                return list[3]
            if list[0] > list[4]:
                if list[0] > list[6]:
                    swap_elements(list, 0, 6)
                order_seven_elements(list, 4, 0, 2, 6, 5, 1, 3)
                return list[3]
            compare_and_swap(list, 4, 6)
            order_seven_elements(list, 0, 4, 2, 6, 5, 1, 3)
            return list[3]
        if list[0] > list[2]:
            if list[0] > list[6]:
                order_seven_elements(list, 4, 5, 2, 6, 0, 1, 3)
                return list[3]
            compare_and_swap(list, 0, 5)
            order_seven_elements(list, 4, 0, 2, 5, 6, 1, 3)
            return list[3]
        if list[1] > list[2]:
            compare_and_swap(list, 2, 5)
            order_seven_elements(list, 4, 2, 0, 5, 6, 1, 3)
            return list[3]
        order_seven_elements(list, 4, 5, 0, 1, 2, 6, 3)
        return list[3]
    if list[2] > list[4]:
        swap_elements(list, 2, 4)
        swap_elements(list, 3, 5)
    if list[1] > list[6]:
        if list[1] > list[4]:
            if list[0] > list[4]:
                compare_and_swap(list, 0, 6)
                order_seven_elements(list, 0, 2, 4, 6, 1, 3, 5)
                return list[3]
            compare_and_swap(list, 4, 6)
            order_seven_elements(list, 2, 4, 0, 6, 1, 3, 5)
            return list[3]
        compare_and_swap(list, 1, 2)
        order_seven_elements(list, 1, 6, 0, 2, 3, 4, 5)
        return list[3]
    if list[4] > list[6]:
        if list[3] > list[6]:
            compare_and_swap(list, 2, 6)
            order_seven_elements(list, 0, 2, 1, 6, 3, 4, 5)
            return list[3]
        return list[3]
    if list[3] > list[4]:
        compare_and_swap(list, 1, 4)
        order_seven_elements(list, 2, 0, 1, 4, 3, 6, 5)
        return list[3]
    return list[3]


functions = {1: median_of_one, 2: median_of_two, 3: median_of_three, 4: median_of_four, 5: median_of_five,
             6: median_of_six, 7: median_of_seven}
