import mysql.connector
def fetch_student_info(grno):
    try:
        # Connect to the MySQL database
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="elections"
        )

        # Create cursor object to execute queries
        cursor = db_connection.cursor()

        # Execute a query to fetch data based on the provided GRNO
        cursor.execute("SELECT NAME, HOUSE FROM sampledb WHERE GRNO = %s", (grno,))

        # Fetch the row from the result set
        row = cursor.fetchone()

        # Check if row exists
        if row:
            name, house = row
            print(f"Name: {name}, House: {house}")
        else:
            print("No student found with the provided GRNO.")

    except mysql.connector.Error as error:
        print("Error fetching data from MySQL database:", error)

    finally:
        # Close cursor and database connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'db_connection' in locals() and db_connection is not None:
            db_connection.close()

if __name__ == '__main__':
    grno = input("Enter the GRNO (4 digit number): ")
    if grno.isdigit() and len(grno) == 5:
        fetch_student_info(grno)
    else:
        print("Invalid GRNO. Please enter a 5-digit number.")
