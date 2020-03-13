import pyodbc

class MSDBConnection():
    # We need to connect to our DB

    def __init__(self):
        # Variables for connections
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        # Making the connection
        self.conn = pyodbc.connect('DSN=MYMSSQL;UID='+self.username+';PWD='+self.password+';'+'DATABASE='+self.database)
        # making cursor
        self.cursor = self.conn.cursor()

    def __sql_query(self, query):
        return self.cursor.execute(query)





# nw_db_objct = MSDBConnection()
#
# rows = nw_db_objct.sql_query('SELECT * FROM Products')
#
# print(rows.fetchone())