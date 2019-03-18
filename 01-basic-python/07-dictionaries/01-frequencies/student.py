# Write your code here
def frequencies(xs):
    dic = {}
    for x in xs:
        if x not in dic:
            dic[x] = 0
        dic[x] += 1
    return dic

