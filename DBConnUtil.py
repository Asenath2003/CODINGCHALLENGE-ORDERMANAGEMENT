import pyodbc

class DBConnUtil:
    @staticmethod
    def getDBConn():
        try:
            connection = pyodbc.connect('Driver={SQL Server};'
                                        'Server=LAPTOP-LOUFODEH\SQLEXPRESS;'
                                        'Database=Order_Mgmt;'
                                        'Trusted_Connection=yes;')
            return connection
        except Exception as e:
            print("Error connecting to the database:", e)
            return None
