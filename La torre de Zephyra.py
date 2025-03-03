from itertools import permutations, count
import sys


def LIS(bloques: list):
    dp = [0] * len(bloques) 
    for i, bloque in enumerate(bloques):
        dp[i] = bloque[-1]
        for j in range(i):
            if (bloque[0] > bloques[j][0] and bloque[1] > bloques[j][1] and dp[j] + bloque[-1] > dp[i]):
                dp[i] = dp[j] + bloque[-1]
  
    return max(dp)

def read_input(source):
    # Función para leer la entrada, ya sea desde un archivo o desde la consola
    if source:
        return open(source, 'r')
    else:
        return sys.stdin  # Lee desde la consola

def write_output(destination):
    # Función para escribir la salida, ya sea en archivo o en la consola
    if destination:
        return open(destination, 'a')  # Modo 'a' para escribir sin sobreescribir el contenido
    else:
        return sys.stdout  # Escribe en la consola

def main(input_file=None, output_file=None):
    with read_input(input_file) as infile:
        outfile = write_output(output_file) 
        for case in count(1):
            line = infile.readline().strip()
            bloques = []
            if not line:
                break  # Si la línea está vacía, salir del bucle
            try:
                T = int(line)
            except ValueError:
                break  # Si la conversión falla, salir del bucle
            for _ in range(T):
                bloques.extend(permutations(map(int, infile.readline().split())))
                
            bloques.sort()
            outfile.write(f"Caso {case}: maxima altura = {LIS(bloques)}\n")
                # Si es sys.stdout, asegurarse de que se vacíe el buffer y se imprima de inmediato
            if outfile == sys.stdout:
                sys.stdout.flush()

        # Cerrar el archivo de salida si fue un archivo
        if output_file:
            outfile.close()
    
if __name__ == "__main__":
    input_file = None
    output_file = None
    
    # Si el usuario pasa argumentos desde la línea de comandos, los utilizamos
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    
    main(input_file, output_file)
    
"""
# -- Sección de Explicación --
# – Su solución es BU o TP:
#   Esta solución es una **solución de arriba hacia abajo(Top-down, TP)**. 
#   Usa el recurso de memorizacion,alamcenando en arrglos las soluciones pasadas, para llegar a la final 


# – Complejidad espacial y temporal:
#   - Complejidad temporal: **O(6n^2 )**, donde `n` es el número de tipos de bloques
#
#   - Complejidad espacial: **O( 6n  )**. La memoria usada para almacenar el resultado de LIS

# – Estrategia de la solución:
     Se utilizo el algoritmo LIS para encontrar la subsecuencia mas larga entre los bloques, comparando las bases y sumando a la lista la altura de cada bloque seleccionado
     de igual forma se utilizo la herramienta permutations dentro de la libreria intertools para realizar las posibles posiciones que puede tomar cada bloque 
# – Uso de Memoización:
#   la solucion reserva un arreglo principal donde se agregan las alturas de las subseciencias, destacando a la mas grande

"""