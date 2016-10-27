def min (first, *args):
    for x in args:
        if x<first:
            first=x
    return first
    
print(min(1,2,3,4,5,6))