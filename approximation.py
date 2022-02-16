import math
from typing import Tuple

def approximate(irrational_number: float) -> list[float]:
    coefficients = []
    x = irrational_number
    for i in range(3):
        x, a = math.modf(x)
        coefficients.append(a)
        x = 1/x

    return coefficients

def continued_fraction(coefficients: list[float]) -> float:
    prev_frac = 0
    new_frac = 0
    if (len(coefficients) == 2):
        return (coefficients[0] * coefficients[1] + 1, coefficients[1])
    for i in range(len(coefficients) - 1, 0, -1):
        new_frac = 1/(coefficients[i] + prev_frac)
        prev_frac = new_frac

    return coefficients[0] + new_frac

def evaluate(coefficients: list[float]) -> tuple: 
    prev_numerator = coefficients[-1]
    prev_denominator = 1
    numerator = 0
    denominator = 0
    for i in range(len(coefficients) - 2, 0, -1):
        # a + b / c = (ac + b) / c
        numerator = coefficients[i] * prev_numerator + prev_denominator
        denominator = prev_numerator

        prev_numerator = numerator
        prev_denominator = denominator

    # switch numerator and denominator
    return (denominator + numerator, numerator)

res_list = []
for i in range(1, 12):
    num = 2**(i/12)
    res = approximate(num)
    m = max(res)
    ind = res.index(m)
    frac = continued_fraction(res)
    print(f"K = {i} = {res}")
    error_percent = ((num / frac) - 1) * 100
    #numerator, denominator = frac.as_integer_ratio()
    numerator, denominator = evaluate(res)

    res_list.append([res, m, ind, num, frac, error_percent, i, numerator, denominator])

    
correct_list = [7, 5, 2, 9, 4, 11, 1, 3, 6, 8, 10]

res_list.sort(key=lambda x: abs(x[5]))

print("####################################")
print("####################################")
print("####################################")
print("Evaluating 2^(k/12) for different k.")
for i in range(len(res_list)):
    print("------------------------------")
    print(f"k = {res_list[i][6]}, Pos: {i+1}({correct_list.index(res_list[i][6]) + 1})")
    print(f"Coefficents: {res_list[i][0]}")
    print(f"Biggest coefficient: {res_list[i][1]}, at index: {res_list[i][2]}")
    print(f"Input number: {res_list[i][3]}")
    print(f"Approximation: {res_list[i][4]}")
    print(f"Approximation fraction: {res_list[i][7]} / {res_list[i][8]}")
    print(f"Error percentage: {res_list[i][5]}")
    #print(f"1/Error: {1/abs(res_list[i][5])}")
    print("------------------------------")

#l = []
#for i in range(len(res_list)):
#    l.append((1/abs(res_list[i][5]))**(1/2))

#a = sum(l)
#for i in range(len(res_list)):
#    l[i] = l[i] / a

#print(l)

# sortera efter storlek på nämnare
res_list.sort(key= lambda x: x[8])

#for l in res_list:
#    print(l)