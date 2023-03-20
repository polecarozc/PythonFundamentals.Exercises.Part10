class person:
    def __init__(self, id, first_name, last_name):
        self.id =id
        self.first_name = first_name
        self.last_name = last_name

class account:
    def __init__(self, number, type, owner, balance):
        self.numer = number
        self.type = type
        self.owner = owner
        self.balance = balance

class bank:
    def __init__(self):
        self.bank_info = {1: "person", 2: "account", 3: 0}

    def add_customer(self, person):
        self.bank_info.update({1: person.first_name +" "+ person.last_name})

    def add_account(self, account_info):
        self.bank_info.update({2: account_info})
    def remove_account(self):
        print("Account was cleared...")
        self.bank_info.update({1: "person", 2: "account", 3: 0})
    def adding_funds(self, money_to_add):
        money_added = int(money_to_add) + int(self.bank_info.get(3))
        self.bank_info.update({3: str(money_added) })
    def balance_inquiry(self):
        print(self.bank_info[3])

person1 = person(7698, "bob", "chob")
person1_account = account(1001, "checking", "primary", 1000)
small_bank = bank()
small_bank.add_customer(person1)
small_bank.add_account(person1_account.type)
small_bank.adding_funds(100)
small_bank.adding_funds(100)
print(small_bank.bank_info)
small_bank.balance_inquiry()
