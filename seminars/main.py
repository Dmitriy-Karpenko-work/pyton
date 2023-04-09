a = int(input("введите год "))

if (a%400==0):
    print("высокостный")
elif (a%4 == 0 and a%100 != 0):
    print("высокостный")
else :
    print("не высокостный")
