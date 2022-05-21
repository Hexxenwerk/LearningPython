import requests


def main():
    search_term = input('Please enter a search term: ')
    r = requests.get(f'https://itunes.apple.com/search?term={search_term}&entity=album')
    j = r.json()
    print(f'The search returned {j["resultCount"]} results.')
    for record in j['results']:
        print(f"Artist: {record['artistName']} - Album: {record['collectionName']} - Track Count: {record['trackCount']}")


if __name__ == '__main__':
    main()
