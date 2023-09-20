# normal function
def add(x,y):
    return x+y

# lamda function
lambda x,y: x+y


# usecase -> higher order functions
def compute(function, numbers):
    results = []
    for number in numbers:
        results.append(function(number))
    return results

if __name__=="__main__":
    numbers = [1,2,3,4,5,6,7,8,9]
    # square
    print(compute(lambda x:x**2, numbers))
    # cube
    print(compute(lambda x: x**3, numbers))
    # Add 5
    print(compute(lambda x: x+5, numbers))

    #results
    # [1, 4, 9, 16, 25, 36, 49, 64, 81]
    # [1, 8, 27, 64, 125, 216, 343, 512, 729]
    # [6, 7, 8, 9, 10, 11, 12, 13, 14]