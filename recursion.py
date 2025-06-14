# Question number 1
def recursive_multiply(a: int, b: int) -> int:
    if b == 0:
        return 0
    if b == 1:
        return a
    if b < 0:
        return -recursive_multiply(a, -b)
    return a + recursive_multiply(a, b - 1)

# Question number 2
def power(base: float, exponent: int) -> float:
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent < 0:
        return 1 / power(base, -exponent)
    if exponent % 2 == 0:
        half_power = power(base, exponent // 2)
        return half_power * half_power
    else:
        return base * power(base, exponent - 1)

# Question number 3
def count_down(n: int) -> None:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        print(0)
        return
    print(n)
    count_down(n - 1)

# Question number 4
def count_up(n: int) -> None:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        print(0)
        return
    count_up(n - 1)
    print(n)

# Question number 5
def reverse_string(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

# Question number 6
def is_prime(n: int, divisor: int = None) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 2:
        return False
    if divisor is None:
        divisor = int(n ** 0.5)
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

# Question number 7
def fibonacci_memoized(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]
