from datetime import datetime as dt

class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []
        self.built = dt.now()

    def deposit(self, amount):
        self.balance += amount
        self.history.append(
            {
                "amount" : amount,
                "time" : dt.now(),
                "balance" : self.balance,
            }
        )
    def withdrawel(self, amount):
        pass
    
    def show_history(self):
        pass

    def __eq__(self, other):
        return self.built == other.built 

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


machine = ATM("Petra", 100)
machine.deposit(500)
print(machine.name)
print(machine.balance)
print(dir(machine))