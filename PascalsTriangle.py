def generate(numRows):
    myList = [[1]]
    for i in range(numRows - 1):
        prevRow = [0] + myList[-1] + [0]
        row = []
        for j in range(len(myList[-1]) + 1):
            row.append(prevRow[j] + prevRow[j + 1])
        myList.append(row)
    return myList


print(generate(1))
