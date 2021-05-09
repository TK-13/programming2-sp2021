import random
import names
from tkinter import *


def user_input(message, options_list, response="", options_message="Valid Inputs: ", print_options=False, entry_type='str'):
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


class Client:
    def __init__(self, accounts, social_security_num, cash, phone_num, email, mailing_address):
        self.accounts = accounts
        self.social_security_num = social_security_num
        self.cash = cash
        self.phone_num = phone_num
        self.email = email
        self.mailing_address = mailing_address


class Account:
    def __init__(self, account_number, balance, owner, password, social_security_num):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.password = password
        self.ssn = social_security_num

    def withdraw(self, amount):
        self.balance -= amount
        print('Withdrawal complete. New balance: ', str(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print('Deposit complete. New balance: ', str(self.balance))

    def get_info(self):
        query_options = ['The account number.', 'The account owner.']
        query = user_input('What do you want to know about this account?',
                           query_options,
                           response='That is not an option.')
        if query == query_options[0]:
            print(str(self.account_number))
        elif query == query_options[1]:
            print(str(self.owner))

    def give_receipt(self):
        print('!!! receipt placeholder !!!\n')


def access_account(accounts, number=0, owner=""):
    for i in range(len(accounts)):
        if accounts[i['account_number']] == number or accounts[i['owner']] == owner:
            print('Account found.')


def make_account(accounts, social_security_num, owner, password, starting_amt=0.0):
    account_num = random.randrange(10000, 50000)
    new_account = Account(account_num, starting_amt, owner, password, social_security_num)
    accounts.append(new_account)

# def close_account(self, social_security_num, owner, password):


def main():
    accounts = {}
    done = False
    for i in range(47):
        dummy_num = random.randrange(10001, 99999)
        dummy_balance = random.randrange(10.00, 99999.00)
        dummy_owner = names.get_full_name()
        dummy_password = "password"
        dummy_ssn = random.randrange(100000000, 999999999)
        # dummy_account = Account(dummy_num, dummy_balance, dummy_owner, dummy_password, dummy_ssn)
        # accounts.append(dummy_account)
        accounts[dummy_num] = {'Balance': dummy_balance,
                               'Owner': dummy_owner,
                               'Password': dummy_password,
                               'Social Security Num': dummy_ssn
                               }

    user_account = Account(10000, 500.00, 'Dan Frank', '3mbry0n1c', 123456789, )
    accounts[10000] = user_account

    # print(accounts.keys())
    access = user_input("Enter your account number: ", accounts.keys, response='That account number is invalid. ', entry_type='int')
    if access == 10000:
        print("Yay")


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