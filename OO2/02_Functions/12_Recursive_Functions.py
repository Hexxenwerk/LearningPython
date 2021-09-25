# 5! = 5 * 4 * 3 * 2 * 1

def factorial_iterative_1(num) -> int:
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def factorial_iterative_2(num) -> int:
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result


def factorial_recursive(num) -> int:
    if num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)


print(factorial_iterative_1(5))
print(factorial_iterative_2(5))
print(factorial_recursive(5))
