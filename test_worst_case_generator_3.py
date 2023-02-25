from IntClass import Int
import pickle
import WorstCaseGenerator as gen

with open("worst_case_3.pkl", "rb") as case3:
    retrieved_data = pickle.load(case3)
    for row in retrieved_data:
        list_ = [Int(x) for x in row]
        length = len(list_)
        list_1 = gen.generateListOfElements(length)
        list_2 = gen.createChangerList(list_1)
        gen.generateWorstCaseForThree(list_2)
        list_1 = [Int(x.value) for x in list_1]
        assert list_1 == list_, f'The lists are not the same for the {length = }'
        