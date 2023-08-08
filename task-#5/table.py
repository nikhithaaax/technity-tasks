table = [['apples', 'oranges', 'strawberries', 'cherries'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'elephants', 'goose'],
            ['cars', 'boats', 'bycicles', 'planes']]
          

def getColWidth(tableData):
    # create list for colWidth and store the max for each line in maxCol
    colWidths = [0] * len(tableData[0])
    maxCol = []

    for i in range(len(tableData)):
        for item in tableData[i]:
            del colWidths[0]
            colWidths.append(len(item))

        maxCol.append(max(colWidths))
    return maxCol

def printTable(tableData, maxColWidth):
    print("The new and aligned table:" + "\n")
    # create items list
    items = [0] * len(tableData)

    # transpose tableData in list "items" and print each item aligned to the right
    # according to the length of the longest word in each column
    for item in tableData:
        del items[0]
        items.append(item)
    for i in range(len(items[0])):
        for j in range(len(items)):
            print(items[j][i].rjust(maxColWidth[j], " "), end=" ")
        print()


printTable(table, getColWidth(table))
