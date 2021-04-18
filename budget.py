class Category:

    def__init__(self, name, amount):
        self.name = Name
        self.amount = Amount
        self.ledger = list()

    def__str__(self):
        title = f"{self.name:*^30}\n"
        items == ""
        total = 0
        for item in self.ledgers:
            item += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + \n

            total +=['amount']

        output = title + items + "Total" + str(total)
        return output
 

    def deposit(self, amount, description"""):
        """
        A deposit method that accept an amount and description, if no description is given, it should default to an empt string.The method should append an object to the ledger list in the form of
        {"amount": amount, "description" description}
        """

        self.ledger.append ({"amount": amount, "description": description})

    def withdraw(self, amount, description"""):
        """
        A withdraw method that is similar to adposit method, but the amount passed in sholud be stored in the ledger as a negative number.. if there are not enough funds, nothing shold be added to the ledger.This methos sholud return true if the withdrawal took place , and False otherwise
        """"
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """"
        A get balance methos that returns the current balance of the budget category based on the deposit and withdrawls that have occured
        """"
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"] 

        return total_cash

    def transfer(self, amount, category):
        """"
        A transfer method that accepts an amount and another budget category as argument. The method should add a withdrwal with the amountand the description "Transfer to[Destination Budget category]". The method sholud then all a deposit to the other bedget category with the amount and the description "Transfer from [source Budget Category]"
        . If there are not enough funds,nothing should be added to either ledgers. This methos sholud return True if the transfer took place and False otherwise.
        """"

        if(self.check_funds(amount)):
            self.witdraw(amount, "Transfer to" + category.name)
            category.deposit(amount, "Transfer from" + self.name)
            return True
        return False  

    def check_fund(self, amount):
        """
        This methos accpet an amount as an argument. It return False if the amount is greater that the balance of the budget category and returns true otherwise. This method sholud be used by both the withdraw methos and transfer methos
        """
        if(self.get_balance()>=amount):
            return True
        return False

        object = Budget("Food", 1000)
        object = Budget("Clothing", 1000)
        object = Budget("Entertanment", 1000)
    
    
