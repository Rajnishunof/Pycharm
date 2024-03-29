from fastapi import FastAPI
import cx_Oracle

app = FastAPI()

# Connect to Oracle database
dsn_tns = cx_Oracle.makedsn('hostname', 'port', service_name='service_name')
connection = cx_Oracle.connect(user='username', password='password', dsn=dsn_tns)

# Define endpoint to execute SQL query
@app.get("/execute_query")
def execute_query(query: str):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return {"data": result}

# Close database connection when the application stops
@app.on_event("shutdown")
def shutdown_event():
    connection.close()
