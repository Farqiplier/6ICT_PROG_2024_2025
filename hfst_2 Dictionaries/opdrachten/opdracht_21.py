lijst_2D = [
    [11, 12, 34, 14],
    [32, 22, 23, 24],
    [31, 32, 33, 12] 
]

def max_vinder(list):
    max_getal = 0
    for index, sublist in enumerate(lijst_2D):
        for x in sublist:
            if  max_getal != (max_getal:=max(max_getal, x)):
                i = index
    return max_getal,i

print(max_vinder(lijst_2D))