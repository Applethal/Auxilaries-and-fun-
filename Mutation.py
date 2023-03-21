
def Set():
    limit = int(input("How many elements should your Set contain ?"))
    Elements = []
    while limit > 0:
        Elements.append(int(input("Insert the element")))
        limit -= 1
    print(Elements)
    
    return Elements
Elements = Set()





cell = int(input("Input the new element that you wish to replace"))
position = int(input("At which position should the element be inserted"))

def Mutation(Elements,position,cell):
    
    Elements.insert(position,cell)
    Elements.pop(position-1)
    print(Elements)
    

Mutation(Elements,position,cell)
