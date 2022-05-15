def encrypt_letter(character: str, key: int) -> str:
    if not character.isalpha():
        return character

    abc = 'abcdefghijklmnopqrstuvwxyz'
    idx = abc.find(character) + key
    if idx >= len(abc):
        idx %= len(abc)

    return abc[idx]


def calculate_shifts(letter: str) -> int:
    return 'abcdefghijklmnopqrstuvwxyz'.find(letter)


def encrypt_text(text: str, keyword: str) -> str:
    text, keyword, cipher = text.lower(), keyword.lower(), ''
    for idx, character in enumerate(text):
        if idx >= len(keyword):
            idx %= len(keyword)
        key = calculate_shifts(keyword[idx])
        cipher += encrypt_letter(character, key)

    return cipher


def main():
    text = input('Which text should be encrypted: ')
    keyword = input('Which keyword should be used? ')

    print(encrypt_text(text, keyword))


main()
