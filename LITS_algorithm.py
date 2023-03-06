import copy


# Normal difficulty 6x6 puzzle (puzzle code: 12,315,755)

'''rowMatrix = [[["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled", "unfilled"]]]

columnMatrix = [[["unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled", "unfilled"]],
[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"]],
[["unfilled", "unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled"]]]'''


# Normal difficulty 8x8 puzzle (puzzle code: 11,699,370)

'''rowMatrix = [[["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]], 
[["unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled"]], 
[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled"]], 
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled"]], 
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled"]], 
[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"]]]

columnMatrix = [[["unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"]],
[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]], 
[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]], 
[["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]], 
[["unfilled", "unfilled", "unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"]]]'''


# Hard difficulty 10x10 puzzle (puzzle code: 15,323,301)


rowMatrix = [[["unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled", "unfilled"]],
[["unfilled", "unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled"]]]

columnMatrix = [[["unfilled", "unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled"], ["unfilled"], ["unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"]]]



rowBlockLengths = []

columnBlockLengths = []

for row in rowMatrix:
    newLengths = []
    for block in row:
        newLengths.append(len(block))
    rowBlockLengths.append(newLengths)

for column in columnMatrix:
    newLengths = []
    for block in column:
        newLengths.append(len(block))
    columnBlockLengths.append(newLengths)

def rowToColumn(rowIndex, rowBlockIndex, blockItemIndex):
    columnIndex = sum(rowBlockLengths[rowIndex][0: rowBlockIndex]) + blockItemIndex
    columnItem = rowIndex + 1
    totalSum = 0
    columnBlockIndex = 0
    for blockLength in columnBlockLengths[columnIndex]:
        if (blockLength + totalSum) < columnItem:
            totalSum = totalSum + blockLength
        elif (blockLength + totalSum) == columnItem:
            columnBlockItemIndex = blockLength - 1
            break
        else:
            columnBlockItemIndex = columnItem - totalSum - 1
            break
        columnBlockIndex = columnBlockIndex + 1
    return [columnIndex, columnBlockIndex, columnBlockItemIndex]

def columnToRow(columnIndex, columnBlockIndex, blockItemIndex):
    rowIndex = sum(columnBlockLengths[columnIndex][0: columnBlockIndex]) + blockItemIndex
    rowItem = columnIndex + 1
    totalSum = 0
    rowBlockIndex = 0
    for blockLength in rowBlockLengths[rowIndex]:
        if (blockLength + totalSum) < rowItem:
            totalSum = totalSum + blockLength
        elif (blockLength + totalSum) == rowItem:
            rowBlockItemIndex = blockLength - 1
            break
        else:
            rowBlockItemIndex = rowItem - totalSum - 1
            break
        rowBlockIndex = rowBlockIndex + 1
    return [rowIndex, rowBlockIndex, rowBlockItemIndex]


blockNumberIDs = []

blockNumberIDSquares = []

completeBlocks = []



blockMatrix = copy.deepcopy(rowMatrix)
blockNumberID = 1
rowIndex = 0
for row in rowMatrix:
    blockIndex = 0
    for block in row:
        blockItemIndex = 0
        for blockItem in block:
            if blockItemIndex == 0:
                columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                if columnIndices[2] != 0:
                    rowIndices = columnToRow(columnIndices[0], columnIndices[1], columnIndices[2] - 1)
                    blockMatrix[rowIndex][blockIndex][blockItemIndex] = blockMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]]
                    blockIDIndex = blockNumberIDs.index(blockMatrix[rowIndex][blockIndex][blockItemIndex])
                    blockNumberIDSquares[blockIDIndex].append([rowIndex, blockIndex, blockItemIndex])
                else:
                    blockMatrix[rowIndex][blockIndex][blockItemIndex] = str(blockNumberID)
                    blockNumberIDs.append(str(blockNumberID))
                    blockNumberIDSquares.append([])
                    blockNumberIDSquares[-1].append([rowIndex, blockIndex, blockItemIndex])
                    blockNumberID = blockNumberID + 1
            else:
                columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                if columnIndices[2] != 0:
                    rowIndices = columnToRow(columnIndices[0], columnIndices[1], columnIndices[2] - 1)
                    blockMatrix[rowIndex][blockIndex][blockItemIndex] = blockMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]]
                    blockIDIndex = blockNumberIDs.index(blockMatrix[rowIndex][blockIndex][blockItemIndex])
                    blockNumberIDSquares[blockIDIndex].append([rowIndex, blockIndex, blockItemIndex])
                    if int(blockMatrix[rowIndex][blockIndex][0]) > int(blockMatrix[rowIndex][blockIndex][blockItemIndex]):
                        secondBlockIDIndex = blockNumberIDs.index(blockMatrix[rowIndex][blockIndex][0])
                        for squareIndex in blockNumberIDSquares[secondBlockIDIndex]:
                            blockMatrix[squareIndex[0]][squareIndex[1]][squareIndex[2]] = blockNumberIDs[blockIDIndex]
                        blockNumberIDSquares[blockIDIndex] = blockNumberIDSquares[blockIDIndex] + blockNumberIDSquares[secondBlockIDIndex]
                        blockNumberIDs.pop(secondBlockIDIndex)
                        blockNumberIDSquares.pop(secondBlockIDIndex)
                    elif int(blockMatrix[rowIndex][blockIndex][0]) < int(blockMatrix[rowIndex][blockIndex][blockItemIndex]):
                        blockIDIndex = blockNumberIDs.index(blockMatrix[rowIndex][blockIndex][0]) 
                        secondBlockIDIndex = blockNumberIDs.index(blockMatrix[rowIndex][blockIndex][blockItemIndex]) 
                        for squareIndex in blockNumberIDSquares[secondBlockIDIndex]:
                            blockMatrix[squareIndex[0]][squareIndex[1]][squareIndex[2]] = blockNumberIDs[blockIDIndex]
                        blockNumberIDSquares[blockIDIndex] = blockNumberIDSquares[blockIDIndex] + blockNumberIDSquares[secondBlockIDIndex]
                        blockNumberIDs.pop(secondBlockIDIndex)
                        blockNumberIDSquares.pop(secondBlockIDIndex)
                else:
                    blockMatrix[rowIndex][blockIndex][blockItemIndex] = blockMatrix[rowIndex][blockIndex][blockItemIndex - 1]
                    blockIDIndex = blockNumberIDs.index(blockMatrix[rowIndex][blockIndex][blockItemIndex])
                    blockNumberIDSquares[blockIDIndex].append([rowIndex, blockIndex, blockItemIndex])
            blockItemIndex = blockItemIndex + 1
        blockIndex = blockIndex + 1
    rowIndex = rowIndex + 1




topLeftSquares = [0] * len(blockNumberIDs)

columnIndex = 0
for column in columnMatrix:
    blockIndex = 0
    for block in column:
        rowIndices = columnToRow(columnIndex, blockIndex, 0)
        blockIDIndex = blockNumberIDs.index(blockMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]])
        if topLeftSquares[blockIDIndex] == 0:
            topLeftSquares[blockIDIndex] = rowIndices
        blockIndex = blockIndex + 1
    columnIndex = columnIndex + 1



