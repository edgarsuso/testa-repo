import pandas as pd
import mysql.connector
from mysql.connector import errorcode
from sqlalchemy import create_engine
from sqlalchemy import text

db_config = {
    'user': 'root',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'python_practice'
}


csv_file_path = "/home/ek/testa-repo/tkarsuizmantosana_valmiera2024-01-01_2024-03-26.csv"

load_csv = pd.read_csv(csv_file_path, index_col=False, delimiter=';')


create_table_cmd = f"CREATE TABLE IF NOT EXISTS karsu_izmantosana_valmiera("
create_table_cmd += "id INT AUTO_INCREMENT PRIMARY KEY, "
create_table_cmd += ", ".join([f"{column} TEXT" for column in load_csv.columns])
create_table_cmd += ") ENGINE=InnoDB;"
print(create_table_cmd)

try:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
# Izpildam create table?
    cursor.execute(create_table_cmd)

    columns_placeholder = ", ".join([f"{column}" for column in load_csv.columns])
    values_placeholder = ", ".join(['%s'] * len(load_csv.columns))
    insert_cmd = f"INSERT INTO karsu_izmantosana_valmiera ({columns_placeholder}) VALUES ({values_placeholder})"

    for row in load_csv.itertuples(index=False, name=None):
        cursor.execute(insert_cmd, row)

    cnx.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Data imported successfully.")
finally:
    if cnx.is_connected():
        cursor.close()
        cnx.close()

#Karsu izmantosana
