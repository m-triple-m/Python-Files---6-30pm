from laptop import Laptop, Computer
import laptop

class Bank:
    bank_name = "XYZ Bank"

    def __init__(self, name, amt):
        self.name = name
        self.amount = amt

    def debit(self, amt):
        self.amount -=amt
        print(f"Rs. {amt} debited from {self.name}'s account")
        print(f"Remaining amount : {self.amount}")


    def credit(self, amt):
        self.amount +=amt
        print(f"Rs. {amt} credited from {self.name}'s account")
        print(f"Remaining amount : {self.amount}")

    def __repr__(self):
        return f'Remaining Balance : Rs. {self.amount}'

    def __add__(self, account):
        return self.amount+account.amount

    
if __name__ == "__main__":
    
    acc1 = Bank('Mr. Kennedy', 5000)

    acc2 = Bank('Miss Wong', 3000)

    lap = Laptop()
    print(lap.showspecs())

    print(acc1.name, acc1.amount)
    print(acc2.name, acc2.amount)

    acc1.credit(4000)
    acc2.debit(2300)
    acc2.credit(10000)
    acc1.debit(1599)

    print(acc1)
    print(acc2)

    print(acc1+acc2)

    print(acc1.bank_name, acc2.bank_name)

    acc1.bank_name = "ABC bank"

    print(acc1.bank_name, acc2.bank_name)

    print(isinstance(acc1, Bank))
    print(isinstance(acc1, Laptop))

    print(issubclass(Laptop, Computer))

    print(issubclass(Bank, object))
