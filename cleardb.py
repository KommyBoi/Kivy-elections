import mysql.connector
try:
    db_connection = mysql.connector.connect(
        host="192.168.1.125",
        user="khsg",
        password="Chunav@24",
        database="elections"
    )
    cursor = db_connection.cursor()

    cursor.execute(f"UPDATE contestants SET VOTES = 0")
    db_connection.commit()

except mysql.connector.Error as error:
    print("Error fetching data from MySQL database:", error)

# finally:
#     if cursor:
#         cursor.close()
#     if db_connection:
#         db_connection.close()