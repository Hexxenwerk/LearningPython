# without return
from typing import Tuple


def addieren_1(x: int, y: int) -> None:
    total = x + y
    print(total)


# with return
def addieren_2(x: int, y: int) -> int:
    total = x + y
    return total


# with multiple return
def addieren_3(x: int, y: int) -> Tuple[int, str, bool]:
    total = x + y
    return total, 'Die Summe beträgt:', True


def main():
    addieren_1(50, 60)
    print(addieren_2(50, 60))
    print(addieren_3(50, 60), type(addieren_3(50, 60)))


if __name__ == '__main__':
    main()
