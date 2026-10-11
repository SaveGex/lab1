lazy import random as r

in_the_task_was_asked_for_3_numbers = 3

some_digits: list[dict[str, int]] = [{
    chr(r.randint(ord('a'), ord('z'))) : r.randrange(10)
} for _ in range(in_the_task_was_asked_for_3_numbers)]

some_digits.sort(
    key=lambda item: next(iter(item.values())),
    reverse=True,
)

print(next(iter(some_digits[0].values())))

# labels = ("top 1", "middle", "the last one")

# for label, item in zip(labels, some_digits):
#     for name, value in item.items():
#         print(f"{label}: {name} = {value}")