def findShape(blockNumberID, squareList=[]):
    squareColumnList = []
    if squareList != []:
        for square in squareList:
            squareColumnList.append(rowToColumn(square[0], square[1], square[2]))
    topLeftSquareRowIndex = topLeftSquares[blockNumberIDs.index(blockNumberID)]
    topLeftSquareIndex = rowToColumn(topLeftSquareRowIndex[0], topLeftSquareRowIndex[1], topLeftSquareRowIndex[2])
    columnIndex = topLeftSquareIndex[0]
    filledFound = False
    for blockItemIndex in range(topLeftSquareIndex[2], len(columnMatrix[columnIndex][topLeftSquareIndex[1]])):
        rowIndices = columnToRow(columnIndex, topLeftSquareIndex[1], blockItemIndex)
        if columnMatrix[columnIndex][topLeftSquareIndex[1]][blockItemIndex] == "filled" or [rowIndices[0], rowIndices[1], rowIndices[2]] in squareList:
            filledFound = True
            firstFilledSquareIndex = [columnIndex, topLeftSquareIndex[1], blockItemIndex]
            break
    if topLeftSquareIndex[1] != len(columnMatrix[columnIndex]) - 1 and filledFound == False:
        shouldBreak = False
        for blockIndex in range(topLeftSquareIndex[1] + 1, len(columnMatrix[columnIndex])):
            rowIndices = columnToRow(columnIndex, blockIndex, 0)
            if blockMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == blockNumberID:
                for blockItemIndex in range(0, len(columnMatrix[columnIndex][blockIndex])):
                    rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)
                    if columnMatrix[columnIndex][blockIndex][blockItemIndex] == "filled" or [rowIndices[0], rowIndices[1], rowIndices[2]] in squareList:
                        filledFound = True
                        firstFilledSquareIndex = [columnIndex, blockIndex, blockItemIndex]
                        break
                if shouldBreak == True:
                    break
    if filledFound == False:
        columnIndex = columnIndex + 1
        while filledFound == False:
            for blockIndex in range(0, len(columnMatrix[columnIndex])):
                rowIndices = columnToRow(columnIndex, blockIndex, 0)
                if blockMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == blockNumberID:
                    for blockItemIndex in range(0, len(columnMatrix[columnIndex][blockIndex])):
                        rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)               #might be unnecessary
                        if rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "filled" or [rowIndices[0], rowIndices[1], rowIndices[2]] in squareList:
                            filledFound = True
                            firstFilledSquareIndex = [columnIndex, blockIndex, blockItemIndex]
                            break
                    if filledFound == True:
                        break                               
            if filledFound == True:
                break
            columnIndex = columnIndex + 1
    numberTurns = 0
    numberSquares = 1
    firstFilledSquareRowIndex = columnToRow(firstFilledSquareIndex[0], firstFilledSquareIndex[1], firstFilledSquareIndex[2])
    if columnMatrix[firstFilledSquareIndex[0]][firstFilledSquareIndex[1]].count("filled") == 4 or rowMatrix[firstFilledSquareRowIndex[0]][firstFilledSquareRowIndex[1]].count("filled") == 4:
        return "I"
    if squareList != [] and len(squareList) == 4:
        if (squareColumnList[0][0] == squareColumnList[1][0] == squareColumnList[2][0] == squareColumnList[3][0]) or (squareList[0][0] == squareList[1][0] == squareList[2][0] == squareList[3][0]):
            return "I"
    firstIteration = True
    iterationNumber = 1
    shapeFound = False
    eitherLorT = False
    while shapeFound == False:
        filledSquareIndex = firstFilledSquareIndex
        filledSquareRowIndex = firstFilledSquareRowIndex
        if firstIteration == False:
            filledFound = False
            for blockIndex in range(0, len(columnMatrix[columnIndex])):
                rowIndices = columnToRow(columnIndex, blockIndex, 0)
                if blockMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == blockNumberID:
                    for blockItemIndex in range(0, len(columnMatrix[columnIndex][blockIndex])):
                        rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)             
                        if rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "filled" or [rowIndices[0], rowIndices[1], rowIndices[2]] in squareList:
                            filledFound = True
                            filledSquareIndex = [columnIndex, blockIndex, blockItemIndex]
                            filledSquareRowIndex = [rowIndices[0], rowIndices[1], rowIndices[2]]
                            break
                    if filledFound == True:
                        break  
            if filledSquareRowIndex[2] != 0:
                if firstFilledSquareRowIndex == [filledSquareRowIndex[0], filledSquareRowIndex[1], filledSquareRowIndex[2] - 1]:
                    if numberSquares == 3:
                        shapeFound = True
                        return "L"
                if filledSquareRowIndex[2] != len(rowMatrix[filledSquareRowIndex[0]][filledSquareRowIndex[1]]) - 1:
                    if (rowMatrix[filledSquareRowIndex[0]][filledSquareRowIndex[1]][filledSquareRowIndex[2] + 1] == "filled" or [filledSquareRowIndex[0], filledSquareRowIndex[1], filledSquareRowIndex[2] + 1] in squareList) and (rowMatrix[filledSquareRowIndex[0]][filledSquareRowIndex[1]][filledSquareRowIndex[2] - 1] == "filled" or [filledSquareRowIndex[0], filledSquareRowIndex[1], filledSquareRowIndex[2] - 1] in squareList):
                        if filledSquareIndex[2] != len(columnMatrix[filledSquareIndex[0]][filledSquareIndex[1]]) - 1:
                            if (columnMatrix[filledSquareIndex[0]][filledSquareIndex[1]][filledSquareIndex[2] + 1] == "filled") or ([filledSquareIndex[0], filledSquareIndex[1], filledSquareIndex[2] + 1] in squareColumnList):
                                shapeFound = True
                                return "T"
                        if shapeFound == False:
                            shapeFound = True
                            return "L"
                if [filledSquareRowIndex[0], filledSquareRowIndex[1], filledSquareRowIndex[2] - 1] != firstFilledSquareRowIndex:
                    numberTurns = numberTurns + 1
            if filledSquareIndex[2] < len(columnMatrix[filledSquareIndex[0]][filledSquareIndex[1]]) - 2:
                if (columnMatrix[filledSquareIndex[0]][filledSquareIndex[1]][filledSquareIndex[2] + 1] == "filled" or [filledSquareIndex[0], filledSquareIndex[1], filledSquareIndex[2] + 1] in squareColumnList) and (columnMatrix[filledSquareIndex[0]][filledSquareIndex[1]][filledSquareIndex[2] + 2] == "filled" or [filledSquareIndex[0], filledSquareIndex[1], filledSquareIndex[2] + 2] in squareColumnList):
                    shapeFound = True
                    eitherLorT = True
        for blockItemIndex in range(filledSquareIndex[2], len(columnMatrix[filledSquareIndex[0]][filledSquareIndex[1]])):
            rowIndices = columnToRow(filledSquareIndex[0], filledSquareIndex[1], blockItemIndex)
            if (rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "unfilled" or rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "x") and [rowIndices[0], rowIndices[1], rowIndices[2]] not in squareList:
                numberSquares = numberSquares - 1
            if firstIteration == False and blockItemIndex == filledSquareIndex[2]:
                numberTurns = numberTurns + 1
            numberAdjacent = 0
            if blockItemIndex != 0:
                if columnMatrix[filledSquareIndex[0]][filledSquareIndex[1]][blockItemIndex - 1] == "filled" or [filledSquareIndex[0], filledSquareIndex[1], blockItemIndex - 1] in squareColumnList:
                    numberAdjacent = numberAdjacent + 1
            if blockItemIndex != len(columnMatrix[filledSquareIndex[0]][filledSquareIndex[1]]) - 1:
                if columnMatrix[filledSquareIndex[0]][filledSquareIndex[1]][blockItemIndex + 1] == "filled" or [filledSquareIndex[0], filledSquareIndex[1], blockItemIndex + 1] in squareColumnList:
                    numberAdjacent = numberAdjacent + 1
            if rowIndices[2] != 0:
                if rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2] - 1] == "filled" or [rowIndices[0], rowIndices[1], rowIndices[2] - 1] in squareList:
                    numberAdjacent = numberAdjacent + 1
            if rowIndices[2] != len(rowMatrix[rowIndices[0]][rowIndices[1]]) - 1:
                if rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2] + 1] == "filled" or [rowIndices[0], rowIndices[1], rowIndices[2] + 1] in squareList:
                    numberAdjacent = numberAdjacent + 1
            if numberAdjacent == 3:
                shapeFound = True
                return "T"
            if firstIteration == True and numberSquares == 3 and numberAdjacent == 2:
                shapeFound = True
                return "L"
            if numberSquares == 4 and numberTurns == 1:
                shapeFound = True
                return "L"
            if eitherLorT == True and numberSquares == 4:
                shapeFound = True
                return "L"
            numberSquares = numberSquares + 1
        if firstIteration == True:
            firstIteration = False
        columnIndex = columnIndex + 1
        iterationNumber = iterationNumber + 1
        if iterationNumber == 3:
            shapeFound = True
            return "S" 

                

