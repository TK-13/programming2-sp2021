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
        else:
            self.balance += amount
            print('Deposit complete. New balance: ', str(self.balance), '\n')
            if not skip_receipt:
                receipt_requested = user_input('Would you like a receipt? (y/n) ', ['y', 'yes', 'n', 'no'],
                                               response='Invalid Entry')
                if receipt_requested == 'y' or receipt_requested == 'yes':
                    Account.give_receipt(self, quantity=amount)

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


def make_account(account_list, social_security_num, owner, password, account_number=0, starting_amt=0.0):
    auth('New account: Please enter your social security number: ', social_security_num,
         response='That is not your social security number. ')
    if not account_number:
        account_number = random.randrange(10000, 50000)
    new_account = Account(account_number, starting_amt, owner, password, social_security_num)
    account_list.append(account_number)
    return new_account


def ask_for_num(account_list):
    selected_account = int(input('What is your account number? '))
    if selected_account not in account_list:
        print('That account number is not in our database. Let me give you a call back later.')
        callback_num = input('What is your phone number? ')


# def close_account(self, social_security_num, owner, password):


def main():
    account_list = []
    dead_accounts = []
    print(account_list)

    print('\nScenario 1: Withdrawal')
    scenario_1 = Client('User', 987654321, 20.0, 1231231234, 'noname@gmail.com', '330 Webster Avenue')
    scen_1_account = Account(12345, 1000.0, 'User', 'abcde', scenario_1.social_security_num)
    account_list.append(scen_1_account.account_number)
    scenario_1.account = scen_1_account
    scenario_1.withdraw()

    print('\nScenario 2: New account + deposit')
    scenario_2 = Client('User 2', 246810121, 2000.0)
    scen_2_account = make_account(account_list, scenario_2.social_security_num, scenario_2.name, 'password 2',
                                  starting_amt=100)
    scenario_2.account = scen_2_account
    print(account_list)
    scenario_2.deposit(skip_receipt=True)

    print('\nScenario 3: Deposit + Receipt')
    scenario_3 = Client('User 3', 112112321, 1000.0)
    scen_3_account = Account(33333, 0.0, scenario_3.name, 'passpasswordword', scenario_3.social_security_num)
    scenario_3.account = scen_3_account
    account_list.append(scen_3_account.account_number)
    scenario_3.deposit(skip_receipt=False)

    print('\nScenario 4: Check balance + Receipt')
    scenario_4 = Client('User 4', 444444444, 1000.0)
    scen_4_account = Account(44444, 1301.56, scenario_4.name, 'passpasswordword', scenario_4.social_security_num)
    scenario_4.account = scen_4_account
    account_list.append(scen_4_account.account_number)
    scenario_4.get_info()

    print('\nScenario 5: Close account')
    scenario_5 = Client('User 5', 555555555, 1000.0)
    scen_5_account = Account(55555, 2000.0, scenario_5.name, 'password5', scenario_5.social_security_num)
    scenario_5.account = scen_5_account
    account_list.append(scen_5_account.account_number)
    print('Before:', scenario_5.account)
    scenario_5.close_account(account_list, dead_accounts)
    print('After:')
    try:
        print(scenario_5.account)
    except AttributeError:
        print("!!! Attribute error hit. scenario_5's account no longer exists !!!")

    print('\nScenario 6: Extreme withdrawal')
    scenario_6 = Client('User 6', 666666666, 1000.0)
    scen_6_account = Account(66666, 100.0, scenario_6.name, 'password6', scenario_6.social_security_num)
    scenario_6.account = scen_6_account
    account_list.append(scen_6_account.account_number)
    scenario_6.withdraw()

    print('\nScenario 7: Ask for an account number')
    scenario_7 = Client('User 7', 777777777, 1000.0, phone_num=1234567890)
    scen_7_account = Account(77777, 100.0, scenario_7.name, 'password7', scenario_7.social_security_num)
    scenario_7.account = scen_7_account
    account_list.append(scen_7_account.account_number)
    ask_for_num(account_list)


if __name__ == '__main__':
    main()
