cost = int(input("Enter cost price:"))
sell = int(input("Enter selling price:"))
profit = sell - cost
print("Profit is: ")
print(profit)
sell = sell + ((sell*5)/100)
profit = sell - cost
print("Profit if selling proce is increased by 5% is: ")
print(profit)
