import csv
archivoEjemplo=open("Ejemplo.csv")
ejemploLector=csv.reader(archivoEjemplo)
for linea in ejemploLector:
    print ("Linea #"+str(ejemploLector.line_num)+ " " + str(linea))
