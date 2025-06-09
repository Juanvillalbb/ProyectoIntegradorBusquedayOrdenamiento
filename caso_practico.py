import time
import random

def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1

def busqueda_binaria(arr, objetivo):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def ordenar_burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)

def main():
    cantidad_lineal = 100_000 
    cantidad_burbuja = 10_000  
    cantidad_quick = 200_000    
    rango_max = 2_000_000

    arreglo_lineal = random.sample(range(rango_max), cantidad_lineal)
    arreglo_burbuja = random.sample(range(rango_max), cantidad_burbuja)
    arreglo_quick = random.sample(range(rango_max), cantidad_quick)

    objetivo_lineal = random.choice(arreglo_lineal)
    objetivo_burbuja = random.choice(arreglo_burbuja)
    objetivo_quick = random.choice(arreglo_quick)

    inicio_lineal = time.time()
    busqueda_lineal(arreglo_lineal, objetivo_lineal)
    fin_lineal = time.time()

    arreglo_burbuja_copia = arreglo_burbuja.copy()

    inicio_burbuja = time.time()
    ordenar_burbuja(arreglo_burbuja_copia)
    fin_burbuja = time.time()

    inicio_binaria_burbuja = time.time()
    busqueda_binaria(arreglo_burbuja_copia, objetivo_burbuja)
    fin_binaria_burbuja = time.time()

    inicio_quick = time.time()
    arreglo_quick_ordenado = quick_sort(arreglo_quick)
    fin_quick = time.time()

    inicio_binaria_quick = time.time()
    busqueda_binaria(arreglo_quick_ordenado, objetivo_quick)
    fin_binaria_quick = time.time()

    print("\n== RESULTADOS ==")
    print(f"[Búsqueda lineal] Elementos: {cantidad_lineal}")
    print(f"  Tiempo búsqueda lineal    : {fin_lineal - inicio_lineal:.6f} segundos")

    print(f"\n[Bubble Sort] Elementos: {cantidad_burbuja}")
    print(f"  Tiempo ordenamiento       : {fin_burbuja - inicio_burbuja:.6f} segundos")
    print(f"  Tiempo búsqueda binaria   : {fin_binaria_burbuja - inicio_binaria_burbuja:.6f} segundos")

    print(f"\n[Quick Sort] Elementos: {cantidad_quick}")
    print(f"  Tiempo ordenamiento       : {fin_quick - inicio_quick:.6f} segundos")
    print(f"  Tiempo búsqueda binaria   : {fin_binaria_quick - inicio_binaria_quick:.6f} segundos")

if __name__ == "__main__":
    main()