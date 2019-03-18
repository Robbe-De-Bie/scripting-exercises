# Write your code here
def is_prime(n):
    return n> 1 and all(n%s != 0 for s in range(2,n))