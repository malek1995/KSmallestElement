import itertools
import unittest
from Abschlussarbeit import median_functions
from Abschlussarbeit.IntClass import Int


def makeList(list_length):
    return [Int(x) for x in range(1, list_length+1)]


class TestMedianFunctions(unittest.TestCase):

    def testMedianOfThreeOnAllPermutations_numberOfComparisonsAndMedian(self):
        list_ = makeList(3)
        perm = list(map(list, itertools.permutations(list_)))
        for subList in perm:
            median = median_functions.functions[len(subList)](subList)
            self.assertEqual(median, 2, "The median of 3 elements is wrong")
            self.assertEqual(Int.count, 3, "The number of comparisons of 3 elements is wrong")
            Int.resetCount()


    def testMedianOfThreeOnAllPermutations_smallerAndGreaterElements(self):
        list_ = makeList(3)
        perm = list(map(list, itertools.permutations(list_)))
        for subList in perm:
            median_functions.functions[len(subList)](subList)
            self.assertEqual(subList[0], 1, "Smaller elements of 3 are wrong")
            self.assertEqual(subList[2], 3, "Greater elements of 3 are wrong")


    def testMedianOfFourOnAllPermutations_numberOfComparisonsAndMedian(self):
        list_ = makeList(4)
        perm = list(map(list, itertools.permutations(list_)))
        for subList in perm:
            median = median_functions.functions[len(subList)](subList)
            self.assertEqual(median, 2, "The median of 4 elements is wrong")
            self.assertEqual(Int.count, 4, "The number of comparisons of 4 elements is wrong")
            Int.resetCount()


    def testMedianOfFourOnAllPermutations_smallerAndGreaterElements(self):
        list_ = makeList(4)
        perm = list(map(list, itertools.permutations(list_)))
        for subList in perm:
            median = median_functions.functions[len(subList)](subList)
            self.assertEqual(subList[0], 1, "Smaller elements of 4 are wrong")
            for greater in subList[2:]:
                self.assertGreater(greater, median, "greater elements of 4 are wrong")
            Int.resetCount()


    def testMedianOfFiveOnAllPermutations_numberOfComparisonsAndMedian(self):
        list_ = makeList(5)
        perm = list(map(list, itertools.permutations(list_)))
        for subList in perm:
            median = median_functions.functions[len(subList)](subList)
            self.assertEqual(median, 3, "The median of 5 elements is wrong")
            self.assertEqual(Int.count, 6, "The number of comparisons of 5 elements is wrong")
            Int.resetCount()


    def testMedianOfFiveOnAllPermutations_smallerAndGreaterElements(self):
        list_ = makeList(5)
        perm = list(map(list, itertools.permutations(list_)))
        for subList in perm:
            median = median_functions.functions[len(subList)](subList)
            for smaller in subList[:1]:
                self.assertGreater(median, smaller, "Smaller elements of 5 are wrong")
            for greater in subList[3:]:
                self.assertGreater(greater, median, "greater elements of 5 are wrong")
            Int.resetCount()


    def testMedianOfSixOnAllPermutations_numberOfComparisonsAndMedian(self):
        list_ = makeList(6)
        perm = list(map(list, itertools.permutations(list_)))
        for subList in perm:
            median = median_functions.functions[len(subList)](subList)
            self.assertEqual(median, 3, "The median of 6 elements is wrong")
            self.assertEqual(Int.count, 8, "The number of comparisons of 6 elements is wrong")
            Int.resetCount()


    def testMedianOfSixOnAllPermutations_smallerAndGreaterElements(self):
        list_ = makeList(6)
        perm = list(map(list, itertools.permutations(list_)))
        for subList in perm:
            median = median_functions.functions[len(subList)](subList)
            for smaller in subList[:1]:
                self.assertGreater(median, smaller, "Smaller elements of 6 are wrong")
            for greater in subList[3:]:
                self.assertGreater(greater, median, "greater elements of 6 are wrong")
            Int.resetCount()


    def testMedianOfSevenOnAllPermutations_numberOfComparisonsAndMedian(self):
        list_ = makeList(7)
        perm = list(map(list, itertools.permutations(list_)))
        for subList in perm:
            median = median_functions.functions[len(subList)](subList)
            self.assertEqual(median, 4, "The median of 7 elements is wrong")
            self.assertGreaterEqual(10, Int.count, "The number of comparisons of 7 elements is wrong")
            Int.resetCount()


    def testMedianOfSevenOnAllPermutations_smallerAndGreaterElements(self):
        list_ = makeList(7)
        perm = list(map(list, itertools.permutations(list_)))
        for subList in perm:
            median = median_functions.functions[len(subList)](subList)
            for smaller in subList[:2]:
                self.assertGreater(median, smaller, "Smaller elements of 7 are wrong")
            for greater in subList[4:]:
                self.assertGreater(greater, median, "greater elements of 7 are wrong")
            Int.resetCount()


if __name__ == '__main__':
    unittest.main()
