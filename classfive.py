matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix1[2][1])
print(len(matrix1))
for i in matrix1:
    for j in i:
        print(j,end =" ")
    print()
matrix2 = [[10,11,12],[13,14,15],[16,17,18]]
matrix3 = [[19,20,21],[22,23,24],[25,26,27]]
matrix4 = []
for i in range(3):
    list = []
    for j in range(3):
        print(matrix2[i][j] + matrix3[i][j])
        list.append(matrix2[i][j] + matrix3[i][j])
    matrix4.append(list)
for i in matrix4:
    for j in i:
        print(j,end=" ")
    print()