import psycopg2
from config import DATABASE, USER, HOST, PORT

def read_postgresql(query, db=DATABASE, user=USER, host=HOST, port=PORT):
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
    cur.execute(query)

    # Fetch all results
    results = cur.fetchall()

    # Close the cursor and connection
    cur.close()
    conn.close()

    return results