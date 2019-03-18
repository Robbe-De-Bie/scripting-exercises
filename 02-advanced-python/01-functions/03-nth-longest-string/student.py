# Write your code here
def nth_longest_string(n,strings):
    lijst = sorted(strings, key=len, reverse=True)
    return lijst[n-1]
