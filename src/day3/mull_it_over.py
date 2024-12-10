import re
from functools import reduce


def read_input(file: str) -> str:
    with open(file, "r") as f:
        text = f.read()
    return text


def calculate_uncorrupted_memory_instructions(corrupted_memory: str):
    pattern = "mul\\((\\d{1,3}),(\\d{1,3})\\)"
    raw_instructions = re.findall(pattern, corrupted_memory)
    return reduce(lambda x, y: x + y,
                  map(lambda t: int(t[0]) * int(t[1]), raw_instructions))


def calculate_uncorrupted_memory_instructions_with_toggle(corrupted_memory: str):
    # Throw away memory content that follows a don't() instruction
    do_memory = "".join([li.split("don't")[0] for li in corrupted_memory.split("do()")])
    pattern = "mul\\((\\d{1,3}),(\\d{1,3})\\)"
    raw_instructions = re.findall(pattern, do_memory)
    return reduce(lambda x, y: x + y,
                  map(lambda t: int(t[0]) * int(t[1]), raw_instructions))


if __name__ == '__main__':
    input_file = "input.txt"
    mem = read_input(input_file)
    print(calculate_uncorrupted_memory_instructions(mem))
    print(calculate_uncorrupted_memory_instructions_with_toggle(mem))
