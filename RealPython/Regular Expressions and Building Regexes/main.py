import re


def main():
    line = 'This stone is rock hard like this asteroid from the other galaxy.'
    for word in re.finditer(r'\bth(?:is|e)\b', line, re.IGNORECASE):
        print(word.group())


if __name__ == '__main__':
    main()
