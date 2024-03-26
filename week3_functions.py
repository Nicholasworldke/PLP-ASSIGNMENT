def calculate_discount(price, discount_percent):

    if discount_percent>=20:
        price = price * (100-discount_percent)/100
        return price

    else:
        return price


price=int(input("Enter the price of the product: "))

discount_percent=int(input("Enter the Discount Percent: "))
print(calculate_discount(price,discount_percent))

