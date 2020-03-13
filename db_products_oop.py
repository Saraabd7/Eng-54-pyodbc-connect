from db_connect_oop import *

class NWProducts(MSDBConnection):

    def __init__(self):
        super().__init__()
        self.table = 'PRODUCTS'

    def __sql_query(self, query): # private to avoid user SQL injection
        return self.cursor.execute(query)

    # READ ALL products (select)
    def read_all(self):
        # return data with all products
        rows = self.__sql_query(f'SELECT * from {self.table}')
        return rows

    #R - Read ONE product based on id :) (Select)
    def read_one(self, id):
        # I want to get one product out
        # I want to identify the one product using an ID
        # I need to build a query to get one product, where ID is the specific ID
        query = f"SELECT * FROM {self.table} WHERE ProductID = {id}"
        # I need to make my DB call
        # I can use my __sql_query to make the call
        result = self.__sql_query(query)
        # breakpoint()
        # I want to return to object with all the information
        return result.fetchone()
        # handle your errors and failures
            # it could fail to find and ID and I want:
            # 1) code not to break
            # 2) let my user know that it failed

    # Create ONE
    def create(self, name_arg):
        # I need want to create a product
        # To Create a product I need a name and nothing else
        # I need to build a query
        query = f"INSERT INTO {self.table} (ProductName) VALUES ('{name_arg}')"
        # I need to call the db
        self.__sql_query(query)
        # from the pyodb package I also need to commit it
        if self.conn.commit() == None:
            return True
        else:
            return False

    # Write all the CRUD methods



    # Create ONE product (insert)
    # tip: search commit for pyodbc
    # delete (delete)

    def __filter_sql_injection(self, query):
    # do some regular expression to filter sql attacks
    # return clean expression (like no DROP or DELETE with no WHERE)
        pass


# Testing get one product
# db_products_instance = NWProducts()
#
# one_product = db_products_instance.read_one(60)
#
# print(one_product.ProductName)
# print(one_product)


# To run a method
# i need an instance
# db_products_instance = NWProducts()
# print(db_products_instance.create('Eggs and more food'))