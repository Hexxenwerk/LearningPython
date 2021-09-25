# 5! = 5 * 4 * 3 * 2 * 1

def factorial_iterative(num) -> int:
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def factorial_recursive(num) -> int:
    if num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)


print(factorial_recursive(5))
