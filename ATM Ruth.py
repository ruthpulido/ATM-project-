account = [
    ["11","1111"],   # account is a table with: [0]=account number, [1]=pin 
    ["22","2222"],
    ["33","3333"],
    ["44","4444"]
]                          
balance_00 = {"11": 1000,
              "22" : 2000,
              "33" : 3000,
              "44" : 4000}           
trying = 3
enter_your_chois = 'Enter "d" to deposit \nenter "w" to withdraw \nenter "b" to balance \nenter "e" to exit '
goodbye = "Thank you for using Sparkasse! Don't forget you card. "
unvalid = "That is not a valid option, please choose an option from the menu"

def deposit_money_funk():
    if key in balance_00:
        deposit = float(input('Enter the Amount, put the money and press Enter ')) # <-- customer enters how much money to deposit
        balance_00[key] = balance_00[key] + deposit
        print('Here please, your amount deposited is: {} €. Your balance is {} € now. ' .format(deposit, balance_00[key]))
        print(goodbye)

def withdraw_money_funk():
    if key in balance_00:
        withdraw = float(input('Enter the Amount: '))  # <-- customer enters how much money to withdraw
        if withdraw <= balance_00[key]:
            balance_00[key] = balance_00[key] - withdraw
            print('Here please, your amount withdraw is: {} €. Your balance is {} € now. ' .format(withdraw, balance_00[key]))
            print(goodbye)
        else:
            print("you don't have enough money in your account.")

def check_balance_funk():
    if key in balance_00:
        print('Your balance is {} €' .format(balance_00[key]))
        print(goodbye)

# the program starts:                

print('Welcome to Sparkasse! ')
while trying != 0:
    accont_number_input = input('Enter your account number, 2 digits ')   # <-- customer enters account number (2 digits).
    pin_input = input(('Enter your pin, 4 digits '))      # <-- customer enters pin (4 digits).
    data_input =[accont_number_input, pin_input]
    key = accont_number_input
    if (data_input not in account):                # <-- while loop checks account number and pin are correct and match. 
        trying = trying - 1                         # <- There are three attempts
        print('invalid pin or account number! You have {} tries left. '.format(trying))
    else:
        user_choise = input(enter_your_chois)
        if user_choise == 'd':
            deposit_money_funk()
        elif user_choise == 'w':
            withdraw_money_funk()   
        elif user_choise == 'e':
            print(goodbye)
        elif user_choise == 'b': # <-- check balancce
            check_balance_funk()
        else:
            print(unvalid) 