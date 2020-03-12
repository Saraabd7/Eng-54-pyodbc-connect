from db_products_oop import *

products_tb = NWProducts()

while True:

    print('select 1 for all products')

    user_input = input('>>>')

    if user_input == '1':
        # get all our product using our new method
        # ITERATE ANd display them nicely
        data = products_tb.read_all()
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record.ProductName)