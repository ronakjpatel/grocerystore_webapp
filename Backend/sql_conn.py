import  mysql.connector


#Creating cnx as a global variable
__cnx = None


def get_sql_connection():
    global __cnx

    #Only create the variable if it has not been created 
    if __cnx is None:
         
        __cnx = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='grocery_store_db',
            port=3306
        )

    return __cnx