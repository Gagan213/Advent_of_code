input_range = "272091-815432"
start_ = int(input_range.split("-")[0])
end_ = int(input_range.split("-")[1])


def check_ascending(n):
    return "".join(sorted(n)) == n


def check_repeat(n):
    for digit1, digit2 in zip(n, n[1:]):
        if digit1 == digit2:
            return True


p1_count = 0


for n in range(start_, end_):
    n = str(n)
    if check_ascending(n):
        if check_repeat(n):
            p1_count += 1

print(f"Number of Combinations {p1_count}")
