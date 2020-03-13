from db_products_oop import *
import time
# this is my instance
products_tb = NWProducts()

while True:
    print('Welcome back')
    print('//////Loading//////')
    time.sleep(2)
    print('Select 1: to show  ll products \n 2: For a product by id \n 3: To add a product')

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
    elif user_input == '2':
        print('getting a product by id')
        # gather user input to use search for product id
        user_input = input('What product do you need? give me an ID:')
        # I need my instance + method
        result = products_tb.read_one(user_input)
        print('//////Loading//////')
        time.sleep(1)
        print(result.ProductName)
    elif user_input == '3':
        print('3 To add a product!!')
        # I need my instance + method
        # my user should be able to input a value
        user_input = input('What product do you want to create??')
        print('//////Loading//////')
        time.sleep(1)
        print(products_tb.create(user_input))
    elif 'exit' in user_input:
        print('Thank you!')
    break