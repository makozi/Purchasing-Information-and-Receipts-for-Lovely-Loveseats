# Adding In The Catalog

lovely_loveseat_description='''
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
'''

lovely_loveseat_price= 254.00


stylish_settee_description= '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''
stylish_settee_price= 180.50

luxurious_lamp_description='''
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
'''

luxurious_lamp_price= 52.15
# In order to be a business, we should also be calculating sales tax. The sales_tax is 8.8%
sales_tax= .088

# Our First Customer

customer_one_total=0


# a list of the descriptions of things been purchased
customer_one_itemization= " "

customer_one_total +=  lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

itemization_description = luxurious_lamp_description


# Ready to Check out. Calculating sale tax
customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax



# Printing receipt
print('Customer One Items:', customer_one_itemization)

print('Customer One Total:' , customer_one_total)


