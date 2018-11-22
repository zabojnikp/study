import Account

t = Account.Transaction(500, "2018-10-10", "CZ")
a = Account.Account(123456, "Petra Zabojnikova")
new_a = Account.Account(8765, "Milos Turek")
print(a.all_eur)
print(a.number)
print(a.name)
a.name = "Petra New Name"
print(a.name)
a.apply(t)
print(a.balance)
print(a.all_eur)
a.save()
x = a.load()
print(x)