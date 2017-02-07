newArray = []
x = [10,2,4,-52, 23, 34 , -3, 23, -5]
x.sort()
for element in x:
    if element < 0:
        newArray.append(element)
        x.pop(0)
print newArray
