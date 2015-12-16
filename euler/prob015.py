# should probably use recursion

def traverse(xPos,yPos):
    if xPos<len(nodes[yPos])-1 and nodes[yPos][xPos+1]==True:
        print(xPos, yPos)
        nodes[yPos][xPos] = False
        traverse(xPos+1,yPos)
    elif yPos<len(nodes)-1 and nodes[yPos+1][xPos]==True:
        print(xPos, yPos)
        nodes[yPos][xPos] = False
        traverse(xPos,yPos+1)
    else:
        print(xPos, yPos)
        return


nodes = [[True for i in range(21)] for i in range(21)]

pathCount = 0
print(nodes)
traverse(0,0)
