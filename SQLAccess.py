import pyodbc as pyodbc


class SQLAccess:

    def __init__(self):
        self.server = 'dubhacks23.database.windows.net'
        self.database = 'DubHacks2023'
        """ removed username and password for privacy """
        self.connectString = 'Driver={ODBC Driver 18 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password

    def execute_non_query(self, query):
        cnxn = pyodbc.connect(self.connectString)
        cursor = cnxn.cursor()
        cursor.execute(query)
        cursor.close()
        cnxn.commit()
        cnxn.close()

    def execute_non_query_many(self, query, data):
        cnxn = pyodbc.connect(self.connectString)
        cursor = cnxn.cursor()
        cursor.fast_executemany = True
        cursor.executemany(query, data)
        cursor.close()
        cnxn.commit()
        cnxn.close()

    def execute_non_query_select(self, query):
        cnxn = pyodbc.connect(self.connectString)
        cursor = cnxn.cursor()
        cursor.execute(query)

        rows = []
        for row in cursor:
            rows.append([elem for elem in row])
        cursor.close()
        cnxn.commit()
        cnxn.close()
        return rows
    
    def fetch_all_records(self, table_name):
        query = f"SELECT * FROM {table_name}"
        return self.execute_non_query_select(query)
    
    def clear_dataset():
        db = SQLAccess()
        query = "DELETE FROM FaceEmbeddingEntryTable"
        db.execute_non_query(query)