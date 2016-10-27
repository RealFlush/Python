def max (first, *args):
    for x in args:
        if x>first:
            first=x
    return first
    
print(max(1,2,3,4,5,6))