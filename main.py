from read_data import read_postgresql
from process_data import process_data
from create_templates import create_docs


QUERY = """
SELECT *
FROM formular
LIMIT 10
"""

def main():

    # read data
    # results = read_postgresql(query=QUERY)
    # df = process_data(results)
    create_docs()

if __name__ == "__main__":
    main()
