
print(123, 345, 56, 324, 234, 345, 45, 78, 56, 634, 52, 35, 34567, 69)

def func(*args):
    print("Прийшло", len(args) , "параметрів")
    for el in args:
        print(el, end=', ')
    print()


func(123, 345,56,324,234,345,45,78,56,634,52,35,34567,69)

def avg(*args):
    return sum(args)/len(args)

print(avg(12,0,0))