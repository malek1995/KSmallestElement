from KSmallest import kthSmallest
from IntClass import Int
import pickle
import time

print("length, comparisons, time")
with open("worst_case_3.pkl", "rb") as case3:
    retrieved_data = pickle.load(case3)
    for row in retrieved_data:
        list_ = [Int(x) for x in row]
        start = time.time()
        kSmallestElement = kthSmallest(list_, 0, len(list_) - 1, 1, 3)
        end = time.time()
        assert kSmallestElement == 0, "The 1 smallest element is wrong"
        execution_time = (end - start)
        print(f'{len(list_)}, {Int.count}, {"{:.4f}".format(execution_time)}')
        Int.resetCount()


