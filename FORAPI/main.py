from fastapi import FastAPI
from pydantic import BaseModel
from connector.connectorr import myModel

md = myModel()

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
def read_root():
    return md.getuserdata()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}













# from flask import Flask
# from flask_mysqldb import MySQL
#
# app = Flask(__name__)
#
# # MySQL configurations
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'your_username'
# app.config['MYSQL_PASSWORD'] = 'your_password'
# app.config['MYSQL_DB'] = 'your_database_name'
#
# mysql = MySQL(app)
#
# @app.route('/')
# def index():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT * FROM your_table_name''')
#     results = cur.fetchall()
#     cur.close()
#     return str(results)
#
# if __name__ == '__main__':
#     app.run(debug=True)








