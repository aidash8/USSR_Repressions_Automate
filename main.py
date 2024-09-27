from argparse import ArgumentParser, ArgumentTypeError
from config import DBType
from read_data import ReadData
from process_data import process_data
from create_templates import create_docs
from create_query import create_query

# check that the number of templates is positive number
def check_positive(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise ArgumentTypeError(f"Invalid number of templates: {value}")
    
    if ivalue <= 0:
        raise ArgumentTypeError(f"{value} is an invalid positive int value")
    return ivalue

# convert the command line arg to Enum
def convert_dbtype_arg(value):
    try:
        return DBType(int(value))
    except ValueError:
        raise ArgumentTypeError(f"Invalid db type value: {value}")

def main(args):

    # parse out the arguments
    n = args.num
    db_type = args.db_type

    # create query
    query = create_query(n, db_type)
    print(query)
    # read data
    results = ReadData(query=query, db_type=db_type).read_data()
    # process data
    df = process_data(results)
    print(df)
    # # output the templates
    # create_docs(df) # the input can be list of tuples as well, not sure if want to use dataframe

if __name__ == "__main__":

    parser = ArgumentParser(description="Automatic Repressions Templates Generator")
    parser.add_argument("-n","--num",  
                        type=check_positive, 
                        default=5, 
                        help="Number of templates needed randomly generate")
    parser.add_argument("-d", "--db_type", 
                        type=convert_dbtype_arg, 
                        choices=list(DBType),
                        default=DBType.POSTGRESQL, 
                        help="DB type where data is stored")
    args = parser.parse_args()

    main(args)
