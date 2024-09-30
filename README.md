# USSR_Repressions_Automate
- main.py: The main driver program
- read_data.py:
  - reads data from various data sources where .sql file was loaded
  - output list of tuples
- process_data.py: cleans data and outputs to the right format, e.g. to pandas dataframe
- creat_docs: creates templates, currently creates docx files as they needed to be formatted manually

# If psycopg2 fails:
```
 pip install psycopg2-binary
```
