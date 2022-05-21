def is_prime(number: int) -> bool:
    if number < 2 or (number > 2 and not number % 2):
        return False
    for i in range(3, number, 2):
        if not number % i:
            return False
    return True


def prime_list(number: int) -> list:
    return [n for n in range(2, number + 1) if is_prime(n)]


def main():
    number = int(input('Up to which number do you want all prime numbers: '))
    print(prime_list(number))


main()
