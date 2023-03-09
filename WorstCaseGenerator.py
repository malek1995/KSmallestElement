class Element:
    def __init__(self):
        self.value = None

    def __repr__(self):
        return str(id(self)) if self.value is None else str(self.value)


def generateListOfElements(list_length):
    return [Element() for i in range(list_length)]


def createChangerList(elements_list):
    return [elements_list[i] for i in range(len(elements_list))]


def calculateMedianPos(length, chunk_size):
    blocks_size = length // chunk_size if length % chunk_size == 0 else (length // chunk_size) + 1
    med_of_med_pos = blocks_size // 2
    median_pos = (med_of_med_pos * chunk_size) + (chunk_size // 2)
    return median_pos


def generateWorstCaseForThree(list):
    length = len(list)
    if length == 1:
        list[0].value = 0
        return list

    median_pos = calculateMedianPos(length, 3)

    # For the case that we just 4 elements
    if median_pos == length:
        list[-1].value = length - 1
        return generateWorstCaseForThree(list[:length - 1])

    smaller_elements_pos = []
    n = length - 1
    value = n

    # Handle last chunk if it includes one element
    if length % 3 == 1:
        list[-1].value = value
        value -= 1
        n -= 1

    while n >= median_pos:
        if n % 3 == 0:
            smaller_elements_pos.append(n)
        else:
            list[n].value = value
            value -= 1
        n -= 1
    smaller_elements_pos.reverse()
    list = list[:median_pos] + [list[i] for i in smaller_elements_pos]
    return generateWorstCaseForThree(list)


def generateWorstCaseForFive(list):
    length = len(list)
    if length == 1:
        list[0].value = 0
        return list

    median_pos = calculateMedianPos(length, 5)

    # For the case that we just have 6 or 7 elements
    if median_pos >= length:
        list[-1].value = length - 1
        return generateWorstCaseForFive(list[:length - 1])

    smaller_elements_pos = []
    n = length - 1
    value = n

    rest_elements = length % 5
    # Handle last chunk if it includes less than 3 elements
    if rest_elements != 0:
        if rest_elements == 1 or rest_elements == 2:
            list[-1].value = value
        else:
            list[-1].value = value
            value -= 1
            list[-2].value = value
            n -= 1
        value -= 1
        n -= 1

    # Handle the rest elements
    while n >= median_pos:
        if n % 5 == 0 or (n - 1) % 5 == 0:
            smaller_elements_pos.append(n)
        else:
            list[n].value = value
            value -= 1
        n -= 1
    smaller_elements_pos.reverse()
    list = list[:median_pos] + [list[i] for i in smaller_elements_pos]

    return generateWorstCaseForFive(list)


def generateWorstCaseForSeven(list):
    length = len(list)
    if length == 1:
        list[0].value = 0
        return list

    median_pos = calculateMedianPos(length, 7)

    # For the case that we just have 8 or 9 or 10 elements
    if median_pos >= length:
        list[-1].value = length - 1
        return generateWorstCaseForSeven(list[:length - 1])

    smaller_elements_pos = []
    n = length - 1
    value = n

    rest_elements = length % 7
    # Handle last chunk if it includes less than 4 elements
    if rest_elements != 0:
        if rest_elements == 1 or rest_elements == 2:
            list[-1].value = value
        elif rest_elements == 3 or rest_elements == 4:
            list[-1].value = value
            value -= 1
            list[-2].value = value
            n -= 1
        else:
            list[-1].value = value
            value -= 1
            list[-2].value = value
            value -= 1
            list[-3].value = value
            n -= 2
        n -= 1
        value -= 1

    # Handle the rest elements
    while n >= median_pos:
        if (n % 7 == 0) or ((n - 1) % 7 == 0) or ((n-2) % 7 == 0):
            smaller_elements_pos.append(n)
        else:
            list[n].value = value
            value -= 1
        n -= 1
    smaller_elements_pos.reverse()
    list = list[:median_pos] + [list[i] for i in smaller_elements_pos]

    return generateWorstCaseForSeven(list)


if __name__ == '__main__':
    list_1 = generateListOfElements(27)
    list_2 = createChangerList(list_1)

    generateWorstCaseForSeven(list_2)
    print(list_1)
