# 1
def countdown(num):
    newList = []
    for num in range(num, -1, -1):
        newList.append(num)
    return newList
print(countdown(10))

# 2
def printReturn(x):
    print(x[0])
    return x[1]
printReturn([3,5])
# y = printReturn([3,5])
# print(y)

# 3
def firstPlusLng(x):
    temp = x[0] + x[len(x)-1]
    return temp 
print(firstPlusLng([1,2,4,5,6]))

# 4
def greaterThanSecond(x):
    if len(x) < 2:
        return False
    newList = []
    for i in range(len(x)):
        if x[i] > x[1]:
            newList.append(x[i])
    print(len(newList))
    return newList

greaterThanSecond([1,6,3,11,4,2,7])

# 5
def lengthAndValue(x,y):
    newList = []
    for i in range(0,x):
        newList.append(y)
    print(newList)
lengthAndValue(4,7)

