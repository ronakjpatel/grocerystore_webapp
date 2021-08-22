import  mysql.connector


cnx = mysql.connector.connect(
user='root',
password='root',
host='localhost',
database='grocery_store_db',
port=3306
)

cursor = cnx.cursor()
query = 'SELECT * FROM grocery_store_db.products;'
cursor.execute(query)

for (product_id, name, unit_of_measure, price_per_unit) in cursor:
    print(product_id, name, unit_of_measure, price_per_unit)


cnx.close()