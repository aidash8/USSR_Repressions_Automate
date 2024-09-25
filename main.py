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
    results = read_postgresql(query=QUERY)
    # process data
    df = process_data(results)
    # output the templates
    create_docs(df) # the input can be list of tuples as well, not sure if want to use dataframe

if __name__ == "__main__":
    main()
