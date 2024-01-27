import pyodbc
from sqlalchemy import create_engine
import pandas as pd

#Simple tests for sqlalchemy and pyodbc - dependent of the db

def test_sql_alchemy():
    #SQL Alchemy
    e = create_engine('mssql+pyodbc://.\SQLEXPRESS/NCAAM_Stats?trusted_connection=yes&driver=SQL+Server')
    sql = "select * from Rank"
    df = pd.read_sql(sql,con=e)
    assert df.size > 0, "Fail"

def test_pyodbc():
    #pyodbc
    SERVER = r'.\SQLEXPRESS'
    DATABASE = 'NCAAM_Stats'
    USERNAME = 'mktal'
    PASSWORD = '<password>'
    SQL_QUERY = "SELECT * FROM Rank"
    connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};TrustedConnection=true;'
    #connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};TrustServerCertificate=True;UID={USERNAME};Trusted_Connection=True'

    conn = pyodbc.connect(connectionString) 
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    x = cursor.fetchall()
    assert(len(x)>0), "Fail"

if __name__ == "__main__":
    test_sql_alchemy()
    test_pyodbc()