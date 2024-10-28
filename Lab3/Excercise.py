def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

def fibonacci_iterative(n):
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Test the function
n = 10
fib_list = fibonacci_iterative(n)
print(f"Fibonacci sequence up to F({n}) = {fib_list}")

import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")

def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

# New function to find the index of the first Fibonacci number that exceeds a given value
def index_of_first_exceeding(value):
    a, b = 0, 1
    index = 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index

# Test the function
value = 20
index = index_of_first_exceeding(value)
print(f"The index of the first Fibonacci number that exceeds {value} is {index}.")

# New function to check if a number is a Fibonacci number
def is_fibonacci(num):
    if num < 0:
        return False
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

# Test the function
test_number = 21
print(f"{test_number} is a Fibonacci number: {is_fibonacci(test_number)}")

# New function to calculate the ratio between consecutive Fibonacci numbers
def fibonacci_ratios(n):
    ratios = []
    fib_sequence = fibonacci_iterative(n)
    for i in range(2, len(fib_sequence)):
        ratios.append(fib_sequence[i] / fib_sequence[i-1])
    return ratios

# Test the function
ratios = fibonacci_ratios(30)
print(f"Ratios of consecutive Fibonacci numbers up to F(30): {ratios}")