def adjacentBlocks(inputSquareIndices, squaresToFill=[], filled=False):
    adjacentBlockIDs = []
    mainBlockID = blockMatrix[inputSquareIndices[0][0]][inputSquareIndices[0][1]][inputSquareIndices[0][2]]
    for inputSquareIndex in inputSquareIndices:
        if not (inputSquareIndex[2] == 0 and inputSquareIndex[1] == 0):
            if inputSquareIndex[2] == 0:
                leftBlockIndex = [inputSquareIndex[0], inputSquareIndex[1] - 1, len(rowMatrix[inputSquareIndex[0]][inputSquareIndex[1] - 1]) - 1]
                leftBlockID = blockMatrix[leftBlockIndex[0]][leftBlockIndex[1]][leftBlockIndex[2]]
                if leftBlockID not in adjacentBlockIDs:
                    if not (filled == True and (rowMatrix[leftBlockIndex[0]][leftBlockIndex[1]][leftBlockIndex[2]] != "filled" and [leftBlockIndex[0], leftBlockIndex[1], leftBlockIndex[2]] not in squaresToFill)):
                        adjacentBlockIDs.append(leftBlockID)
        if not (inputSquareIndex[2] == len(rowMatrix[inputSquareIndex[0]][len(rowMatrix[inputSquareIndex[0]]) - 1]) - 1 and inputSquareIndex[1] == len(rowMatrix[inputSquareIndex[0]]) - 1):
            if inputSquareIndex[2] == len(rowMatrix[inputSquareIndex[0]][inputSquareIndex[1]]) - 1:
                rightBlockIndex = [inputSquareIndex[0], inputSquareIndex[1] + 1, 0]
                rightBlockID = blockMatrix[rightBlockIndex[0]][rightBlockIndex[1]][rightBlockIndex[2]]
                if rightBlockID not in adjacentBlockIDs:
                    if not (filled == True and (rowMatrix[rightBlockIndex[0]][rightBlockIndex[1]][rightBlockIndex[2]] != "filled" and [rightBlockIndex[0], rightBlockIndex[1], rightBlockIndex[2]] not in squaresToFill)):
                        adjacentBlockIDs.append(rightBlockID)
        columnIndices = rowToColumn(inputSquareIndex[0], inputSquareIndex[1], inputSquareIndex[2])
        if inputSquareIndex[0] != 0:
            if columnIndices[2] == 0:
                topBlockColumnIndex = [columnIndices[0], columnIndices[1] - 1, len(columnMatrix[columnIndices[0]][columnIndices[1] - 1]) - 1]
                topBlockIndex = columnToRow(topBlockColumnIndex[0], topBlockColumnIndex[1], topBlockColumnIndex[2])
                topBlockID = blockMatrix[topBlockIndex[0]][topBlockIndex[1]][topBlockIndex[2]]
                if topBlockID not in adjacentBlockIDs:
                    if not (filled == True and (rowMatrix[topBlockIndex[0]][topBlockIndex[1]][topBlockIndex[2]] != "filled" and [topBlockIndex[0], topBlockIndex[1], topBlockIndex[2]] not in squaresToFill)):
                        adjacentBlockIDs.append(topBlockID)
        if inputSquareIndex[0] != len(rowMatrix) - 1:
            if columnIndices[2] == len(columnMatrix[columnIndices[0]][columnIndices[1]]) - 1:
                bottomBlockColumnIndex = [columnIndices[0], columnIndices[1] + 1, 0]
                bottomBlockIndex = columnToRow(bottomBlockColumnIndex[0], bottomBlockColumnIndex[1], bottomBlockColumnIndex[2])
                bottomBlockID = blockMatrix[bottomBlockIndex[0]][bottomBlockIndex[1]][bottomBlockIndex[2]]
                if bottomBlockID not in adjacentBlockIDs:
                    if not (filled == True and (rowMatrix[bottomBlockIndex[0]][bottomBlockIndex[1]][bottomBlockIndex[2]] != "filled" and [bottomBlockIndex[0], bottomBlockIndex[1], bottomBlockIndex[2]] not in squaresToFill)):
                        adjacentBlockIDs.append(bottomBlockID)
    return adjacentBlockIDs


