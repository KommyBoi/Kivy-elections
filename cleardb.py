import mysql.connector
try:
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="elections"
    )
    cursor = db_connection.cursor()

    cursor.execute(f"UPDATE candidates SET VOTES = 0")
    db_connection.commit()

except mysql.connector.Error as error:
    print("Error fetching data from MySQL database:", error)

finally:
    if cursor:
        cursor.close()
    if db_connection:
        db_connection.close()