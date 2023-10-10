lengte = int(input("Hoe lang wil je de reeks? > ")) - 2  # -2, want er staan al 2 in de array.
iteraties = 1
fibonacciReeks = [0, 1]

while iteraties <= lengte:
    getal = fibonacciReeks[-1] + fibonacciReeks[-2]
    fibonacciReeks.append(getal)
    iteraties += 1
print(fibonacciReeks)