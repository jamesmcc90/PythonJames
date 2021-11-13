import pyodbc
import pandas as pd

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=JAMES-PC\SQLEXPRESS;DATABASE=James_DB;Trusted_Connection=yes;')

query = pd.read_sql('SELECT * FROM Cars', conn)

print(query.head(20))

import os
print(os.path.expanduser('~'))