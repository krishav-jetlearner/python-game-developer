tuple1 = ("Krishav","11","Netherlands")
tuple2 = (10,11,12,13,14,15,16)
for i in tuple1:
    print(i)
f,f1,f2 = tuple1
print(f)
print(f1)
print(f2)
print(tuple2[2:6])
tuple3 = ((1,2,3),(4,5,6),[7,8])
print(tuple3[1][1])
tuple3[2][1] = 80
print(tuple3)
tuple3 = ((9),(0),[10])
print(tuple3)