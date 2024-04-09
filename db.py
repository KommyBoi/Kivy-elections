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
        cursor.execute(f"SELECT HOUSE FROM sampledb WHERE GRNO = {grno}")

        # Fetch the row from the result set
        row = cursor.fetchone()

        # Check if row exists
        if row:
            # Fetch the first (and only) column of the row, which corresponds to 'HOUSE'
            house = row[0]
            print(f"House: {house}")
            return house  # Return the house information

    except mysql.connector.Error as error:
        print("Error fetching data from MySQL database:", error)

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()

def fetch_info(final_num):
    return fetch_student_info(final_num)

def UpdateVotes(UID):
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

        # Execute a query to increment votes for a specific candidate
        cursor.execute(f"UPDATE candidates SET VOTES = VOTES + 1 WHERE UID = '{UID}' ")

        # Commit the changes to the database
        db_connection.commit()

        # Execute a query to fetch the total number of votes for the candidate
        # cursor.execute("SELECT VOTES FROM candidates WHERE UID = 'HB-1' ")

        # Fetch the total number of votes for the candidate
        # total_votes = cursor.fetchone()[0]
        # print("Total votes ", total_votes)

    except mysql.connector.Error as error:
        print("Error executing SQL queries:", error)

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()



def check_entry_exists(value):
    connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="elections"
        )
    cursor = connection.cursor()
    query = f"SELECT * FROM sampledb WHERE GRNO = %s"
    cursor.execute(query, (value,))
    result = cursor.fetchone()
    cursor.close()
    return result

if __name__ == '__main__':
    grno = input("Enter the GRNO (5 digit number): ")
    if grno.isdigit() and len(grno) == 5:
        fetch_student_info(grno)
    else:
        print("Invalid GRNO. Please enter a 5-digit number.")
