import psycopg2
from config import DBType, DATABASE, USER, HOST, PORT

class ReadData:
    def __init__(self, query, db_type=DBType.POSTGRESQL):
        self.db_type = db_type
        self.query = query

    def read_data(self):
        if self.db_type == DBType.POSTGRESQL:
            results = self._read_postgresql(db=DATABASE, user=USER, host=HOST, port=PORT)
        elif self.db_type == DBType.SQLLIGHT:
            raise NotImplementedError 
        elif self.db_type == DBType.SQLDUMP:
            raise NotImplementedError
        else:
            raise ValueError(f"Not valid choice: {self.db_type}")
        
        return results

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