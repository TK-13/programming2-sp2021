import random
import names
from tkinter import *


def user_input(message, options_list, response="", options_message="Valid Inputs: ", print_options=False,
               entry_type='str'):
    if print_options:
        print(options_message)
        for option in options_list:
            print(option)
    if entry_type == 'int':
        entry = int(input(message))
    elif entry_type == 'int':
        entry = float(input(message))
    else:
        entry = input(message)

    while entry not in options_list:
        print(response)
        entry = input(message)
    return entry


def auth(message, options_list, correct_option, response="", entry_type='int'):
    auth_done = False
    if entry_type == 'str':
        entry = str(input(message))
    elif entry_type == 'int':
        entry = int(input(message))
    print(entry)
    print(type(entry))
    while entry != correct_option:
        print(response)
        print('Correct: ', correct_option)
        entry = input(message)
    if entry == correct_option:
        return True
    else:
        return False


class Client:
    def __init__(self, name, social_security_num, cash, phone_num, email, mailing_address, account_list, account=None):
        self.name = name
        self.social_security_num = social_security_num
        self.cash = cash
        self.phone_num = phone_num
        self.email = email
        self.mailing_address = mailing_address
        if account:
            self.account = account
        # else:
        #     self.account = user_input('What is your account number? ', account_list,
        #                               response='That is not a valid number.', entry_type='int')
        # account_list.append(account_num)

    def withdraw(self, account_list):
        access_granted = auth("Please enter your account number: ", account_list, self.account.account_number,
                              response='That is not your account number.', entry_type='int')
        if access_granted:
            amount = float(input("How much would you like to withdraw? "))
            self.account.withdraw(amount)

    def deposit(self, account_list):
        correct_account_num = auth("Please enter your account number: ", account_list, self.account.account_number,
                                   response='Invalid number', entry_type='int')
        if correct_account_num:
            amount = float(input("How much would you like to withdraw? "))
            self.account.deposit(amount)
        else:
            print("That is not your account number.")


class Account:
    def __init__(self, account_number, balance, owner, password, social_security_num):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.password = password
        self.ssn = social_security_num

    def withdraw(self, amount):
        if amount > self.balance:
            print('That amount exceeds your balance.\n')
        else:
            self.balance -= amount
            print('Withdrawal complete. New balance: ', str(self.balance), '\n')

    def deposit(self, amount):
        self.balance += amount
        print('Deposit complete. New balance: ', str(self.balance), '\n')

    def get_info(self):
        query_options = ['The account number', 'The account owner']
        query = user_input('What do you want to know about this account?\n',
                           query_options,
                           response='That is not an option.', print_options=True)
        if query == query_options[0]:
            print(str(self.account_number))
        elif query == query_options[1]:
            print(str(self.owner))
        print()

    def give_receipt(self):
        print('!!! receipt placeholder !!!\n')
        print()


# def access_account(accounts, number=0, owner=""):
#     for i in range(len(accounts)):
#         if accounts[i['account_number']] == number or accounts[i['owner']] == owner:
#             print('Account found.\n')


def make_account(account_list, social_security_num, owner, password, account_num=0, starting_amt=0.0):
    if not account_num:
        account_num = random.randrange(10000, 50000)
    new_account = Account(account_num, starting_amt, owner, password, social_security_num)
    account_list.append(account_num)
    return new_account


# def close_account(self, social_security_num, owner, password):


def main():
    account_list = []
    print(account_list)
    User = Client('User', 987654321, 20.0, 1231231234, 'noname@gmail.com', '330 Webster Avenue', account_list)
    test = make_account(account_list, User.social_security_num, User.name, 'abcde', account_num=12345,
                        starting_amt=1000.0)
    User.account = test

    print(account_list)

    User.withdraw(account_list)
    # User.deposit(account_list)

    # test = Account(12345, 1000.00, 'User', 'abcde', 987654321)
    # test.withdraw(10)
    # test.deposit(20)
    # test.get_info()
    # test.give_receipt()

    # accounts = []
    # done = False
    # for i in range(47):
    #     dummy_num = random.randrange(10001, 99999)
    #     dummy_balance = random.randrange(10.00, 99999.00)
    #     dummy_owner = names.get_full_name()
    #     dummy_password = "password"
    #     dummy_ssn = random.randrange(100000000, 999999999)
    #     # dummy_account = Account(dummy_num, dummy_balance, dummy_owner, dummy_password, dummy_ssn)
    #     # accounts.append(dummy_account)
    #     accounts[dummy_num] = {'Balance': dummy_balance,
    #                            'Owner': dummy_owner,
    #                            'Password': dummy_password,
    #                            'Social Security Num': dummy_ssn
    #                            }

    # user_account = Account(10000, 500.00, 'Dan Frank', '3mbry0n1c', 123456789)
    # accounts.append(user_account)
    #
    # for a in accounts:
    #     print(a)
    # access = user_input("Enter your account number: ", accounts, response='That account number is invalid. ', entry_type='int')

    # while not done:
    #     command_list = ['1', '2,', '3', '4', '5,']
    #     UI_list = ['1. Make a withdrawal. ',
    #                '2. Make a deposit. ',
    #                '3. Get account information. ',
    #                '4. Make a new account. ',
    #                '5. Close an account.']
    #     command = user_input("What would you like to do? ", command_list, 'That is not a valid input. ')
    #     for option in UI_list:
    #         print(option)


if __name__ == '__main__':
    main()

    # todo: full main program is lower priority than class structures
    # start with simple functionality, then add more.
