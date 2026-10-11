
def user_entry():
    try:

        name = input("Enter the name of the product: ")
        price = float(input("Enter the price of the product: "))
        quantity = int(input("Enter the quantity: "))
        sub_total = price * quantity
        print(f"SUb Total : {sub_total}")
        tax_percent = 0.05


        tax = sub_total * tax_percent
        grand_total = sub_total + tax

        if grand_total <= 2000:
            delivary_charge = 50

        elif grand_total <= 1000:
            delivary_charge = 100

        else:
            delivary_charge = 0

        total = grand_total + delivary_charge

        print(f"Grand Total (including 5% tax):{grand_total}")
        print(f"Tax : {tax}")
        print(f"Delivary Charge: {delivary_charge}")
        print(f"Total payable Amount : {total}")
    except KeyError as e:
        print('Enter the Valid entry "Error" : {e}')

    except Exception as e:
        print(f"Error : {e}")

user_entry()
