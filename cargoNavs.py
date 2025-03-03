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
    

"""
Respuestas a las preguntas:

1. **¿La solución es Bottom-Up (BU) o Top-Down (TP)?**
   - La solución es **Bottom-Up (BU)**.
    Porque comenzamos con el máximo de una sola nave y vamos usando ese caso anterior para construir el caso siguiente.
2. **Complejidad temporal y espacial:**
   - **Temporal:** O(n), ya que en el peor caso (que quepan todos los cohetes en la plataforma) el algoritmo solo recorre una lista de N cohetes una vez.
   - **Espacial:** O(n), ya que en el peor caso (que quepan todos los cohetes en la plataforma) se crean dos listas de tamaño N.
3. **Explicación de la estrategia de la solución:**
   - La estrategia usada consiste en inicializar agregando el cohete a la izquierda (ya que ambas plataformas son factibles).
   Una vez inicializada, revisa que el cohete quepa en al menos una de las plataformas y acto seguido escoge la plataforma con mayor espacio restante y si son iguales escoga le izquierda por defecto.
   Lleva el conteo de cuántos cohetes caben en la variable <<ind>>.
   - **Memoización:** La memorización se hace a través de dos listas. Una llamada memo la cuál almacena el número de cohetes que caben en ese indice y numero de cohetes que lleva. Y otra lista la cuál se
   encarga de almacenar en orden de cohete hacia qué lado de la plataformo debe ser acomodado.
   
Por último, es necesario aclarar que este algoritmo no necesariamente toma el camino esperado en las pruebas de senesummit; ya que como se indica en el PDF existen varios caminos factibles. Sin embargo,
sí retorna el valor esperado, solo ubicando los cohetes en plataformas diferentes (incluso las posiciones del ejemplo del PDF son diferentes).
   """