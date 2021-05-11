import random


# Supposed to make it easier to validate user inputs.
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


# Rather than confirm from a list of correct answers, this function is meant to validate whether the user enters a
# specific answer (like an account number).
def auth(message, correct_option, response=""):
    entry = int(input(message))
    while entry != correct_option and entry != "":
        print(response)
        print('(Debug) Correct: ', correct_option)  # This is just here to make it easier to use on the developer side.
        # it would be removed for the true product.
        entry = int(input(message))


class Client:
    def __init__(self, name, social_security_num, cash, phone_num=0, email='', mailing_address='', account=None):
        self.name = name
        self.social_security_num = social_security_num
        self.cash = cash
        self.phone_num = phone_num
        self.email = email
        self.mailing_address = mailing_address
        self.account = account

    # This checks that the right account is in use, then runs the sub-method within that account to withdraw/deposit.
    def withdraw(self):
        auth("Please enter your account number: ", self.account.account_number,
             response='That is not your account number.')
        amount = float(input("How much would you like to withdraw? "))
        withdrawal = self.account.withdraw(amount)
        if withdrawal:
            self.cash += amount
            print('Your cash: ', self.cash)

    def deposit(self, skip_receipt):
        auth("Please enter your account number: ", self.account.account_number,
             response='Invalid number')
        amount = float(input("How much would you like to deposit? "))
        self.account.deposit(amount, self.cash, skip_receipt)
        self.cash -= amount
        print('Your cash: ', self.cash)

    def get_info(self):
        self.account.get_info()

    # This is meant to delete the specified account object, remove its number from the account_list, and add it's
    # number to a list of 'dead' accounts.
    def close_account(self, account_list, dead_list):
        dead_list.append(self.account.account_number)
        account_list.remove(self.account.account_number)
        del self.account
        print('Your account has been closed.')


class Account:
    def __init__(self, account_number, balance, owner, password, social_security_num):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.password = password
        self.ssn = social_security_num

    # If the amount is greater than one's balance or cash, respectively, the method returns as False, and the
    # withdrawal/deposit does not go through.
    def withdraw(self, amount):
        if amount > self.balance:
            print('That amount exceeds your balance.\n')
            return False
        else:
            self.balance -= amount
            print('Withdrawal complete. New balance: ', str(self.balance))
            return True

    def deposit(self, amount, cash, skip_receipt):
        if amount > cash:
            print('That amount exceeds your cash on hand.\n')
            return False
        else:
            self.balance += amount
            print('Deposit complete. New balance: ', str(self.balance), '\n')
            # skip_receipt is meant to make it easier to deposit non-manually, without having to trigger the
            # receipt system.
            if not skip_receipt:
                receipt_requested = user_input('Would you like a receipt? (y/n) ', ['y', 'yes', 'n', 'no'],
                                               response='Invalid Entry')
                if receipt_requested == 'y' or receipt_requested == 'yes':
                    Account.give_receipt(self, quantity=amount)
            return True

    # Lets the user learn more about an account, or print a receipt with it's balance.
    def get_info(self):
        query_options = ['The account number', 'The account owner', 'The balance']
        query = user_input('What do you want to know about this account?\n',
                           query_options,
                           response='That is not an option.', print_options=True)
        if query == query_options[0]:
            print(str(self.account_number))
        elif query == query_options[1]:
            print(str(self.owner))
        elif query == query_options[2]:
            Account.give_receipt(self, quantity=0)

    def give_receipt(self, quantity):
        print('Receipt: \nDate: (date would go here) \nName:', self.owner, '\nNumber:', self.account_number,
              '\nDeposit Amount:', quantity, '\nTotal Balance:', self.balance)


def make_account(user, account_list, social_security_num, owner_name, password, account_number=0, starting_amt=0.0,
                 setup_mode=True):
    # similar to give_receipt, setup_mode is meant to make it easier to use this function as both a user-interface
    # where they enter the social security number to authenticate the account's creation, and a method of creating
    # fake accounts for demonstration, without that hassle.
    if not setup_mode:
        auth('New account: Please enter your social security number: ', social_security_num,
             response='That is not your social security number. ')
    # for the same purpose, if an account number is not specified, it is randomly generated.
    if not account_number:
        account_number = random.randrange(10000, 50000)
    new_account = Account(account_number, starting_amt, owner_name, password, auth)
    user.account = new_account
    account_list.append(account_number)
    return new_account


# This tries to handle the 7th scenario, where a teller asks for an account number, and has to be called back.
def ask_for_num(account_list):
    selected_account = int(input('What is your account number? '))
    if selected_account not in account_list:
        print('That account number is not in our database. Let me give you a call back later.')
        callback_num = input('What is your phone number? ')


def main():
    account_list = []
    dead_accounts = []
    print(account_list)

    print('\nScenario 1: Withdrawal')
    scenario_1 = Client('User', 987654321, 100.0, 1231231234, 'noname@gmail.com', '330 Webster Avenue')
    make_account(scenario_1, account_list, scenario_1.social_security_num, scenario_1.name, 'password 1',
                 account_number=12345, starting_amt=100.0)
    scenario_1.withdraw()

    print('\nScenario 2: New account + deposit')
    scenario_2 = Client('User 2', 246810121, 2000.0)
    make_account(scenario_2, account_list, scenario_2.social_security_num, scenario_2.name, 'password 2', setup_mode=False)
    scenario_2.deposit(skip_receipt=True)

    print('\nScenario 3: Deposit + Receipt')
    scenario_3 = Client('User 3', 112112321, 1000.0)
    make_account(scenario_3, account_list, scenario_3.social_security_num, scenario_3.name, 'password 3',
                 account_number=33333)
    scenario_3.deposit(skip_receipt=False)

    print('\nScenario 4: Check balance + Receipt')
    scenario_4 = Client('User 4', 444444444, 1000.0)
    make_account(scenario_4, account_list, scenario_4.social_security_num, scenario_4.name, 'password 4',
                 account_number=44444, starting_amt=1250.)
    scenario_4.get_info()

    print('\nScenario 5: Close account')
    scenario_5 = Client('User 5', 555555555, 1000.0)
    make_account(scenario_5, account_list, scenario_5.social_security_num, scenario_5.name, 'password 5',
                 starting_amt=2000.0, account_number=55555)
    print('Before:', scenario_5.account)
    scenario_5.close_account(account_list, dead_accounts)
    print('After:')
    try:
        print(scenario_5.account)
    except AttributeError:
        print("!!! Attribute error hit. scenario_5's account no longer exists !!!")

    print('\nScenario 6: Extreme withdrawal')
    scenario_6 = Client('User 6', 666666666, 1000.0)
    make_account(scenario_6, account_list, scenario_6.social_security_num, scenario_6.name, 'password 6',
                 starting_amt=100.0, account_number=66666)
    scenario_6.withdraw()

    print('\nScenario 7: Ask for an account number')
    scenario_7 = Client('User 7', 777777777, 1000.0, phone_num=1234567890)
    make_account(scenario_7, account_list, scenario_7.social_security_num, scenario_7.name, 'password 7',
                 starting_amt=100.0, account_number=77777)
    ask_for_num(account_list)


if __name__ == '__main__':
    main()
