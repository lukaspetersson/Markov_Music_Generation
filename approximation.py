import math

def approximate(irrational_number: float) -> list[float]:
    coefficients = []
    x = irrational_number
    for i in range(10):
        x, a = math.modf(x)
        coefficients.append(a)
        if x == 0:
            # not irrational? 
            break
        x = 1/x

    return coefficients

def continued_fraction(coefficients: list[float]) -> float:
    prev_frac = 0
    new_frac = 0
    for i in range(len(coefficients) - 1, 0, -1):
        new_frac = 1/(coefficients[i] + prev_frac)
        prev_frac = new_frac

    return coefficients[0] + new_frac

print("Evaluating 2^k for different k.")
for i in range(1, 13):
    print("----------------------------")
    print(f"k = {i}")
    num = 2**(i/12)
    res = approximate(num)
    m = max(res)
    ind = res.index(m)
    frac = continued_fraction(res[0:ind + 1])
    error_percent = ((num / frac) - 1) * 100
    numerator, denominator = frac.as_integer_ratio()

    print(f"Coefficents: {res}")
    print(f"Biggest coefficient: {m}")
    print(f"Input number: {num}")
    print(f"Approximation: {frac}")
    print(f"Approximation fraction: {numerator} / {denominator}")
    print(f"Error percentage: {error_percent}")
