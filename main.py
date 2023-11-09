                                        
                                        #################################################
                                        ############## Calculator Project ###############
                                        #################################################


#function to add two numbers
def add(a,b):
    return a+b

#function to subtract two numbers
def subtract(a,b):
    return a-b

#function to multiply two numbers
def multiply(a,b):
    return a*b

#function to divide two numbers
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero" 


#The main function for the calculator
def main():
        
    # the welcome message
    print("##################### Welcome to the Calculator ######################")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    try:
        #user input for choice
        choice = int(input("Choose from the above options and Enter your choice: "))
        if choice < 1 or choice > 5:
            raise ValueError
    except ValueError:
        choice = int(input("Invalid choice, please try again choose from the above options: "))

    if choice == 1 :
        print("You have selected Addition")
    elif choice == 2:
        print("You have selected Subtraction")
    elif choice == 3:
        print("You have selected Multiplication")
    elif choice == 4:
        print("You have selected Division")
    elif choice == 5:
        exit_confirmation = str(input("Do you really want to exit? (y/n) : "))
        if exit_confirmation.lower() in ("y", "yes"):
            exit()
        else:
            main()
            

    while True:
        try :
            #user input for first number
            a = float(input("Enter the first Number please: "))

            #user input for second number
            b = float(input("Enter the second number please: "))
        except ValueError or TypeError or NameError :
            print("Invalid Number, please try again")
        
        try :
            if choice == 1:
                print("Result: ", add(a,b))
            elif choice == 2:
                print("Result: ", subtract(a,b))
            elif choice == 3:
                print("Result: ", multiply(a,b))
            elif choice == 4:
                print("Result: ", divide(a,b))
        except ValueError:
            print("Invalid Number, please try again")
            continue    # Continue with the loop
                    
        #ask user if they want to continue
        try_again = str(input("Do you want to continue? (y/n)"))
        if try_again.lower() in ("y", "yes"):
            main()
        else:
            exit()

if __name__ == "__main__":
    main()
