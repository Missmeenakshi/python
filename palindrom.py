
while True:
    print("Do you want some calculation???")
    print("1. check a num is palindrom")
    print("2. add two numbers")
    num = int(input("Enter your choice. "))
    if num == 1:
        num = int(input("enter a number = "))
        b = 0
        temp = num
        while num > 0:
            a = num % 10
            b = b * 10 + a
            num = num // 10
        print(b)
        print(temp)
        if b == temp:
            print("number is palindrom ", b)
        else:
            print("number is not palindrom", temp)
    
    elif num == 2:
        a = int(input("Enter your first number. "))
        b = int(input("Enter your second number. "))
        print("this is the addition of given numbers", a+b)
    else:
        break
    