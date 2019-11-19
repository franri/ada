import math

def coin_change(original_amount, coins): # coins ordenado de manera descendente
    # array que contiene la cantidad de monedas, y cuales de cada una
    efficient_quantity = [(-1, []) for _ in range(original_amount+1)]
    efficient_quantity[0] = (0, [])

    for amount in range(1, len(efficient_quantity)):
        coins_quantity_each_coin = [[0, [0 for _ in coins]] for _ in coins] # guarda cantidad de cambio para cada moneda
        for i, coin in enumerate(coins):
            # if restante//coin != 0: # si no me paso con esta moneda
            #     quantity += restante//coin
            #     coins_quantity[i] += quantity
            #     left -= quantity*coin
            #     # ahora busco lo que falte para el mejor cambio

            # calculo la cantidad de monedas requeridas para el cambio si incluyera esa moneda
            left = amount
            if left//coin != 0: # no me paso con esta moneda
                quantity_of_this_coin = left//coin
                coins_quantity_each_coin[i][0] += quantity_of_this_coin
                coins_quantity_each_coin[i][1][i] += quantity_of_this_coin
                leftover = left%coin
                if leftover != 0:
                    optimum_change_for_leftover = efficient_quantity[leftover]
                    coins_quantity_each_coin[i][0] += optimum_change_for_leftover[0]
                    for idx, quan in enumerate(optimum_change_for_leftover[1]):
                        coins_quantity_each_coin[i][1][idx] += quan
            else:
                coins_quantity_each_coin[i][0] = math.inf
        # elijo la que tenga menor cantidad de monedas, y tenga por lo menos una moneda
        mejor_cambio = coins_quantity_each_coin[0]
        for tupl in coins_quantity_each_coin:
            if tupl[0] < mejor_cambio[0]:
                mejor_cambio = tupl
        # ya tengo el mejor cambio, ahora lo guardo
        efficient_quantity[amount] = mejor_cambio
    
    return efficient_quantity[-1]

print(coin_change(15, [12, 5, 1]))

                


