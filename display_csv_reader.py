import csv
import pandas as pd

def display_csv_reader_dict():
    with  open('monsters.csv') as f:
        dictReader = csv.DictReader(f, delimiter=',')
        for row in dictReader:
            print(row["monsterName"] + " is priced at " + row["price"])

def display_csv_reader():
    with open('monsters.csv') as f:
        # create a reader object
        # give the reader the file as well as the delimiter which will be a comma
        reader = csv.reader(f, delimiter=",")
        #skip the first iteration (column name)
        next(reader)
        #iterate through the reader 
        for row in reader:
            # for each row, out the monster name
            # the monster name is in the second column so that would be a index one
            print(row[1])

def display_csv_pandas():
    df = pd.read_csv('/monsters.csv')
    print(df)

if __name__ == "__main__":
    display_csv_pandas()
