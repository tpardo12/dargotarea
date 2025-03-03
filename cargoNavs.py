from sys import stdin

def cargar_naves_bu(izq: int, der: int, naves: list):
    if naves[0] > izq and naves[0] > der:
        return 0, ""

    pos = []
    memo = [None]*len(naves)
    pos.append("izquierda")
    izq -= naves[0]
    memo[0] = 1
    ind = 1

    if len(naves) > 1:
        salir = False
        while ind < len(naves) and not salir:
            if naves[ind] > izq and naves[ind] > der:
                salir = True
            else:
                if izq >= der:
                    memo[ind] = 1 + memo[ind-1]
                    izq -= naves[ind]
                    pos.append("izquierda")
                else:
                    memo[ind] = 1 + memo[ind-1]
                    der -= naves[ind]
                    pos.append("derecha")
                ind += 1
    return ind, pos

def main():
    resp = []
    line = stdin.readline().strip().split()
    ind = int(line[0])
    while (ind > 0):
        naves = []
        line = stdin.readline().strip().split()
        if len(line) == 0:
            print(0)
            break
        tam = (int(line[0])*100)
        line = stdin.readline().strip().split()
        while (int(line[0]) != 0):
            naves.append(int(line[0]))
            line = stdin.readline().strip().split()
        resp.append(cargar_naves_bu(tam, tam, naves))
        ind -= 1
    
    for response in resp:
        print(response[0])
        for posi in response[1]:
            print(posi)

if __name__ == '__main__':
    main()