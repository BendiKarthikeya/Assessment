'''Given three numbers a, b and m. Calculate (ab % m)
Example input :
2 5 3
Example output :
2
Explanation :
25 % 3 = 32 % 3 = 2'''


def power_modulo(a, b, m):
    result = 1

    
    a = a % m
    
    while b > 0:
        # If b is odd, multiply result with a and take modulo m
        if b % 2 == 1:
            result = (result * a) % m
        
        # Square a and take modulo m
        a = (a * a) % m

        # Divide b by 2
        b //= 2

    return result

if _name_ == "_main_":

    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    m = int(input("Enter the value of m: "))

    # (a^b % m)
    result = power_modulo(a, b, m)

    print(f"The result of ({a}^{b} % {m}) is: {result}")