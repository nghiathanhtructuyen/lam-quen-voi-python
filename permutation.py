def F(x, y, n):
    def permutation(n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
            
        numerator = 1
        denominator = 1
        
        for i in range(k):
            numerator *= (n - i)
            denominator *= (i + 1)
            
        return numerator // denominator
        
    # Define the binomial coefficient function using the permutation function
    def binomial_coefficient(n, k):
        return permutation(n, k)
    
    # Recursive function to compute F(x, y, n)
    def F_recursive(x, y, n):
        if n == 0:
            return 1
        elif n == 1:
            return x + 1 / y
        else:
            result = 0
            for k in range(n + 1):
                coeff = binomial_coefficient(n, k)
                result += coeff * x**(n - k) * (1 / y)**k
            return result
    
    return F_recursive(x, y, n)

# Test the function F(x, y, n)
x = 2
y = 3
n2 = 2
n3 = 3

print(F(x, y, n2))  # Output should be 5.444444444444444 (2^2 + 2*2*(1/3) + (1/3)^2)
print(F(x, y, n3))  # Output should be 12.703703703703702 (2^3 + 3*2^2*(1/3) + 3*2*(1/3)^2 + (1/3)^3)