def twoByTwoCheck (inputSquareIndices, squaresToFillList=[]):
    answer = [0] * len(inputSquareIndices)
    index = 0
    for inputSquareIndex in inputSquareIndices:
        columnIndices = rowToColumn(inputSquareIndex[0], inputSquareIndex[1], inputSquareIndex[2])
        if inputSquareIndex[0] != 0:
            if columnIndices[2] == 0:
                topBlockColumnIndex = [columnIndices[0], columnIndices[1] - 1, len(columnMatrix[columnIndices[0]][columnIndices[1] - 1]) - 1]
            else:
                topBlockColumnIndex = [columnIndices[0], columnIndices[1], columnIndices[2] - 1]
            topBlockIndex = columnToRow(topBlockColumnIndex[0], topBlockColumnIndex[1], topBlockColumnIndex[2])
            if (rowMatrix[topBlockIndex[0]][topBlockIndex[1]][topBlockIndex[2]] == "filled") or ([topBlockIndex[0], topBlockIndex[1], topBlockIndex[2]] in squaresToFillList) or ([topBlockIndex[0], topBlockIndex[1], topBlockIndex[2]] in inputSquareIndices): 
                if not (inputSquareIndex[2] == 0 and inputSquareIndex[1] == 0):
                    if inputSquareIndex[2] == 0:
                        leftBlockIndex = [inputSquareIndex[0], inputSquareIndex[1] - 1, len(rowMatrix[inputSquareIndex[0]][inputSquareIndex[1] - 1]) - 1]
                    else:
                        leftBlockIndex = [inputSquareIndex[0], inputSquareIndex[1], inputSquareIndex[2] - 1]
                    if (rowMatrix[leftBlockIndex[0]][leftBlockIndex[1]][leftBlockIndex[2]] == "filled") or ([leftBlockIndex[0], leftBlockIndex[1], leftBlockIndex[2]] in squaresToFillList) or ([leftBlockIndex[0], leftBlockIndex[1], leftBlockIndex[2]] in inputSquareIndices):
                        columnIndices = rowToColumn(leftBlockIndex[0], leftBlockIndex[1], leftBlockIndex[2])
                        if columnIndices[2] == 0:
                            topLeftBlockColumnIndex = [columnIndices[0], columnIndices[1] - 1, len(columnMatrix[columnIndices[0]][columnIndices[1] - 1]) - 1]
                        else:
                            topLeftBlockColumnIndex = [columnIndices[0], columnIndices[1], columnIndices[2] - 1]
                        topLeftBlockIndex = columnToRow(topLeftBlockColumnIndex[0], topLeftBlockColumnIndex[1], topLeftBlockColumnIndex[2])
                        if (rowMatrix[topLeftBlockIndex[0]][topLeftBlockIndex[1]][topLeftBlockIndex[2]] == "filled") or ([topLeftBlockIndex[0], topLeftBlockIndex[1], topLeftBlockIndex[2]]) in squaresToFillList or ([topLeftBlockIndex[0], topLeftBlockIndex[1], topLeftBlockIndex[2]] in inputSquareIndices):
                            answer[index] = True
                if not (inputSquareIndex[2] == len(rowMatrix[inputSquareIndex[0]][len(rowMatrix[inputSquareIndex[0]]) - 1]) - 1 and inputSquareIndex[1] == len(rowMatrix[inputSquareIndex[0]]) - 1):
                    if inputSquareIndex[2] == len(rowMatrix[inputSquareIndex[0]][inputSquareIndex[1]]) - 1:
                        rightBlockIndex = [inputSquareIndex[0], inputSquareIndex[1] + 1, 0]
                    else:
                        rightBlockIndex = [inputSquareIndex[0], inputSquareIndex[1], inputSquareIndex[2] + 1]
                    if (rowMatrix[rightBlockIndex[0]][rightBlockIndex[1]][rightBlockIndex[2]] == "filled") or ([rightBlockIndex[0], rightBlockIndex[1], rightBlockIndex[2]] in squaresToFillList) or ([rightBlockIndex[0], rightBlockIndex[1], rightBlockIndex[2]] in inputSquareIndices):
                        columnIndices = rowToColumn(rightBlockIndex[0], rightBlockIndex[1], rightBlockIndex[2])
                        if columnIndices[2] == 0:
                            topRightBlockColumnIndex = [columnIndices[0], columnIndices[1] - 1, len(columnMatrix[columnIndices[0]][columnIndices[1] - 1]) - 1]
                        else:
                            topRightBlockColumnIndex = [columnIndices[0], columnIndices[1], columnIndices[2] - 1]
                        topRightBlockIndex = columnToRow(topRightBlockColumnIndex[0], topRightBlockColumnIndex[1], topRightBlockColumnIndex[2])
                        if (rowMatrix[topRightBlockIndex[0]][topRightBlockIndex[1]][topRightBlockIndex[2]] == "filled") or ([topRightBlockIndex[0], topRightBlockIndex[1], topRightBlockIndex[2]] in squaresToFillList) or ([topRightBlockIndex[0], topRightBlockIndex[1], topRightBlockIndex[2]] in inputSquareIndices):
                            answer[index] = True
        columnIndices = rowToColumn(inputSquareIndex[0], inputSquareIndex[1], inputSquareIndex[2])
        if inputSquareIndex[0] != len(rowMatrix) - 1:
            if columnIndices[2] == len(columnMatrix[columnIndices[0]][columnIndices[1]]) - 1:
                bottomBlockColumnIndex = [columnIndices[0], columnIndices[1] + 1, 0]
            else:
                bottomBlockColumnIndex = [columnIndices[0], columnIndices[1], columnIndices[2] + 1]
            bottomBlockIndex = columnToRow(bottomBlockColumnIndex[0], bottomBlockColumnIndex[1], bottomBlockColumnIndex[2])
            if (rowMatrix[bottomBlockIndex[0]][bottomBlockIndex[1]][bottomBlockIndex[2]] == "filled") or ([bottomBlockIndex[0], bottomBlockIndex[1], bottomBlockIndex[2]] in squaresToFillList) or ([bottomBlockIndex[0], bottomBlockIndex[1], bottomBlockIndex[2]] in inputSquareIndices):
                if not (inputSquareIndex[2] == 0 and inputSquareIndex[1] == 0):
                    if inputSquareIndex[2] == 0:
                        leftBlockIndex = [inputSquareIndex[0], inputSquareIndex[1] - 1, len(rowMatrix[inputSquareIndex[0]][inputSquareIndex[1] - 1]) - 1]
                    else:
                        leftBlockIndex = [inputSquareIndex[0], inputSquareIndex[1], inputSquareIndex[2] - 1]
                    if (rowMatrix[leftBlockIndex[0]][leftBlockIndex[1]][leftBlockIndex[2]] == "filled") or ([leftBlockIndex[0], leftBlockIndex[1], leftBlockIndex[2]] in squaresToFillList) or ([leftBlockIndex[0], leftBlockIndex[1], leftBlockIndex[2]] in inputSquareIndices):
                        columnIndices = rowToColumn(leftBlockIndex[0], leftBlockIndex[1], leftBlockIndex[2])
                        if columnIndices[2] == len(columnMatrix[columnIndices[0]][columnIndices[1]]) - 1:
                            bottomLeftBlockColumnIndex = [columnIndices[0], columnIndices[1] + 1, 0]
                        else:
                            bottomLeftBlockColumnIndex = [columnIndices[0], columnIndices[1], columnIndices[2] + 1]
                        bottomLeftBlockIndex = columnToRow(bottomLeftBlockColumnIndex[0], bottomLeftBlockColumnIndex[1], bottomLeftBlockColumnIndex[2])
                        if (rowMatrix[bottomLeftBlockIndex[0]][bottomLeftBlockIndex[1]][bottomLeftBlockIndex[2]] == "filled") or ([bottomLeftBlockIndex[0], bottomLeftBlockIndex[1], bottomLeftBlockIndex[2]] in squaresToFillList) or ([bottomLeftBlockIndex[0], bottomLeftBlockIndex[1], bottomLeftBlockIndex[2]] in inputSquareIndices):
                            answer[index] = True
                if not (inputSquareIndex[2] == len(rowMatrix[inputSquareIndex[0]][len(rowMatrix[inputSquareIndex[0]]) - 1]) - 1 and inputSquareIndex[1] == len(rowMatrix[inputSquareIndex[0]]) - 1):
                    if inputSquareIndex[2] == len(rowMatrix[inputSquareIndex[0]][inputSquareIndex[1]]) - 1:
                        rightBlockIndex = [inputSquareIndex[0], inputSquareIndex[1] + 1, 0]
                    else:
                        rightBlockIndex = [inputSquareIndex[0], inputSquareIndex[1], inputSquareIndex[2] + 1]
                    if (rowMatrix[rightBlockIndex[0]][rightBlockIndex[1]][rightBlockIndex[2]] == "filled") or ([rightBlockIndex[0], rightBlockIndex[1], rightBlockIndex[2]] in squaresToFillList) or ([rightBlockIndex[0], rightBlockIndex[1], rightBlockIndex[2]] in inputSquareIndices):
                        columnIndices = rowToColumn(rightBlockIndex[0], rightBlockIndex[1], rightBlockIndex[2])
                        if columnIndices[2] == len(columnMatrix[columnIndices[0]][columnIndices[1]]) - 1:
                            bottomRightBlockColumnIndex = [columnIndices[0], columnIndices[1] + 1, 0]
                        else:
                            bottomRightBlockColumnIndex = [columnIndices[0], columnIndices[1], columnIndices[2] + 1]
                        bottomRightBlockIndex = columnToRow(bottomRightBlockColumnIndex[0], bottomRightBlockColumnIndex[1], bottomRightBlockColumnIndex[2])
                        if (rowMatrix[bottomRightBlockIndex[0]][bottomRightBlockIndex[1]][bottomRightBlockIndex[2]] == "filled") or ([bottomRightBlockIndex[0], bottomRightBlockIndex[1], bottomRightBlockIndex[2]] in squaresToFillList) or ([bottomRightBlockIndex[0], bottomRightBlockIndex[1], bottomRightBlockIndex[2]] in inputSquareIndices):
                            answer[index] = True
        if answer[index] == 0:
            answer[index] = False
        index = index + 1
    return answer


