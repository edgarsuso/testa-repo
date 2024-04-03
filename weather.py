import pandas as pd
import mysql.connector as msql
from mysql.connector import errorcode

db_config = {
    'user': 'root',
    'password': 'password',
    'host': '127.0.0.1',
    #'database': 'weather_practice'
}

csv_file_path = "/home/ek/testa-repo/test.csv"

load_csv = pd.read_csv(csv_file_path, index_col=False, delimiter=';')

#print(load_csv.columns)

#for value in load_csv.columns:
    #print(value)

try:
    conn = msql.connect(**db_config)
    if conn.is_connected():
        cursor = conn.cursor() #So es nesaprotu
        cursor.execute("CREATE DATABASE Weather")
        print("Database created")
except errorcode as err:
    print("Error while connecting to MySQL", err)

#test.csv
