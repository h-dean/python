
def treegen(basesize, trunkchar, leafchar):
    spaces = int(int(basesize)/2)
    
    for x in range(1, int(basesize)+1):
        if x % 2 != 0:
            print(spaces * " " + leafchar * int(x))
            spaces -= 1    
    print(int(int(basesize)/2-2) * " ", trunkchar * 3)


#rules = input("enter (basesize trunkchar leafchar)\n").split(" ")
#treegen(rules[0], rules[1], rules[2])

treegen(10, "|", "o")
