from decimal import Decimal
import sys


monedas = [1, 2, 4, 10,20,40]



def cc(value: int, coins: list[int], memo: list[int]) -> int:
    return_value = 1_000_000_000_000
    if value == 0:
        return_value = 0
    elif value > 0:
        visited = memo[value]
        if visited != return_value:
            return_value = visited
        else:
            
            for coin in coins:
                 return_value = min(
                    return_value, 1 + cc(value - coin, coins, memo)
                )
        memo[value] = return_value
    return return_value

def coinchangelimited (value,memo,limits):
    rtvalue = 1_000_000_000_000
    if value == 0:
        return 0
    elif value < 0:
        return 1_000_000_000_000
    
    visited = memo[value]
    if visited != 1_000_000_000_000:
        return visited
    else:
        for i in range(len(monedas)):
            if limits[i] > 0 and value >= monedas[i]:
                copy = limits[:]
                copy[i] -= 1
                rtvalue = min (
                    rtvalue, 1 + coinchangelimited(  (value - monedas[i]), memo, copy)
                    )
                    
    memo[value] = rtvalue 
    return rtvalue


def pep (monedaspepe,valor):
    
    montomaximo = monedaspepe[0]  + monedaspepe[1]*2 + monedaspepe[2]*4 + monedaspepe[3]*10 + monedaspepe[4]*20 + monedaspepe[5]*40
    memochange = [1_000_000_000_000] * (montomaximo + 1)
    memopepe = [1_000_000_000_000] * (montomaximo + 1)
    ci  = cc(montomaximo,monedas,memochange)
    cl = coinchangelimited(montomaximo, memopepe, monedaspepe)
    res = 1_000_000_000_000
    memochange[0] = 0
    
    for i in range(int(valor/5), montomaximo  + 1):
        
        if memopepe[i] != 1_000_000_000_000:
            res = min(res, memopepe[i] + memochange[i - int(valor/5)])
            
    return res



if __name__ == "__main__":
    
    eol = "0 0 0 0 0 0"
    current_case = sys.stdin.readline().strip()
    while current_case != eol:
    
        number_of_coins = list(map(int, current_case.split()[:6]))
        change = Decimal(current_case.split()[6])
        change_int = int(change * 100)
        print(pep(number_of_coins, change_int))
        current_case = sys.stdin.readline().strip()