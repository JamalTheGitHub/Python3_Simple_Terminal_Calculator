# To run this code, type "python3 simple_terminal_calculator.py

while True: #True is to establish that it is Correct and thus perform the actions.
  print("Hello! What would you like to do?")
  print("=================================")
  print(" ")
  print("Type 'Addition' to add")
  print("Type 'Subtraction' to subtract")
  print("Type 'Multiplication' to multiply")
  print("Type 'Division' to divide")
  print(" ")
  print("=================================")
  print("To exit, type 'quit'")
  print("")
  user_input = input() #this function turns whatever the user inputs as string

  if user_input == "quit":
    print("Thank you for using ME!")
    print("")
    print("")
    break

  elif user_input == "Addition":
    print("")
    print("")
    print("Give Me a first number")
    first_number = float(input()) #use float(input()) to turn the user inputs as floating numbers which has decimals.
    print("Give Me a second number")
    second_number = float(input())
    print("The equation is, " + str(first_number) + " + " + str(second_number)) #because floating numbers are floats, in order to print you need to convert them into strings.
    result = first_number + second_number
    print("###############################")
    print("The answer is :" + str(result))
    print("###############################")
    print("")
    print("")


  elif user_input == "Subtraction":
    print("")
    print("")
    print("Give Me a first number")
    first_number = float(input())
    print("Give Me a second number")
    second_number = float(input())
    print("The equation is, " + str(first_number) + " - " + str(second_number))
    result = first_number - second_number
    print("###############################")
    print("The answer is :" + str(result))
    print("###############################")
    print("")
    print("")

  elif user_input == "Multiplication":
    print("")
    print("")
    print("Give Me a first number")
    first_number = float(input())
    print("Give Me a second number")
    second_number = float(input())
    print("The equation is, " + str(first_number) + " x " + str(second_number))
    result = first_number * second_number
    print("###############################")
    print("The answer is :" + str(result))
    print("###############################")
    print("")
    print("")

  elif user_input == "Division":
    print("")
    print("")
    print("Give Me a first number")
    first_number = float(input())
    print("Give Me a second number")
    second_number = float(input())
    print("The equation is, " + str(first_number) + " / " + str(second_number))
    result = first_number / second_number
    print("###############################")
    print("The answer is :" + str(result))
    print("###############################")
    print("")
    print("")

  else: #if none of the input corresponds to the 'options' available, it will tell the user that the input is unknown
    print("'" + user_input + "'" + " is an unknown input! Try Again!")
    print("")
    print("")