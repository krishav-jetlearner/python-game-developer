geography = {}
while True:
    print("1.Insert a value")
    print("2.Retrieve a value")
    print("3.delete a value")
    print("4.view all values")
    print("5.exit")
    num = int(input("Choose 1-5 "))
    if num == 1:
        country = input("write any country ")
        capital = input("write the capital of the country ")
        geography[country] = capital
    elif num == 2:
        retrieve = input("write the country you want to see its capital ")
        print(geography[retrieve])
    elif num == 3:
        delete = input("write the country that you want deleted ")
        del geography[delete]
    elif num == 4:
        print(geography)
    elif num == 5:
        break