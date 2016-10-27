import csv

def load_data():
    with open('header_data.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        return [(header[0], header[1:]) for header in reader]

