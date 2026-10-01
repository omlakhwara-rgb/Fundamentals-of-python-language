#3.Build a Zomato-style bill calculator: take the price of a food item and quantity as input, convert them to float and int, calculate the total bill, and display it with a message like 'Your total bill is ₹350.50'.

price = float(input("enter your food item: "))
quantity = int(input("Enter the quantity: -"))

totalbill = price * quantity

print ("your total bill is ", totalbill)