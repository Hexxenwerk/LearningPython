import csv

import requests


def load_data():
    response = requests.get('https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv')
    csv_reader = csv.reader(response.text, delimiter=';')
    for row in csv_reader:
        print(''.join(row), end='')
    print(response.text)


def main():
    load_data()


if __name__ == '__main__':
    main()
