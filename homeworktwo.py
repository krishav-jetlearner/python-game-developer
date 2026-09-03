test_scores = {}
while True:
    print("1.Insert a test score ")
    print("2.retrieve a test score")
    print("3.delete a test score")
    print("4.view all test scores")
    print("5.exit")
    print("6.highest marks")
    print("7. average marks")
    num = int(input("choose 1-5 "))
    if num == 1:
        subject = input("write a subject ")
        test_score = input("write the test score of that subject ")
        test_scores[subject] = test_score
    elif num == 2:
        retrieve = input("write the subject that you want to retrieve ")
        print(test_scores[retrieve])
    elif num == 3:
        delete = input("write the subject that you deleted ")
        del test_scores[delete]
    elif num == 4:
        print(test_scores)
    elif num == 5:
        break