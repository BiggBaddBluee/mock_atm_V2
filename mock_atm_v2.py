database = {}
from random import randrange
bal = 5000


#landing page, an entry point into the system
def landingPage():
    
    print('Welcome to Bankblue, Do you have an account with us?')
    
    

    options = int(input('Yes (1) No (2)\n'))
    
    if (options == 1):
        login()
    elif (options == 2):
        register()
    else:
        print("invalid option!")
        landingPage()   
        

def register():
    """for registering users into the system if they don't have an account with bankblue"""

    print("REGISTER")

    #the variables used
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    email = input('What is your email address?\n')
    password = input('Please create a secure password\n')
    user_name =  f'{first_name}{last_name}'
    account_number = gen_account() #the random number generated

    print('===== ===== ===== ======= =====')
    print('HERE ARE YOUR BANK DETAILS, PLEASE KEEP IT SAFE')
    print(f'Your UserId is {user_name}')
    print(f'Your account number is {account_number}')
    print(f'Your Password is {password}')
    print('===== ===== ===== ======= =====')


    database [account_number] = [first_name, last_name, email, user_name, password]
    
    print('Your account has been successfully created')
    
    login()
        

#generating account
def gen_account():
    """for generating 10 digit account number for user identification"""

    return randrange(1111111111, 9999999999)  


#login
def login():

    print('LOG IN')
    print('Please log in to your account')
    userId = input('Type in your UserId or email\n')
    
    for accountNumber, user_details in database.items():

        if userId == user_details[3] or user_details[2]:
            inputPassword = input('Type in your Password \n')
            if inputPassword == user_details[4]:
                bank_operation(user_details)
            else:
                print('Invalid password')
        else:
            print('UserId not found, please try again')


#bank operation
def bank_operation(user):
    """this leads to the different functions users are about to perform"""
    
    print('Welcome %s %s' %(user[0], user[1]))
    options = int(input('What do you want to do? \nDeposit(1), Withdraw(2), Check Balance(3), logout(4), exit(5)\n'))

    if options == 1:
        deposit()
    elif options == 2:
        withdraw()
    elif options == 3:
        balance(user)
    elif options == 4:
        logout() 
    elif options == 5:
        print("***SESSION TERMINATED***")
        exit()
    else:
        print('wrong option selected')
        bank_operation(user)



def deposit():

    deposited_amount = int(input('How much do you want to deposit? \n'))

    if deposited_amount > 0:
        print(f'You just deposited N{deposited_amount} into your acount')
        print(f'Your account balance is now N{deposited_amount + bal}')

    else:
        print('Wrong amount deposited, please try again')
        deposit() #loop back to the deposit


def withdraw():
    withdraw_amount = int(input(f'Your account balance is N{bal} \nHow much do you want to withdraw?\n'))
    if withdraw_amount > bal:
        print('Insufficient funds, try again')
        withdraw()
    elif withdraw_amount == 0:
        print('invalid amount, try again')
        withdraw()    
    else:
        print(f'You just withdrew N{withdraw_amount}\nYour account balance is now {bal - withdraw_amount}')


def balance(user):
    print(f'Your account balance is {bal}')
    bal_action = int(input('Do you want to perform another action? Yes(1) No(2)\n'))

    if bal_action == 1:
        bank_operation(user)
    elif bal_action == 2:
        print('***SESSION TERMINATED***')
        exit()
    else:
        print('Invalid option selected')


def logout():
    login()


#LAUNCHING SYSTEM
landingPage()