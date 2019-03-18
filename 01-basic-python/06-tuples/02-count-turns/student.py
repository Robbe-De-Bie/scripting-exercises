# Write your code here
def count_turns(ns):
    aantal = 0

    for (x, y, z) in zip(ns, ns[1:], ns[2:]):
        if x < y > z or x > y < z:
            aantal += 1
    
    return aantal