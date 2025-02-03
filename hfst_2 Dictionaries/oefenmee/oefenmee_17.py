lijst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

print(lijst_1[0])
print(lijst_1[2])
print(lijst_1[6])

lijst_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(lijst_2[0][0])
print(lijst_2[1][1])
print(lijst_2[2][1])

lijst_3 = [ 1, 2, [3, 4], 5, 7, [7, 8, 9] ]

print(lijst_3[1])
print(lijst_3[2][1])
print(lijst_3[5][2])

lijst_4 = [ [1, 2, 3, [4, 5, 6, [7, 8, 9] ] ] ]

print(lijst_4[0][0])
print(lijst_4[0][3][1])
print(lijst_4[0][3][3][2])