# Write your code here
def contains_duplicates(xs):
    for k in range(0,len(xs)):
        for i in range(k+1,len(xs)):
            if xs[k] == xs[i]:
                return True
    return False