input_range = "272091-815432"
start_ = int(input_range.split("-")[0])
end_ = int(input_range.split("-")[1])


def check_ascending(n):
    return "".join(sorted(n)) == n


def check_two_consecutive_digits(n):
    repeat_count = 0
    for n1, n2 in zip(n, n[1:]):
        if n1 == n2:
            repeat_count += 1
        else:
            if repeat_count == 1:
                return True
            repeat_count = 0
    return repeat_count == 1


p2_count = 0

for n in range(start_, end_):
    n = str(n)
    if check_ascending(n):
        if check_two_consecutive_digits(n):
            p2_count += 1

print(f"Number of Combinations {p2_count}")