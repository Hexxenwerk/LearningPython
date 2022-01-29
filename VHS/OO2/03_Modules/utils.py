def find_max(*numbers: int) -> int:
    largest: int = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i

    return largest
