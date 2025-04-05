import mysql.connector

conn = mysql.connector.connect(
        host="weewx",
        port=3306,
        user="weewx",
        password="weewx"
        )

conn.close()
