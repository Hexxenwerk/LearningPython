from urllib.request import urlopen


def main():
    with urlopen('https://www.google.de') as response:
        with open('testfile.txt', mode='w', encoding='utf-8') as html_file:
            html_file.write(response.read().decode(response.headers.get_content_charset()))

    with open('testfile.txt', mode='r') as html_file:
        print(html_file.read())


if __name__ == '__main__':
    main()
