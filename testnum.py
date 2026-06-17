def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

assert check_even_odd(2) == "Even"
assert check_even_odd(7) == "Odd"
assert check_even_odd(0) == "Even"
assert check_even_odd(-3) == "Odd"

print("All tests passed!")
