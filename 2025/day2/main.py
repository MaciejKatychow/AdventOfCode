

def is_half_duplicated(value: str) -> bool:
    if len(value) % 2 != 0:
        return False
    split = int(len(value)/2)
    first_half = value[:split]
    second_half = value[split:]
    if first_half == second_half:
        return True
    return False


def task_1(input: list[tuple[int,int]]) -> int:
    result = 0
    for start, end in input:
        for id_value in range(start, end+1):
            if is_half_duplicated(str(id_value)):
                result += id_value
    return result


def is_any_duplicated(value: str) -> bool:
    split = int(len(value)/2)
    for idx in range(split):
        to_check = value[:idx+1]
        splitted = []
        for split_idx in range(0, len(value), len(to_check)):
            splitted.append(value[split_idx:split_idx+len(to_check)])
        if len(list(filter(lambda x: x == to_check, splitted))) == len(splitted):
            return True
    return False


def task_2(input: list[tuple[int,int]]) -> int:
    result = 0
    for start, end in input:
        for id_value in range(start, end+1):
            if is_any_duplicated(str(id_value)):
                result += id_value
    return result



if __name__ == "__main__":
    with open ('2025/day2/input.txt') as f:
        data = f.read()

    input = []
    ranges = data.split(",")
    for r in ranges:
        start, end = r.split("-")
        input.append((int(start), int(end)))
    result = task_2(input)
    print(result)
