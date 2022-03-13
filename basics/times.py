list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i * j)
a_set = set(list3)
count = 0
for item in a_set:
    count += 1
print(a_set)
print(count)
