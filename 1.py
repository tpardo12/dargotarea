def coinchangelimited(value, memo, limits):
    coins = [1, 2, 3, 5, 10, 20]
    INF = 1_000_000_000_000  # Un valor muy grande que representa "no es posible"
    
    if value == 0:
        return 0  # Si el valor es 0, no se necesitan monedas
    if value < 0:
        return INF  # No se puede formar un valor negativo

    # Si ya hemos calculado el resultado antes, devolvemos el valor memoizado
    if memo[value] != INF:
        return memo[value]

    rtvalue = INF  # Inicializamos con un valor grande para encontrar el mínimo

    for i in range(len(coins)):
        if limits[i] > 0 and value >= coins[i]:  # Solo usar la moneda si hay disponibles
            new_limits = limits[:]  # Hacemos una copia nueva en cada iteración
            new_limits[i] -= 1  # Usamos una moneda de este tipo

            rtvalue = min(rtvalue, 1 + coinchangelimited(value - coins[i], memo, new_limits))

    memo[value] = rtvalue  # Guardamos el resultado en la memoización
    print(memo)
    return rtvalue


def pep(monedaspepe):
    montomaximo = sum(monedaspepe[i] * c for i, c in enumerate([1, 2, 3, 5, 10, 20]))
    memo = [1_000_000_000_000] * (montomaximo + 1)  # Inicializamos memo con INF

    resultado = coinchangelimited(6, memo, monedaspepe)

    return resultado if resultado != 1_000_000_000_000 else -1  # Devolvemos -1 si no hay solución


# Prueba con un conjunto de monedas limitadas
print(pep([2, 2, 0, 1, 0, 0]))  # Debería devolver la cantidad mínima de monedas necesarias
