#Banking Stimulator
#author: Sehaj

#ask the user for basic name and contact information
name= input("FIRST NAME: ")
input("LAST NAME: ")
input("CONTACT NUMBER: ")
print("Hello "+ name +"! Welcome to the Bank of Canada.")


#define a function for when the user wants to open an account
def openaccount():
#create a while loop to return if the user gives a wrong input 
  while True:
    a = input("Would you like to book an appointment with our consultant to open your bank account? (yes/no): ")
    if a == "yes":
      print("Okay!")
      while True:
#create a try and except block within the nested while loop to avoid a value error if the user gives a wrong input
        try:
          b = int(input("Select the month (1-12): "))
          if b<1 or b>12:
            print("Please enter a valid value.")
          else:
            break
        except:
          print("Please enter a valid value.")

#nest a seperate while loop for the seperate input to avoid overlapping it with the previous input question  
      while True:
#create a try and except block within the nested while loop to avoid a value error if the user gives a wrong input
        try:
          c = int(input("Select a date (1-31): "))
          if c<1 or c>31:
            print("Please enter a valid value.")
          else:
            break
        except:
          print("Please enter a valid value.")

#add the further commands outside the nested while loops but within the the main while loop
      print("Okay! You are all set.")
      print("Our consulatant will call you within the next hour to conform the timing of your appointment and will inform you about what documents you need to bring in.")
      print("Thank you for your time. Have a good day!")
      break
    if a == "no":
      print("Thank you for your time.")
      break
    else:
      print("Please respond with yes or no.")


#define a function for when the user wants to withdraw money from their account
def moneywithd():
#create a while loop to return if the user gives a wrong input
  while True:
#create a try and except block within the while loop to avoid a value error if the user gives a wrong input
    try:
      int(input("Type in your account number: "))
      break
    except ValueError:
      print("Try again with a valid value.")

#add next commands outside the while loop 
  input("Type the security password: ")
  print("Total amount in your account: $1000")

#create another while loop to return if the user gives a wrong input
  while True:
#create a try and except block within the nested while loop to avoid a value error if the user gives a wrong input
    try:
      d = float(input("Amount of money you want to withdraw: "))
      if d>1000:
        print("You don't have enough balance for this transaction. Try Again.")
      elif d<1000:
        print("WITHDRAWN AMOUNT: $" + str(d))
        print("TOTAL BALANCE LEFT: $" + str(1000-d))
        print("Thank you for your time. Have a good day!")
        break
    except ValueError:
      print("Try again with a valid value.")


#define a function for when the user wants to deposit money in their account
def moneydep():
#create a while loop to return if the user gives a wrong input
  while True:
#create a try and except block within the while loop to avoid a value error if the user gives a wrong input
    try:
        int(input("Type in your account number: "))
        break
    except ValueError:
        print("Try again with a valid value.")

  input("Type the security password: ")
  print("Total amount in your account: $1000")

#create another while loop to return if the user gives a wrong input
  while True:
#create a try and except block within the while loop to avoid a value error if the user gives a wrong input
    try:
      e = float(input("Amount of money you want to deposit: "))
      print("DEPOSITED AMOUNT: $" + str(e))
      print("TOTAL BALANCE LEFT: $" + str(1000+e))
      print("Thank you for your time. Have a good day!")
      break
    except ValueError:
      print("Try again with a valid value.")
  

#define a function for when the user wants to transfer money from their account to another account
def transfer():
#create a while loop to return if the user gives a wrong input
  while True:
#create a try and except block within the while loop to avoid a value error if the user gives a wrong input
    try:
      int(input("Type in your account number: "))
      break
    except ValueError:
      print("Try again with a valid value.")

#create another while loop to return if the user gives a wrong input
  while True:
#create a try and except block within the while loop to avoid a value error if the user gives a wrong input
    try:
      int(input("Type in the account number you want to transfer money to: "))
      break
    except ValueError:
      print("Try again with a valid value.")

  input("Type the security password: ")
  print("Total amount in your account: $1000")

#create another while loop to return if the user gives a wrong input
  while True:
#create a try and except block within the while loop to avoid a value error if the user gives a wrong input
    try:
      f = float(input("Amount of money you want to transfer: "))
      if f>1000:
        print("You don't have enough balance for this transaction. Try Again.")
      elif f<1000:
        print("TRANSFERRED AMOUNT: $" + str(f))
        print("TOTAL BALANCE LEFT: $" + str(1000-f))
        print("Thank you for your time. Have a good day!")
        break
    except ValueError:
      print("Try again with a valid value.")


#define a function for when the user wants to apply for a mortgage
def mort():
#create a while loop to return if the user gives a wrong input
  while True:
#create a try and except block within the while loop to avoid a value error if the user gives a wrong input
    try:
      int(input("Type in your account number: "))
      break
    except ValueError:
      print("Try again with a valid value.")

#add further commands
  input("Type the security password: ")

#create another while loop to return if the user gives a wrong input
  while True:
#create a try and except block within the while loop to avoid a value error if the user gives a wrong input
    try:
      int(input("The amount that you want to apply the mortgage for: "))
      break
    except ValueError:
      print("Try again with a valid value.")

#add further commands
  input("The accomodity that you want to finance: ")

#create another while loop to return if the user gives a wrong input
  while True:
    z = input("Any ongoing mortgages (yes/no): ")
#use if statements to respond to respective inputs
    if z == "yes":
#nest a while loop to return if the user gives a wrong input
      while True:
        try:
          int(input("Total amount of the ongoing mortgage: "))
          break
        except:
          print("Try again with a valid value.")
      break
    elif z == "no":
      print("")
      break
    else:
      print("Try again with a valid value.")

#add the further commands     
  print("You will be informed when your mortage application is being processed.")
  print("Our mortgage consultant will talk to you about the chances of your mortgage being approved and answer any queries you may have.")
  print("Thank you for your time. Have a good day!")  


#create a while loop displaying all the options and asking for input
while True:
  print("Type in 1 for opening a bank account.")
  print("Type in 2 for withdrwawal from existing account.")
  print("Type in 3 for deposit to existing account.")
  print("Type in 4 to transfer money from existing account.")
  print("Type in 5 to apply for a mortgage.")
  print("Type in 6 to ask a question to our experts.")
  print("Type in 0 to exit.")
  x = input("OPTION: ")

#use if statements within the while loop to call out different functions or respond after slecting respective options
  if x == "1":
    openaccount()

  elif x == "2":
    moneywithd()

  elif x == "3":
    moneydep()

  elif x == "4":
    transfer()  

  elif x == "5":
    mort()

  elif x == "6":
    input("Type in you question: ")
    print("We will get back to you within 24 hours via the contact number you privided.")
    print("Have a nice day!")

  elif x =="0":
    print("Goodbye!")
    break

  else:
    print("Please enter a valid value and try again.")
    continue 

#nest a while loop to assk the user if they want to return to the main menu unless the option selected is not to exit the program
  while x != 0:
      y = input("Would you like to return to the main menu? (yes/no): ")
      if y == "yes":
        print("Okay!")
        break
      elif y == "no":
        print("Thank you for your time!")
        break
      else:
        print("Please respond with a yes or no and try again.")

#break for y to be "no" outside of the nested while loop so that the main while loop does not run back
  if y == "no":
    break

#no outside sources used for help
