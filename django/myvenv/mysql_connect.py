import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='my-sql-nan4',
    host='localhost',
    port='13306'
)

cursor = cnx.cursor()
cursor.execute('SELECT * FROM supu_db.users')

for id, name in cursor:
    print(f'{id}: {name}')