import mysql.connector

class myModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='csek2141011103',
            password='password',
            database='abcd'
        )
        self.conn.autocommit = True
        self.curr = self.conn.cursor()
        print("connected successfully")

    def getuserdata(self):
        self.curr.execute("SELECT * FROM employee")
        data = self.curr.fetchall()

        if self.curr.rowcount > 0:
            return {'Payload': data}
        return "No data found"
