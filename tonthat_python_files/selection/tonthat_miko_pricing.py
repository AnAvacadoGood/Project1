#Programmed by: Miko Tonthat
#Date: 07/03/19
#Description: This program calculates the subtotal, discount, and the total depending on the quantity of items.

#input
price = float(input("What is the price of each item? "))
quantity = int(input("How many are you ordering? "))

#calculation to get subtotal
subtotal = price * quantity

#calculation to get discount
if quantity < 10:
    discount = subtotal * 0
elif quantity < 20:
    discount = subtotal * .1
elif quantity < 50:
    discount = subtotal * .2
elif quantity < 100:
    discount = subtotal * .25
else:
    discount = subtotal * .3

#calculation to get total
total = subtotal - discount

#output/results
print("Subtotal: $", format((subtotal), '.2f'))
print("Discount: $", format((discount), '.2f'))
print("Total: $", format((total), '.2f'))