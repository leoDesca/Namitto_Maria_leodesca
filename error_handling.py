#assignment 2:
        #write a program to handle errors, the program should ask for two numbers using input and the divides them.
        #use an infinite loop to keep asking untill a valid input is provided.

def get_division():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            
            if num2 == 0:
                print("Error: invalid input try again.")
                continue
            
            result = num1 / num2
            
        except ValueError:
            print("Error: enter valid numbers only!")
            
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed!")
            
            
        else:
            print("Result:", result)
            print("Division completed successfully!")
            break 
            
        finally:
            print("Attempt finished" )
        
get_division()
print("Division done")