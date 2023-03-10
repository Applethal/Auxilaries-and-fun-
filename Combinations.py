Sets = {}
Combinations = []
Limit = int(input("Please enter the number of elements that you wish to add to your Set"))
Elements = []
while Limit > 0:
    Element = int(input("Enter the element that you wish to add to your set"))
    Elements.append(Element)
    Limit -= 1

for x in Elements:
    for y in Elements:
        if x != y:
            Combinations.append((x, y))

for i in range(len(Combinations)):
    Sets[i] = Combinations[i]

print(Sets)
