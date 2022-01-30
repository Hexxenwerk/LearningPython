import csv

import requests


def load_data():
    response = requests.get('https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv')
    csv_result = csv.reader(response.text)
    print(type(csv_result))


def main():
    load_data()


if __name__ == '__main__':
    main()
