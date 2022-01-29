import requests


def main():
    response = requests.get('https://api.thedogapi.com')
    [print(f'{key} is {response.json()[key]}') for key in response.json()]


if __name__ == '__main__':
    main()
