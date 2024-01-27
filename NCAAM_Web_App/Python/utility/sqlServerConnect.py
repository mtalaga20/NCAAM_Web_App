import pyodbc

def connect():
    connectionString = f'''
        DRIVER={{SQL Server}};
        SERVER=.\SQLEXPRESS;
        DATABASE=NCAAM_Stats;
        TrustedConnection=true
    '''
    connection = pyodbc.connect(connectionString)
    return connection.cursor