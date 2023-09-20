# simple function
def make_even(number: int) -> int:
    if number % 2 == 1:
        return number + 1
    return number


# map
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = map(make_even, x)

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # map
    y = map(make_even, x)
    print(list(y))
