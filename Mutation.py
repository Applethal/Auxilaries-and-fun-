Parents = {}

p = int(input("How many parents do you wish to have ?"))
counter = 0

for i in range(p):
    Parents[i] = []
    counter += 1
    print("You are now processing parent number", counter)
    limit = int(input("How many elements should this parent have"))
    while limit > 0:
        Parents[i].append(int(input("Insert the element")))
        limit -= 1

print(Parents)


def Pick(Parents):
    Choose = int(
        input(
            "From The Parents dictionary that you have created, which parent do you want to choose for the crossover"
        )
    )
    parent1 = Parents.get(Choose)
    Choose_new = int(input("Now choose the second parent"))
    parent2 = Parents.get(Choose_new)
    return parent1, parent2


parent1, parent2 = Pick(Parents)

print("First Parent", parent1)
print("Second Parent", parent2)


def Crossover(parent1, parent2):
    if len(parent1) != len(parent2):
        print(
            "Unless I missed something, I don't see potential for a crossover with these parents, you might want to choose ones which have the same number of elements within their sets"
        )
    k = int(input("how many cuts do you wish to perform within the set ?"))
    A = 0
    child1 = []
    child2 = []

    for i in range(k):
        while k > 1:
            position = int(input("At which position should this cut occur"))
            child1.extend(parent1[A:position])
            child2.extend(parent2[A:position])
            parent1, parent2 = parent2, parent1
            A = position
            print("first child", child1)
            print("second child", child2)
            k -= 1
    if k == 1:
        position = int(input("At which position should the last cut occur ?"))
        child1.extend(parent1[A:position])
        child2.extend(parent2[A:position])
        parent1, parent2 = parent2, parent1
        A = position
        child1.extend(parent1[position:])
        child2.extend(parent2[position:])

    return child1, child2


child1, child2 = Crossover(parent1, parent2)

print("first child", child1)
print("second child", child2)
