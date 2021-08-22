from flask import Flask, request, jsonify
import products_page
from sql_conn import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts',methods=['GET'])

def getProducts():
    products = products_page.get_all_products(connection)

    response = jsonify(products)

    response.headers.add('Access-Control-Allow-Origin','*')

    return response



if __name__ == "__main__":

    print("Starting the flask server")
    app.run(port=5000)
