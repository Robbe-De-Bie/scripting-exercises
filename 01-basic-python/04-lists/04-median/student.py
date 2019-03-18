# Write your code here
def median(ns):
    ns = sorted(ns)
    lengte = len(ns)
    if(lengte%2 == 0):
        return (ns[(lengte//2)-1]+ns[lengte//2])/2        
    else:
        return ns[(lengte//2)]