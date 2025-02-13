import os

def List():
    database_path = '/home/titobyte/Desktop/Databases/aurora_databases'
    databases = os.listdir(database_path)
    for database in databases:
        count = 0
        print(f"{count + 1} : {database}")
    
List()