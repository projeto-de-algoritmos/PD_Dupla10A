def knapnapSacknap(W, wt, val, n): 
    knap = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                knap[i][w] = 0
            elif wt[i-1] <= w: 
                knap[i][w] = max(val[i-1] + knap[i-1][w-wt[i-1]],  knap[i-1][w]) 
            else: 
                knap[i][w] = knap[i-1][w] 
  
    return knap[n][W] 

if __name__ == '__main__':

    print("Insira os valores de cada item os separando por espaços: ")
    val = list(map(int, input().split()))
    # val = [60, 100, 120]
    print("Insira os peso de cada item os separando por espaços: ")
    wt = list(map(int, input().split()))
    W = int(input("Insira a capacidade da mochila: "))
    n = len(val) 
    print("A valor máximo que se pode carregar na mochila é: {}".format(knapnapSacknap(W, wt, val, n))) 