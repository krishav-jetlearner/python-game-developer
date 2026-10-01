list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = [[10,11,12],[13,14,15],[16,17,18]]
list3 = []
for i in range(3):
    matrix = []
    for j in range(3):
        print(list2[i][j] - list1[i][j])
        matrix.append(list2[i][j] - list1[i][j])
    list3.append(matrix)
print(list3)
print(list3[0][0])
print(list3[1][1])
print(list3[2][2])