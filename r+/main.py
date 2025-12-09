# Abrimos el archivo "julian.txt" en modo r+ (leer y escribir)
# r+ permite leer y luego escribir SIN borrar el contenido existente
with open("julian.txt", "r+") as archivo:

    # Leemos todo el contenido del archivo y lo guardamos en la variable 'texto'
    texto = archivo.read()

    # Escribimos una nueva línea al final del archivo
    # OJO: después de leer, el cursor queda al final del archivo,
    # por eso lo que escribimos se agrega automáticamente al final
    archivo.write("\ntexto agregado al final del archivo.")

    # Mostramos en pantalla lo que tenía el archivo antes de agregar el texto
    print(texto)
