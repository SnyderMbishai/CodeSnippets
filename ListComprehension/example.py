# simple function
def make_even(number: int) -> int:
    if number % 2 == 1:
        return number + 1
    return number


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # list Comprehension
    y = [make_even(num) for num in x]
    print(y)
