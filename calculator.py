while True:
    num1 = int(input("enter your number 1= "))
    num2 = int(input("enter the number 2= "))
    print("Do you want some calculation????")
    print("1. additon ")
    print("2. subtraction")
    print("3. dividation")
    print("4. multiplication")
    choice = int(input("Enter the choice= "))
    if choice == 1:
        choice1 = num1 + num2
        print(choice1)

    elif choice == 2:
        choice2 = num1 - num2
        print(choice2)

    elif choice == 3:
        choice3 = num1 / num2
        print(choice3)
    elif choice == 4:
        choice4 = num1 * num2
        print(choice4)
 
    else:
        print("you pick wrong option!!!!, see you again.")
        break

       
    