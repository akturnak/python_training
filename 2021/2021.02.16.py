import numpy as np

CURVE_CENTER = 80
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])


def curve(grades):
    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change
    return np.clip(new_grades, grades, 100)


print(curve(grades))

temperatures = np.array(
    [
        29.3,
        42.1,
        18.8,
        16.1,
        38.0,
        12.5,
        12.6,
        49.9,
        38.6,
        31.3,
        9.2,
        22.2,
    ]
)
print(temperatures.shape)

temperatures = temperatures.reshape(2, 2, 3)
print(temperatures.shape)
print(temperatures)

print("\nswapaxes\n")
temperatures = np.swapaxes(temperatures, 1, 2)
print(temperatures)

table = np.array(
    [
        [5, 3, 7, 1],
        [2, 6, 7, 9],
        [1, 1, 1, 1],
        [4, 3, 2, 0],
    ]
)

print(f"table.max(): {table.max()}")

print(f"table.max(axis=0): {table.max(axis=0)}")

print(f"table.max(axis=1): {table.max(axis=1)}")

A = np.arange(32).reshape(4, 1, 8)
print(f"A: {A}")

B = np.arange(48).reshape(1, 6, 8)
print(f"B: {B}")

print(f"A + B: {A + B}")

square = np.array(
    [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]
)

for i in range(4):
    print(f"square[:, {i}]: {square[:, i]}")
    print(f"square[{i}, :]: {square[i, :]}")
    assert square[:, i].sum() == 34
    assert square[i, :].sum() == 34

print()
print(f"square[:2, :2]: {square[:2, :2]}")
assert square[:2, :2].sum() == 34

numbers = np.linspace(5, 50, 24, dtype=int).reshape(4, -1)
print(f"numbers: {numbers}")

mask = numbers % 4 == 0
print(mask)

print(numbers[mask])

by_four = numbers[numbers % 4 == 0]
print(by_four)
