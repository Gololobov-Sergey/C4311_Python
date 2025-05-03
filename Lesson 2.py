
def starLine():
    for i in range(30):
        print("*", end='')
    print()
#
#

# print(starLine())


# starLine()



def summa(a, b):

    c = a + b
    return c

res = summa(3,3)
print(res)


def isEven(a):
    if a % 2 == 0:
        return True
    return False

arr = [1,2,34,56,87,9,8,6,4,3,34,5,78,9]
c = 0
for el in arr:
    if isEven(el):
        c += 1


print(c)