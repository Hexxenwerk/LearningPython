import requests


def main():
    response = requests.get('https://api.thedogapi.com/v1/breeds')
    for x in response.json():
        for y in x:
            print(y)


if __name__ == '__main__':
    main()
