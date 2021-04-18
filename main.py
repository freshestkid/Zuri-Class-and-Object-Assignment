import budget



food = budget. Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "resturant")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(70, "Clothing")
clothing.withdraw(25.55)
clothing.withdraw(100)
entertainment = budget.Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(15)

print(food)
print(clothing)
print(entertainment)


main(module='test_module', exit=False)