import math

test_1 = 0
test_2 = 1
test_3 = 0
test_4 = 0
test_5 = 0
test_6 = 0

List_of_test = ["test_1", "test_2", "test_3", "test_4", "test_5", "test_6"]
count_tests = len(List_of_test)
total_numers = int(test_1 + test_2 + test_3 + test_4 + test_5 + test_6)
total_perc = (math.floor((total_numers / count_tests)*100))
print(round(total_perc, 1),"%")