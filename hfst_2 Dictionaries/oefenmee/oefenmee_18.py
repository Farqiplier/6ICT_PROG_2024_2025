dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']]
rijen = len(dambord_2D) - 1

while True:
    print("------- UNPUT -------")
    y = int(input("Geef een rij op: "))
    x = input("Geef een kolom op: ")
    if x and y <= rijen:
        print("------- RESULTAAT -------")
        print(f"Op deze INDEX staat: {dambord_2D[int(y)][int(x)]}")
        break
    else:
        print("Deze index bestaat niet.")
        