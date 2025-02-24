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
            selected_items.append(tesoros[n-1])
            w -= tesoros[n-1][0]
        n -= 1
    return selected_items

def main():
    x,y = stdin.readline().split()
    while x != '':
        N = stdin.readline().strip()
        tesoros = []
        for i in range(int(N)):
            tesoros.append(tuple(map(int,stdin.readline().split())))
    
        k = [[-1 for i in range(int(x)+1)] for j in range(int(N)+1)]
        oro = knapsck(int(x), int(N), tesoros, k)
        selected_items = get_selected_items(int(x), int(N), tesoros, k)
        stdout.write(str(oro) + '\n')
        stdout.write(str(len(selected_items)) + '\n')
        for item in selected_items:
            stdout.write(str(item[0]) + ' ' + str(item[1]) + '\n')
        x,y = stdin.readline().split()
       

        
if __name__ == "__main__":
    main()
    