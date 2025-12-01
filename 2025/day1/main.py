
with open ('2025/day1/input.txt') as f:
    data = f.read().splitlines()

def move_circle_right(circle: int, jump: int) -> tuple[int, int]:
    new_circle = circle + jump
    too_much_circle = new_circle - 100
    passed_zero = 0
    if too_much_circle > 0:
        new_circle = too_much_circle
        passed_zero = 1 if circle not in (0, 100) else 0
    return new_circle, passed_zero


def move_circle_left(circle: int, jump: int) -> tuple[int, int]:
    diff = circle - jump
    new_circle = diff
    passed_zero = 0
    if jump > circle:
        new_circle = 100 + diff
        passed_zero = 1 if circle not in (0, 100) else 0
    return new_circle, passed_zero

result = 0
circle = 50

for move in data:
    direction = move[0]
    jump = int(move[1:])
    if jump > 99:
        count_zeros = int(str(jump)[0])
        result += count_zeros
        jump -= count_zeros * 100

    if direction == "R":
        circle, passed_zero = move_circle_right(circle, jump)
    else:
        circle, passed_zero = move_circle_left(circle, jump)

    result += passed_zero
    if circle in (0, 100):
        result += 1

print(result)
