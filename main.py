amount = int(input("PLease enter the amount of withdrawal: "))

amount1 = amount//100
amount2 = (amount%100)//50
amount3 = (amount2%50)//10


print("The ammount of 100tk notes: ", amount1)
print("The amount of 50tk notes: ", amount2)
print("The amount of 10tk notes: ", amount3)