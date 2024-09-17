class Bank:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.str = date + name
        self.jopa = 1
    def __str__(self):
        return self.name + self.date


sber = Bank("Sberbank", "1841")
x = str(sber)
print(x)

x = sber.__dict__
print(len(x))
