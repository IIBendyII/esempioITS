tabellina = [x*3 for x in range (1,11)]
sintassi = [f"{i+1} x 3 = {n}" for i,n in enumerate(tabellina)]
map(print, sintassi)
