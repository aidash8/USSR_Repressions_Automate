import psycopg2
import sqlite3
from config import DBType, DATABASE, USER, HOST, PORT

class ReadData:
    def __init__(self, query, db_type=DBType.POSTGRESQL):
        self.db_type = db_type
        self.query = query

    def read_data(self):
        if self.db_type == DBType.POSTGRESQL:
            results = self._read_postgresql(db=DATABASE, user=USER, host=HOST, port=PORT)
        elif self.db_type == DBType.SQLITE:
            results = self._read_sqlite("names.sqlite3")
        elif self.db_type == DBType.SQLDUMP:
            raise NotImplementedError
        else:
            raise ValueError(f"Not valid choice: {self.db_type}")
        
        return results

    def _read_sqlite(self, path):
        cursor = None
        connection = None
        try:
            # Step 2: Establish a connection
            connection = sqlite3.connect(path)
            cursor = connection.cursor()

            # Step 4: Execute an SQL query
            query = "SELECT * FROM names;"
            cursor.execute(query)

            # Step 5: Fetch the result set
            results = cursor.fetchall()

            return results

            # # Process data
            # for row in results:
            #     print(row)

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

        finally:
            # Step 6: Ensure that the cursor and connection are closed
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def _read_postgresql(self, db, user, host, port):
        # Establish a connection to the database
        conn = psycopg2.connect(
            database=db,
            user=user,
            host=host,
            port=port
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute a query
        cur.execute(self.query)

        # Fetch all results
        results = cur.fetchall()

        # Close the cursor and connection
        cur.close()
        conn.close()

        return results