from sys import stdin, stdout




def knapsck(w, n, tesoros, k):
    oro = -1 
    siguiente = n - 1 
    current_store_value = k[n][w]
   
    if n == 0 or w == 0:
        oro = 0
    elif current_store_value != -1:
        oro = current_store_value
    elif tesoros[siguiente][0] > w:
        current_store_value = knapsck(w, siguiente, tesoros, k)
        k[n][w] = current_store_value
        oro = current_store_value
    else:
        current_store_value = max(knapsck(w, n - 1, tesoros, k) ,  tesoros[siguiente][1] + knapsck(w - tesoros[siguiente][0], siguiente, tesoros,k))
        k[n][w] = current_store_value
        oro = current_store_value

    return oro 

def get_selected_items(w, n, tesoros, k):
    selected_items = []
    while n > 0 and w > 0:
        if k[n][w] != k[n-1][w]:
            selected_items.append(n-1) 
            w -= tesoros[n-1][0]
        n -= 1
    return selected_items

def main():
    x,y = stdin.readline().split()
    while x != '' and y != '':
        N = stdin.readline().strip()
        
        if N != '':
            tesoros = []
            tesorosnomod = []
            for i in range(int(N)):
                m,s = stdin.readline().split()
                tesorosnomod.append((int(m),int(s)))
                tesoros.append(((2*int(y)*(int(m)) + (int(y)* int(m))),int(s)))
        
            k = [[-1 for i in range(int(x)+1)] for j in range(int(N)+1)]
            oro = knapsck(int(x), int(N), tesoros, k)
            selected_items = get_selected_items(int(x), int(N), tesoros, k)
            stdout.write(str(oro) + '\n')
            itemstot = len(selected_items) -1 
            stdout.write(str(itemstot) + '\n')
            indx = selected_items[::-1]
            for index in range(1, len(selected_items)):
                ind = indx[index]
                item  = tesorosnomod[ind]
                stdout.write(str(item[0]) + ' ' + str(item[1]) + '\n')
        else: 
            x  = ''
       
if __name__ == "__main__":
    main()
    
"""
La Solucion es TD

LA compleidad espacial el (tiempo maximo * numero de tesoros), la complejidad temporal es (N * W) donde N es el numero de elementos
y W es el tiempo maximo que tenemos para ir por los tesoros

LA estrategia abordada no es muy diferente al bien conocido problema de la mochila, basicamente vamos memorizando las soluciones optimas 
que llevamos hasta ahora, resolviendo el problema de manera recursiva dividiendo el problema en unos mas pequeños . Asi evitando calculos repetivivos y ayudando a la complejidad temporal.
Para el retorno de los tesoros en los que ya hemos pasado vamos a recorrer el arreglo en el que almacenamos los problemas y hacemos una operacion inversa, mirando si escogimos o no el tesoro 
en cuestion.

"""