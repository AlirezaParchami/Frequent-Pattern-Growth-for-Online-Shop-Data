import os
import csv


def load_data():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.csv')
    with open(file_path, 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        transactions = list()
        for row in csv_data:
            transactions.append([item for item in row if item != ''])
    return transactions
