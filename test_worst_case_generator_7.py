from IntClass import Int
import pickle
import WorstCaseGenerator as gen

with open("worst_case_7.pkl", "rb") as case:
    retrieved_data = pickle.load(case)
    for row in retrieved_data:
        list_ = [Int(x) for x in row]
        length = len(list_)
        list_1 = gen.generateListOfElements(length)
        list_2 = gen.createChangerList(list_1)
        gen.generateWorstCaseForSeven(list_2)
        list_1 = [Int(x.value) for x in list_1]
        assert list_1 == list_, f'The lists are not the same for the {length = }'
