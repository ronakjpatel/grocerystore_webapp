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


    cnx.close()

    return result

def insert_new_product(connection, product):
    cursor = connection.cursor()

    query_string = ("INSERT INTO products (name,unit_of_measure,price_per_unit) VALUES (%s,%s,%s)")

    data = (product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query_string,data)

    connection.commit()

    return cursor.lastrowid



if __name__=='__main__':
    conn = get_sql_connection()
    print(insert_new_product(conn,{
        'product_name':'cabbage',
        'uom_id':'2',
        'price_per_unit':'10'
    }))