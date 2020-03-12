from db_connect_oop import *

class NWProducts(MSDBConnection):

    def __init__(self):
        super().__init__()
        self.table = 'PRODUCTS'

    def __sql_query(self, query): # private to avoid user SQL injection
        return self.cursor.execute(query)

    def read_all(self):
        # return data with all products
        rows = self.__sql_query(f'SELECT * from {self.table}')
        return rows

    # READ ALL products (select)



    # Write all the CRUD methods



    #R - Read ONE product based on id :) (Select)

    def get_one_product_by_id(self):
        id = int(input('Please enter the Product ID...'))
        query = f"SELECT * FROM products WHERE ProductID = {id} "
        result = self._MSDBConnection__sql_query(query)
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(
                f'Product ID: {record.ProductID} - Name: {record.NameOfProducts}')
        return 'Thank You.'

    # Create ONE product (insert)
    def create_products (self, NameOfProducts):
        query = ('INSERT INTO Products (Name of Product')
        result = self.__sql_query(query)
        self.docker_Northwind.commit()
        return result

    # tip: search commit for pyodbc
    # delete (delete)

    def __filter_sql_injection(self, query):
    # do some regular expression to filter sql attacks
    # return clean expression (like no DROP or DELETE with no WHERE)
        pass