from sys import argv, exit
import csv
import re

if len(argv) != 3:
    print(f"Number of arguments must be 3, you typed {argv} arguments in the command-line")
    exit

seq = open(argv[2], "r").read()  # abre y guarda la secuencia

with open(argv[1], "r") as file:  # abre el archivo csv de base de datos
    csv_reader = csv.reader(file)  # lee el archivo
    k = []
    dna = []
    count = 0
    for j in csv_reader:  # loop para leer solo la primera linea del csv y guardar str
        j.remove('name')  # quitar name y dejar solo str
        break
    for x in j:  # loop para identificar numero de veces que se repite cada str en la secuencia
        result_dna = x
        while result_dna in seq:
            count += 1
            result_dna += x
        dna.append(count)  # agrega cada numero en una lista
        count = 0
    for i in csv_reader:  # loop para leer numero de str en el archivo csv
        k = i.copy()
        del k[0]
        k = list(map(int, k))
        len_dna = len(dna)
        if dna == k:
            print(i[0])
            exit()
    
print("No match")
