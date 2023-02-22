# Abrir el archivo en modo de escritura (si no existe, se crea)
archivo = open("mi_archivo.txt", "w")

# Escribir en el archivo la primera vez
archivo.write("Este es mi primer texto en el archivo.\n")
archivo.close()

# Abrir el archivo en modo de escritura de nuevo
archivo = open("mi_archivo.txt", "w")

# Escribir en el archivo la segunda vez
archivo.write("Este es mi segundo texto en el archivo.\n")
archivo.close()

# Abrir el archivo en modo de lectura para leer su contenido
archivo = open("mi_archivo.txt", "r")
contenido = archivo.read()
archivo.close()

# Mostrar el contenido del archivo
print(contenido)
