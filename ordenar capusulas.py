import sys

def solve_case(n, capsula):
   
    lis = []
    if n > 0:
        lis.append(capsula[0])  
    for i in range(1, 2 * n):
        if capsula[i] > lis[-1]:  
            lis.append(capsula[i]) 
        else:
            index = lower_bound(lis, capsula[i])
            lis[index] = capsula[i]  

    return len(lis)

def lower_bound(lis, value):
    
    low, high = 0, len(lis)
    while low < high:
        mid = (low + high) // 2
        if lis[mid] < value:
            low = mid + 1
        else:
            high = mid
    return low

def main(input_source=sys.stdin, output_dest=sys.stdout):

    case = int(input_source.readline().strip())
    
    while case > 0:
        n = int(input_source.readline().strip()) 
        cap = [0] * (2 * n)
        
       
        for i in range(n):
            cap[i + n] = int(input_source.readline().strip())
            cap[n - i - 1] = cap[i + n]  
        

        result = solve_case(n, cap)
       
        output_dest.write(f"{result}\n")
   
        case -= 1

if __name__ == "__main__":
   
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as input_file:
            if len(sys.argv) > 2:
                with open(sys.argv[2], 'w') as output_file:
                    main(input_source=input_file, output_dest=output_file)
            else:
                main(input_source=input_file)
    else:
        main() 
"""
Respuestas a las preguntas:

1. **¿La solución es Bottom-Up (BU) o Top-Down (TP)?**
   - La solución es **Bottom-Up (BU)**. Empezamos desde las capsulas más pequeñas y vamos construyendo la subsecuencia más larga posible, utilizando la información previa para extenderla paso a paso.

2. **Complejidad temporal y espacial:**
   - **Temporal:** \(O(n \log n)\). Esto se debe a que, para cada vagón, realizamos una búsqueda binaria (usando la función `lower_bound`), que tiene un costo de \(O(\log n)\) para cada uno de los \(n\) elementos. La búsqueda binaria optimiza la inserción en la subsecuencia.
   - **Espacial:** \(O(n)\). Solo necesitamos un array de tamaño \(n\) para mantener la subsecuencia más larga (LIS), además del array `capulas` que tiene longitud \(2n\) para manejar las dos mitades de la lista original (orden directo e invertido).

3. **Explicación de la estrategia de la solución:**
   - La estrategia utilizada es una combinación de la **Subsecuencia más larga creciente (LIS)** y la **Subsecuencia decreciente más larga (LDS)**. Para cada capsula, decidimos si lo colocamos al principio o al final . El objetivo es maximizar la longitud del tren con las capsulas ordenados de manera decreciente por peso.
   - **Memoización:** La memoización está presente implícitamente en el uso del array `lis`, donde almacenamos los resultados parciales de la subsecuencia más larga. Esto evita que tengamos que recalcular desde el principio en cada paso, lo que mejora la eficiencia del algoritmo.
"""