def possibleCombinations(inputBlockNumberID, adjacentBlockNumberToFill="0", adjacentSquareIndicesToFill=[]):
    topLeftSquareRowIndex = topLeftSquares[blockNumberIDs.index(inputBlockNumberID)]
    possibleCombinationsList = []
    alreadyFilled = False
    alreadyFilledSquares = []
    finished = False
    topLeftSquareColumnIndex = rowToColumn(topLeftSquareRowIndex[0], topLeftSquareRowIndex[1], topLeftSquareRowIndex[2])
    columnIndex = topLeftSquareColumnIndex[0]
    possibleCombination = []
    firstIteration = True
    crossedSquares1 = []
    crossedSquares2 = []
    crossedSquares3 = []
    crossedSquares4 = []
    startingSquareColumnIndex = topLeftSquareColumnIndex
    startingSquareRowIndex = topLeftSquareRowIndex
    index = 0
    while finished == False:
        index = index + 1
        originalPossibleCombination = copy.deepcopy(possibleCombination)
        if firstIteration == False:
            shouldBreak = False
            shouldContinue = False
            found = False
            for blockIndex in range(0, len(columnMatrix[columnIndex])):
                rowIndices = columnToRow(columnIndex, blockIndex, 0)
                if blockMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == inputBlockNumberID:
                    notCrossedYet4 = False
                    notCrossedYet3 = False
                    notCrossedYet3_0 = False
                    notCrossedYet3_0_1 = False
                    notCrossedYet3_0_2 = False
                    notCrossedYet3_1 = False
                    notCrossedYet3_2 = False
                    notCrossedYet3_2_0 = False
                    for blockItemIndex in range(0, len(columnMatrix[columnIndex][blockIndex])):
                        rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)
                        if len(possibleCombination) == 0 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares1 and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                            startingSquareRowIndex = rowIndices
                            startingSquareColumnIndex = [columnIndex, blockIndex, blockItemIndex]
                            shouldBreak = True
                            found = True
                            break
                        if len(possibleCombination) == 3:
                            if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[2] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                notCrossedYet4 = True
                                index4 = rowIndices
                                columnIndex4 = [columnIndex, blockIndex, blockItemIndex]
                                found = True
                            if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[1] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                notCrossedYet3_1 = True
                                index3_1 = rowIndices
                                columnIndex3_1 = [columnIndex, blockIndex, blockItemIndex]
                                found = True
                            if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[0] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                notCrossedYet3_0 = True
                                index3_0 = rowIndices
                                columnIndex3_0 = [columnIndex, blockIndex, blockItemIndex]
                                found = True
                            if ([columnIndex, blockIndex, blockItemIndex - 1] == rowToColumn(possibleCombination[2][0], possibleCombination[2][1], possibleCombination[2][2]) or [columnIndex, blockIndex, blockItemIndex + 1] == rowToColumn(possibleCombination[2][0], possibleCombination[2][1], possibleCombination[2][2])) and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                notCrossedYet3_0_1 = True
                                index3_0_1 = rowIndices
                                columnIndex3_0_1 = [columnIndex, blockIndex, blockItemIndex]
                                found = True
                            if ([columnIndex, blockIndex, blockItemIndex - 1] == rowToColumn(possibleCombination[1][0], possibleCombination[1][1], possibleCombination[1][2]) or [columnIndex, blockIndex, blockItemIndex + 1] == rowToColumn(possibleCombination[1][0], possibleCombination[1][1], possibleCombination[1][2])) and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                notCrossedYet3_0_2 = True
                                index3_0_2 = rowIndices
                                columnIndex3_0_2 = [columnIndex, blockIndex, blockItemIndex]
                                found = True
                        if len(possibleCombination) == 2:
                            if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[1] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                notCrossedYet3 = True
                                index3 = rowIndices
                                columnIndex3 = [columnIndex, blockIndex, blockItemIndex]
                                found = True
                            if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[0] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                notCrossedYet3_2 = True
                                index3_2 = rowIndices
                                columnIndex3_2 = [columnIndex, blockIndex, blockItemIndex]
                                found = True
                            if ([columnIndex, blockIndex, blockItemIndex - 1] == rowToColumn(possibleCombination[1][0], possibleCombination[1][1], possibleCombination[1][2]) or [columnIndex, blockIndex, blockItemIndex + 1] == rowToColumn(possibleCombination[1][0], possibleCombination[1][1], possibleCombination[1][2])) and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                notCrossedYet3_2_0 = True
                                index3_2_0 = rowIndices
                                columnIndex3_2_0 = [columnIndex, blockIndex, blockItemIndex]
                                found = True
                        if len(possibleCombination) == 1:
                            if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[0] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares2 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                startingSquareRowIndex = rowIndices
                                startingSquareColumnIndex = [columnIndex, blockIndex, blockItemIndex]
                                shouldBreak = True
                                found = True
                                break
                        if found == True:
                            break
                    if shouldBreak == True:
                        break
                    if notCrossedYet4 == True:
                        startingSquareRowIndex = index4
                        startingSquareColumnIndex = columnIndex4
                        break
                    elif notCrossedYet3_1 == True:                  
                        startingSquareRowIndex = index3_1
                        startingSquareColumnIndex = columnIndex3_1
                        break
                    elif notCrossedYet3_0 == True:                  
                        startingSquareRowIndex = index3_0
                        startingSquareColumnIndex = columnIndex3_0
                        break
                    elif notCrossedYet3_0_1 == True:                  
                        startingSquareRowIndex = index3_0_1
                        startingSquareColumnIndex = columnIndex3_0_1
                        break
                    elif notCrossedYet3_0_2 == True:                  
                        startingSquareRowIndex = index3_0_2
                        startingSquareColumnIndex = columnIndex3_0_2
                        break
                    elif notCrossedYet3 == True:
                        startingSquareRowIndex = index3
                        startingSquareColumnIndex = columnIndex3
                        break
                    elif notCrossedYet3_2 == True:
                        startingSquareRowIndex = index3_2
                        startingSquareColumnIndex = columnIndex3_2
                        break
                    elif notCrossedYet3_2_0 == True:
                        startingSquareRowIndex = index3_2_0
                        startingSquareColumnIndex = columnIndex3_2_0
                        break
            if columnIndex != len(columnMatrix) - 1 and found == False:
                columnIndex = columnIndex + 1
                for blockIndex in range(0, len(columnMatrix[columnIndex])):
                    rowIndices = columnToRow(columnIndex, blockIndex, 0)
                    if blockMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == inputBlockNumberID:
                        notCrossedYet4 = False
                        notCrossedYet3 = False
                        notCrossedYet3_0 = False
                        notCrossedYet3_0_1 = False
                        notCrossedYet3_0_2 = False
                        notCrossedYet3_1 = False
                        notCrossedYet3_2 = False
                        notCrossedYet3_2_0 = False
                        for blockItemIndex in range(0, len(columnMatrix[columnIndex][blockIndex])):
                            rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)
                            if len(possibleCombination) == 0 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares1 and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                startingSquareRowIndex = rowIndices
                                startingSquareColumnIndex = [columnIndex, blockIndex, blockItemIndex]
                                shouldBreak = True
                                found = True
                                break
                            if len(possibleCombination) == 3:
                                if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[2] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                    notCrossedYet4 = True
                                    index4 = rowIndices
                                    columnIndex4 = [columnIndex, blockIndex, blockItemIndex]
                                    found = True
                                if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[1] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                    notCrossedYet3_1 = True
                                    index3_1 = rowIndices
                                    columnIndex3_1 = [columnIndex, blockIndex, blockItemIndex]
                                    found = True
                                if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[0] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                    notCrossedYet3_0 = True
                                    index3_0 = rowIndices
                                    columnIndex3_0 = [columnIndex, blockIndex, blockItemIndex]
                                    found = True
                                if ([columnIndex, blockIndex, blockItemIndex - 1] == rowToColumn(possibleCombination[2][0], possibleCombination[2][1], possibleCombination[2][2]) or [columnIndex, blockIndex, blockItemIndex + 1] == rowToColumn(possibleCombination[2][0], possibleCombination[2][1], possibleCombination[2][2])) and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                    notCrossedYet3_0_1 = True
                                    index3_0_1 = rowIndices
                                    columnIndex3_0_1 = [columnIndex, blockIndex, blockItemIndex]
                                    found = True
                                if ([columnIndex, blockIndex, blockItemIndex - 1] == rowToColumn(possibleCombination[1][0], possibleCombination[1][1], possibleCombination[1][2]) or [columnIndex, blockIndex, blockItemIndex + 1] == rowToColumn(possibleCombination[1][0], possibleCombination[1][1], possibleCombination[1][2])) and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                    notCrossedYet3_0_2 = True
                                    index3_0_2 = rowIndices
                                    columnIndex3_0_2 = [columnIndex, blockIndex, blockItemIndex]
                                    found = True
                            if len(possibleCombination) == 2:
                                if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[1] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                    notCrossedYet3 = True
                                    index3 = rowIndices
                                    columnIndex3 = [columnIndex, blockIndex, blockItemIndex]
                                    found = True
                                if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[0] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                    notCrossedYet3_2 = True
                                    index3_2 = rowIndices
                                    columnIndex3_2 = [columnIndex, blockIndex, blockItemIndex]
                                    found = True
                                if ([columnIndex, blockIndex, blockItemIndex - 1] == rowToColumn(possibleCombination[1][0], possibleCombination[1][1], possibleCombination[1][2]) or [columnIndex, blockIndex, blockItemIndex + 1] == rowToColumn(possibleCombination[1][0], possibleCombination[1][1], possibleCombination[1][2])) and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares3 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares4 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                    notCrossedYet3_2_0 = True
                                    index3_2_0 = rowIndices
                                    columnIndex3_2_0 = [columnIndex, blockIndex, blockItemIndex]
                                    found = True
                            if len(possibleCombination) == 1:
                                if [rowIndices[0], rowIndices[1], rowIndices[2] - 1] == possibleCombination[0] and [rowIndices[0], rowIndices[1], rowIndices[2]] not in crossedSquares2 and [rowIndices[0], rowIndices[1], rowIndices[2]] not in possibleCombination and rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] != "x":
                                    startingSquareRowIndex = rowIndices
                                    startingSquareColumnIndex = [columnIndex, blockIndex, blockItemIndex]
                                    shouldBreak = True
                                    found = True
                                    break
                        if shouldBreak == True:
                            break
                        if notCrossedYet4 == True:
                            startingSquareRowIndex = index4
                            startingSquareColumnIndex = columnIndex4
                            break
                        elif notCrossedYet3_1 == True:                  
                            startingSquareRowIndex = index3_1
                            startingSquareColumnIndex = columnIndex3_1
                            break
                        elif notCrossedYet3_0 == True:                  
                            startingSquareRowIndex = index3_0
                            startingSquareColumnIndex = columnIndex3_0
                            break
                        elif notCrossedYet3_0_1 == True:                  
                            startingSquareRowIndex = index3_0_1
                            startingSquareColumnIndex = columnIndex3_0_1
                            break
                        elif notCrossedYet3_0_2 == True:                  
                            startingSquareRowIndex = index3_0_2
                            startingSquareColumnIndex = columnIndex3_0_2
                            break
                        elif notCrossedYet3 == True:
                            startingSquareRowIndex = index3
                            startingSquareColumnIndex = columnIndex3
                            break
                        elif notCrossedYet3_2 == True:
                            startingSquareRowIndex = index3_2
                            startingSquareColumnIndex = columnIndex3_2
                            break
                        elif notCrossedYet3_2_0 == True:
                            startingSquareRowIndex = index3_2_0
                            startingSquareColumnIndex = columnIndex3_2_0
                            break
            if found == False:
                if len(possibleCombination) == 3:
                    squareToRemove = possibleCombination.pop()
                    crossedSquares3.append(squareToRemove)
                    crossedSquares4 = []
                    columnIndices = rowToColumn(squareToRemove[0], squareToRemove[1], squareToRemove[2])
                    columnIndices2 = rowToColumn(possibleCombination[-1][0], possibleCombination[-1][1], possibleCombination[-1][2])
                    if columnIndices[0] == columnIndices2[0] and columnIndices[2] == columnIndices2[2] + 1:
                        if columnIndices[0] != len(columnMatrix) - 1:
                            columnIndex = columnIndices[0] + 1
                    else:
                        columnIndex = columnIndices[0]
                elif len(possibleCombination) == 2:
                    squareToRemove = possibleCombination.pop()
                    crossedSquares2.append(squareToRemove)
                    crossedSquares3 = []
                    crossedSquares4 = []
                    columnIndices = rowToColumn(squareToRemove[0], squareToRemove[1], squareToRemove[2])
                    columnIndices2 = rowToColumn(possibleCombination[-1][0], possibleCombination[-1][1], possibleCombination[-1][2])
                    if columnIndices[0] == columnIndices2[0] and columnIndices[2] == columnIndices2[2] + 1:
                        if columnIndices[0] != len(columnMatrix) - 1:
                            columnIndex = columnIndices[0] + 1
                    else:
                        columnIndex = columnIndices[0]
                elif len(possibleCombination) == 1:
                    squareToRemove = possibleCombination.pop()
                    crossedSquares1.append(squareToRemove)
                    crossedSquares2 = []
                    crossedSquares3 = []
                    crossedSquares4 = []
                    columnIndices = rowToColumn(squareToRemove[0], squareToRemove[1], squareToRemove[2])
                    columnIndex = columnIndices[0]
                elif (len(possibleCombination)) == 0:
                    if columnIndex != len(columnMatrix) - 1:
                        columnIndex = columnIndex + 1
                    else:
                        finished = True
                        return possibleCombinationsList
                shouldContinue = True
            if shouldContinue == True:
                continue
        for blockItemIndex in range(startingSquareColumnIndex[2], -1, -1):
            rowIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex)
            nextColumnIndices = 0
            previousColumnIndices = 0
            if rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "unfilled":
                if len(possibleCombination) == 0:
                    if rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                        possibleCombination.append(rowIndices)
                elif len(possibleCombination) == 1:
                    if rowIndices not in crossedSquares2 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                        if blockItemIndex != len(columnMatrix[startingSquareColumnIndex[0]][startingSquareColumnIndex[1]]) - 1:
                            nextColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex + 1)
                        if blockItemIndex != 0:
                            previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1) 
                        if (nextColumnIndices in possibleCombination) or (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                            possibleCombination.append(rowIndices)
                elif len(possibleCombination) == 2:
                    if rowIndices not in crossedSquares3 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                        if blockItemIndex != len(columnMatrix[startingSquareColumnIndex[0]][startingSquareColumnIndex[1]]) - 1:
                            nextColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex + 1) 
                        if blockItemIndex != 0:
                            previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1)
                        if (nextColumnIndices in possibleCombination) or (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                            possibleCombination.append(rowIndices)
                elif len(possibleCombination) == 3:
                    if rowIndices not in crossedSquares4 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                        if blockItemIndex != len(columnMatrix[startingSquareColumnIndex[0]][startingSquareColumnIndex[1]]) - 1:
                            nextColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex + 1) 
                        if blockItemIndex != 0:
                            previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1)
                        if (nextColumnIndices in possibleCombination) or (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                            possibleCombination.append(rowIndices)
            if rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "filled":
                if alreadyFilled == False:                                         
                    alreadyFilled = True
                if rowIndices not in alreadyFilledSquares:
                    possibleCombinationsList = []
                    alreadyFilledSquares.append(rowIndices)
                if len(possibleCombination) == 0:
                        if rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                            possibleCombination.append(rowIndices)
                elif len(possibleCombination) == 1:
                    if rowIndices not in crossedSquares2 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                        if blockItemIndex != len(columnMatrix[startingSquareColumnIndex[0]][startingSquareColumnIndex[1]]) - 1:
                            nextColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex + 1) 
                        if blockItemIndex != 0:
                            previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1) 
                        if (nextColumnIndices in possibleCombination) or (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                            possibleCombination.append(rowIndices)
                elif len(possibleCombination) == 2:
                    if rowIndices not in crossedSquares3 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                        if blockItemIndex != len(columnMatrix[startingSquareColumnIndex[0]][startingSquareColumnIndex[1]]) - 1:
                            nextColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex + 1) 
                        if blockItemIndex != 0:
                            previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1) 
                        if (nextColumnIndices in possibleCombination) or (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                            possibleCombination.append(rowIndices)
                elif len(possibleCombination) == 3:
                    if rowIndices not in crossedSquares4 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                        if blockItemIndex != len(columnMatrix[startingSquareColumnIndex[0]][startingSquareColumnIndex[1]]) - 1:
                            nextColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex + 1) 
                        if blockItemIndex != 0:  
                            previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1) 
                        if (nextColumnIndices in possibleCombination) or (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                            possibleCombination.append(rowIndices)
            if len(possibleCombination) == 4:
                break
        if startingSquareColumnIndex[2] != len(columnMatrix[startingSquareColumnIndex[0]][startingSquareColumnIndex[1]]) - 1 and len(possibleCombination) < 4:
            for blockItemIndex in range(startingSquareColumnIndex[2] + 1, len(columnMatrix[startingSquareColumnIndex[0]][startingSquareColumnIndex[1]])):
                rowIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex)
                previousColumnIndices = 0
                if rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "unfilled":
                    if len(possibleCombination) == 0:
                        if rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                            possibleCombination.append(rowIndices)
                    elif len(possibleCombination) == 1:
                        if rowIndices not in crossedSquares2 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                            if blockItemIndex != 0:
                                previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1) 
                            if (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                                possibleCombination.append(rowIndices)
                    elif len(possibleCombination) == 2:
                        if rowIndices not in crossedSquares3 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                            if blockItemIndex != 0:
                                previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1) 
                            if (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                                possibleCombination.append(rowIndices)
                    elif len(possibleCombination) == 3:
                        if rowIndices not in crossedSquares4 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                            if blockItemIndex != 0:   #stopped here
                                previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1) 
                            if (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                                possibleCombination.append(rowIndices)
                if rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "filled":
                    if alreadyFilled == False:
                        alreadyFilled = True
                    if rowIndices not in alreadyFilledSquares:
                        possibleCombinationsList = []
                        alreadyFilledSquares.append(rowIndices)
                    if len(possibleCombination) == 0:
                        if rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                            possibleCombination.append(rowIndices)
                    elif len(possibleCombination) == 1:
                        if rowIndices not in crossedSquares2 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                            if blockItemIndex != 0:
                                previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1) 
                            if (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                                possibleCombination.append(rowIndices)
                    elif len(possibleCombination) == 2:
                        if rowIndices not in crossedSquares3 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                            if blockItemIndex != 0:
                                previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1) 
                            if (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                                possibleCombination.append(rowIndices)
                    elif len(possibleCombination) == 3:
                        if rowIndices not in crossedSquares4 and rowIndices not in crossedSquares1 and rowIndices not in possibleCombination:
                            if blockItemIndex != 0:   #stopped here
                                previousColumnIndices = columnToRow(startingSquareColumnIndex[0], startingSquareColumnIndex[1], blockItemIndex - 1) 
                            if (previousColumnIndices in possibleCombination) or ([rowIndices[0], rowIndices[1], rowIndices[2] - 1] in possibleCombination):
                                possibleCombination.append(rowIndices)
                if len(possibleCombination) == 4:
                    break
        if len(possibleCombination) == 4:
            possibleCombinationShape = findShape(inputBlockNumberID, possibleCombination)
            if adjacentSquareIndicesToFill != []:
                adjacentBlockIDList = adjacentBlocks(possibleCombination, adjacentSquareIndicesToFill, True)
            else:
                adjacentBlockIDList = adjacentBlocks(possibleCombination, [], True)
            matchedShape = False
            for blockNumberID in adjacentBlockIDList:
                adjacentShape = 0
                if blockNumberID != adjacentBlockNumberToFill:
                    if blockNumberID in completeBlocks:
                        adjacentShape = findShape(blockNumberID)
                else:
                    adjacentShape = findShape(adjacentBlockNumberToFill, adjacentSquareIndicesToFill)
                if possibleCombinationShape == adjacentShape:
                    matchedShape = True
            if adjacentSquareIndicesToFill != []:
                twoByTwo = twoByTwoCheck(possibleCombination, adjacentSquareIndicesToFill)
            else:
                twoByTwo = twoByTwoCheck(possibleCombination)
            containsFilledSquares = True 
            if alreadyFilledSquares != []:
                for alreadyFilledSquare in alreadyFilledSquares:
                    if alreadyFilledSquare not in possibleCombination:
                        containsFilledSquares = False
            if True not in twoByTwo and matchedShape == False and containsFilledSquares == True:
                itemToAppend = copy.deepcopy(possibleCombination)
                possibleCombinationsList.append(itemToAppend)
            squareToRemove = possibleCombination.pop()
            crossedSquares4.append(squareToRemove)
            columnIndices = rowToColumn(squareToRemove[0], squareToRemove[1], squareToRemove[2])
            columnIndices2 = rowToColumn(possibleCombination[-1][0], possibleCombination[-1][1], possibleCombination[-1][2])
            if columnIndices[0] == columnIndices2[0] and columnIndices[2] == columnIndices2[2] + 1:
                if columnIndices[0] != len(columnMatrix) - 1:
                        columnIndex = columnIndices[0] + 1
            else:
                columnIndex = columnIndices[0]
            continue
        elif possibleCombination == originalPossibleCombination:
            if len(possibleCombination) == 3:
                squareToRemove = possibleCombination.pop()
                crossedSquares3.append(squareToRemove)
                crossedSquares4 = []
                columnIndices = rowToColumn(squareToRemove[0], squareToRemove[1], squareToRemove[2])
                columnIndices2 = rowToColumn(possibleCombination[-1][0], possibleCombination[-1][1], possibleCombination[-1][2])
                if columnIndices[0] == columnIndices2[0] and columnIndices[2] == columnIndices2[2] + 1:
                    if columnIndices[0] != len(columnMatrix) - 1:
                        columnIndex = columnIndices[0] + 1
                else:
                    columnIndex = columnIndices[0]
            elif len(possibleCombination) == 2:
                squareToRemove = possibleCombination.pop()
                crossedSquares2.append(squareToRemove)
                crossedSquares3 = []
                crossedSquares4 = []
                columnIndices = rowToColumn(squareToRemove[0], squareToRemove[1], squareToRemove[2])
                columnIndices2 = rowToColumn(possibleCombination[-1][0], possibleCombination[-1][1], possibleCombination[-1][2])
                if columnIndices[0] == columnIndices2[0] and columnIndices[2] == columnIndices2[2] + 1:
                    if columnIndices[0] != len(columnMatrix) - 1:
                        columnIndex = columnIndices[0] + 1
                else:
                    columnIndex = columnIndices[0]
            elif len(possibleCombination) == 1:
                squareToRemove = possibleCombination.pop()
                crossedSquares1.append(squareToRemove)
                crossedSquares2 = []
                crossedSquares3 = []
                crossedSquares4 = []
                columnIndices = rowToColumn(squareToRemove[0], squareToRemove[1], squareToRemove[2])
                columnIndex = columnIndices[0]
            elif (len(possibleCombination)) == 0:
                if columnIndex != len(columnMatrix) - 1:
                    columnIndex = columnIndex + 1
                else:
                    finished = True
        else:
            if columnIndex != len(columnMatrix) - 1:
                columnIndex = columnIndex + 1
        if firstIteration == True:
            firstIteration = False
    return possibleCombinationsList



while len(completeBlocks) < len(blockNumberIDs):
    for blockNumberID in blockNumberIDs:
        blockIDIndex = blockNumberIDs.index(blockNumberID)
        possibleCombinationsList = possibleCombinations(blockNumberID)
        if len(possibleCombinationsList) == 1:
            for squareIndex in possibleCombinationsList[0]:
                if rowMatrix[squareIndex[0]][squareIndex[1]][squareIndex[2]] != "x":
                    rowMatrix[squareIndex[0]][squareIndex[1]][squareIndex[2]] = "filled"
                    columnIndices = rowToColumn(squareIndex[0], squareIndex[1], squareIndex[2])
                    columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "filled"
            for squareIndex in blockNumberIDSquares[blockIDIndex]:
                if rowMatrix[squareIndex[0]][squareIndex[1]][squareIndex[2]] != "filled":
                    rowMatrix[squareIndex[0]][squareIndex[1]][squareIndex[2]] = "x"
                    columnIndices = rowToColumn(squareIndex[0], squareIndex[1], squareIndex[2])
                    columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
            if blockNumberID not in completeBlocks:
                completeBlocks.append(blockNumberID)
        else:
            filteredPossibleCombinationsList = copy.deepcopy(possibleCombinationsList)
            for possibleCombination in possibleCombinationsList:
                adjacentBlockIDList = adjacentBlocks(possibleCombination)
                shouldContinue = False
                for adjacentBlockID in adjacentBlockIDList:
                    if adjacentBlockID not in completeBlocks:
                        adjacentPossibleCombinationsList = possibleCombinations(adjacentBlockID, blockNumberID, possibleCombination)
                        if len(adjacentPossibleCombinationsList) == 0:
                            filteredPossibleCombinationsList.remove(possibleCombination)
                            shouldContinue = True
                            break
                if shouldContinue == True:
                    continue
                adjacentFilled = True
                for adjacentBlockID in adjacentBlockIDList:
                    if adjacentBlockID not in completeBlocks:
                        adjacentFilled = False
                        break
                if adjacentFilled == True:
                    filledAdjacentBlockIDList = adjacentBlocks(possibleCombination, [], True)
                    if len(filledAdjacentBlockIDList) == 0:
                        filteredPossibleCombinationsList.remove(possibleCombination)
                        continue
                    breakLoop = False
                    isolated = False
                    for adjacentBlockID in adjacentBlockIDList:
                        if adjacentBlockID not in filledAdjacentBlockIDList:
                            blockNumbersToCheck = [adjacentBlockID]
                            checkedBlockNumbers = []
                            isolated = False
                            filledSquares = []
                            while len(blockNumbersToCheck) > 0:
                                adjacentBlockIDIndex = blockNumberIDs.index(blockNumbersToCheck[0])
                                for square in blockNumberIDSquares[adjacentBlockIDIndex]:
                                    if rowMatrix[square[0]][square[1]][square[2]] == "filled":
                                        filledSquares.append(square)
                                secondAdjacentBlockIDList = adjacentBlocks(filledSquares)
                                for secondAdjacentBlockID in secondAdjacentBlockIDList:
                                    if (secondAdjacentBlockID not in completeBlocks) and (secondAdjacentBlockID != blockNumberID):
                                        breakLoop = True
                                        break
                                if breakLoop == True:
                                    break
                                filledSecondAdjacentBlockIDList = adjacentBlocks(filledSquares, [], True)
                                if filledSecondAdjacentBlockIDList != []:
                                    for filledSecondAdjacentBlockID in filledSecondAdjacentBlockIDList:
                                        if (filledSecondAdjacentBlockID not in checkedBlockNumbers) and (filledSecondAdjacentBlockID not in blockNumbersToCheck):
                                            blockNumbersToCheck.append(filledSecondAdjacentBlockID)
                                checkedBlockNumbers.append(blockNumbersToCheck.pop(0))
                                filledSquares = []
                            if breakLoop == True:
                                break
                            if (blockNumbersToCheck == []) and (len(checkedBlockNumbers) < len(blockNumberIDs) - 1):
                                isolated = True
                                filteredPossibleCombinationsList.remove(possibleCombination)
                                break
                    if isolated == True:
                        continue
            counter = [0] * len(blockNumberIDSquares[blockIDIndex])
            index = 0
            fillCount = 0
            for squareIndex in blockNumberIDSquares[blockIDIndex]:
                if rowMatrix[squareIndex[0]][squareIndex[1]][squareIndex[2]] == "filled":
                    fillCount = fillCount + 1
                for possibleCombination in filteredPossibleCombinationsList:
                    if squareIndex in possibleCombination:
                        counter[index] = counter[index] + 1
                index = index + 1
            index = 0
            for item in counter:
                if item == 0:
                    if rowMatrix[blockNumberIDSquares[blockIDIndex][index][0]][blockNumberIDSquares[blockIDIndex][index][1]][blockNumberIDSquares[blockIDIndex][index][2]] != "filled":
                        rowMatrix[blockNumberIDSquares[blockIDIndex][index][0]][blockNumberIDSquares[blockIDIndex][index][1]][blockNumberIDSquares[blockIDIndex][index][2]] = "x"
                        columnIndices = rowToColumn(blockNumberIDSquares[blockIDIndex][index][0], blockNumberIDSquares[blockIDIndex][index][1], blockNumberIDSquares[blockIDIndex][index][2])
                        columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
                if item == len(filteredPossibleCombinationsList):
                    if rowMatrix[blockNumberIDSquares[blockIDIndex][index][0]][blockNumberIDSquares[blockIDIndex][index][1]][blockNumberIDSquares[blockIDIndex][index][2]] != "x":
                        rowMatrix[blockNumberIDSquares[blockIDIndex][index][0]][blockNumberIDSquares[blockIDIndex][index][1]][blockNumberIDSquares[blockIDIndex][index][2]] = "filled"
                        fillCount = fillCount + 1
                        columnIndices = rowToColumn(blockNumberIDSquares[blockIDIndex][index][0], blockNumberIDSquares[blockIDIndex][index][1], blockNumberIDSquares[blockIDIndex][index][2])
                        columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "filled" 
                index = index + 1
            if fillCount == 4:
                if blockNumberID not in completeBlocks:
                    completeBlocks.append(blockNumberID)


print(rowMatrix)                        





        



        
        

                


