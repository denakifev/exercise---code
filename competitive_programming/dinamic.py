el = {
    0: ('water' , 3, 10),
    1: ('book', 1,3),
    2: ('food', 2,9),
    3:('jacket', 2, 5),
    4: ('camera', 1,6)
}

matrix = [[[0, None] for _ in range(6)] for _ in range(5)]

def unit(par):
    res = []
    for row in par:
        for el in row:
            res.append(el)
    return res
for i in range(5):
    for j in range(6):
        if el[i][1] <= j+1:
            cost = el[i][2]
            if cost > matrix[i-1][j][0]:
                matrix[i][j] = [cost, [el[i][0],]]
            else: 
                if j-el[i][1] <= 0:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    cost+= matrix[i-1][j-el[i][1]][0]
                    if cost > matrix[i-1][j][0]:
                    
                        res = [[el[i][0],], matrix[i-1][j - el[i][1]][1]]
                        matrix[i][j] = [cost, unit(res)]
                    else:
                        matrix[i][j] = matrix[i-1][j]
        else:
            matrix[i][j] = matrix[i-1][j] 

print(*matrix, sep = '\n')






            
            
            





                
        