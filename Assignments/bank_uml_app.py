import random


def user_input(message, options_list, response="", options_message="Valid Inputs: ", print_options=False):
    if print_options:
        print(options_message)
        for option in options_list:
            print(option)
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


# TODO: make into main()
class Bank:
    def __init__(self, accounts):
        self.accounts = accounts

    def access_account(self, password, number=0, owner=""):
        for i in self.accounts:
            if i['account_number'] == number or i['owner'] == owner:
                print('Account found.')

    def new_account(self, social_security_num, owner, password, starting_amt=0.0):
        account_num = random.randrange(10000, 50000)
        new_account = Account(account_num, starting_amt, owner, password, social_security_num)
        self.accounts.append(new_account)

    def close_account(self, social_security_num, owner, password):
