def nums(*args):
    return sum(args)

print(nums(10,20,40,60))

def keyValue(**kwargs):
    for k,val in kwargs.items():
        print(k,val)

keyValue(a=10,b=20,c=30)