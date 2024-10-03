# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
salePrice = retailPrice * 0.75
# Write your assignment statements here for profit, salePrice, and saleProfit

print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(retailPrice-wholesalePrice))
print("Sale Price: $" + str(retailPrice * 0.75))
print("Sale Profit: $" + str(salePrice-wholesalePrice))
