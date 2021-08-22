from sql_conn import get_sql_connection


def get_all_products(conn):


    cursor = conn.cursor()
    query = "SELECT products.product_id, products.name, products.unit_of_measure, products.price_per_unit, unit_of_measure_table.uom_name FROM products inner join unit_of_measure_table on products.unit_of_measure = unit_of_measure_table.uom_id;"


    cursor.execute(query)

    result = []

    for (product_id, name, unit_of_measure, price_per_unit,measure_name) in cursor:
        result.append(
            {
            'product_id' : product_id,
            'name': name,
            'unit_of_measure': unit_of_measure,
            'price_per_unit': price_per_unit,
            'measure_name': measure_name
            }
        )
        print(product_id, name, unit_of_measure, price_per_unit,measure_name)


    conn.close()

    return result

def insert_new_product(connection, product):
    cursor = connection.cursor()

    query_string = ("INSERT INTO products (name,unit_of_measure,price_per_unit) VALUES (%s,%s,%s)")

    data = (product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query_string,data)

    connection.commit()

    return cursor.lastrowid


#Delete product using product_ID

def delete_product(connection,product_id):
    cursor = connection.cursor()

    query_string = ("DELETE FROM products WHERE product_id = " + str(product_id))
    cursor.execute(query_string)
    connection.commit()




if __name__=='__main__':
    conn = get_sql_connection()
    print(delete_product(conn,8))
        