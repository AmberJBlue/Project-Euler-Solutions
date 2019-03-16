

def multOf3and5(ceiling):
    total = 0
    result = sum(x for x in range(ceiling) if x % 5 == 0 or x % 3 == 0)
    for x in range(ceiling):
        if x % 5 == 0 or x % 3 == 0:
            total += x

    print(total)


multOf3and5(1000)
