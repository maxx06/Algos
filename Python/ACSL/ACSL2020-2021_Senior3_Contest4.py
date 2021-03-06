#ACSL2020-2021_Senior3_Contest4
#April 2021
#Max Xiong

def combineNums(numsThatWork, edges) -> list[int]:
    x, numsThatWork = numsThatWork, []
    for i in x:
        for j in edges:
            if str(i)[-1] == str(j)[0] and len(list(str(i)[:-1] + j)) == len(list(set(str(i)[:-1] + j))):
                numsThatWork.append(str(i)[:-1] + j)
    for s in numsThatWork:
        numsThatWork[numsThatWork.index(s)] = int(s)
    return sorted(list(set(numsThatWork)))

def sumPathsOfLengthN(num, edges) -> int:
    edge, numsThatWork = edges.split(), edges.split()
    for i in range(num - 1):
        numsThatWork = combineNums(numsThatWork, edge)
    return sum(numsThatWork)
