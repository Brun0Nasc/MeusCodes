while True:
    n = int(input())
    sdesc = "Discarded cards: "
    if n == 0:
        break
    elif n > 1:
        pilha = []
        desc = []
        for i in range(1, n+1):
            pilha.insert(0, i)
        while len(pilha) > 1:
            desc.append(pilha[len(pilha)-1])
            pilha.pop()
            pilha.insert(0, pilha[len(pilha)-1])
            pilha.pop()
        for c, p in enumerate(desc):
            if c != (len(desc)-1):
                sdesc += f"{p}, "
            else:
                sdesc += f"{p}"
        print(sdesc)
        print(f"Remaining card: {pilha[0]}")
