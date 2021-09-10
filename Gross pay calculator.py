# Elisa Turner
# September 2, 2021
# Gross pay calculator program 

# Define the main function
def main(): 

    # Display an introduction
    print("Welcome to my Gross Pay Calculator!\n")
    
    # Prompt for name
    userName = input("Please enter your name: ")
    
    # Prompt for hourly pay
    hourlyPay = float(input(f"\nHow much do you make per hour {userName}: $"))
    
    # Prompt for hours worked
    hoursWorked = float(input(f"How many hours have you worked {userName}: "))
    
    # Calculate gross pay  = hours worked * hourly pay
    grossPay = hourlyPay * hoursWorked
    
    # Display gross pay to user
    print(f"Gross Pay: \t${grossPay:,.2f}")


    
# Call or invoke the main function 
main()

