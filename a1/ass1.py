x = [[1,2,3,4],[4,5,6,6]]
y = []
for index in range(0, len(x)):
    for items in x[index]:
        y.append(items)
print(y)