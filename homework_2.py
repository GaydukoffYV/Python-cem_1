def inputNum(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a

def checkPred(x):
    l = not (x[0] or x[1] or x[2])
    r = not x[0] and not x[1] and not x[2]
    result = l == r
    return result

statement = inputNum(3)

if checkPred(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")