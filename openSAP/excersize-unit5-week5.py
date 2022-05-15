def reaction_path(speed: float):
    return speed * 3 / 10


def brake_distance(speed):
    return (speed / 10) ** 2


def stopping_distance(speed):
    return reaction_path(speed) + brake_distance(speed)


input_speed = float(input('Enter speed in km/h: '))
print(stopping_distance(input_speed))
