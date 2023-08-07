cadena_usuario = input("Escriba una cadena de texto: ")

#Se convierte la cadena a minúsculas para hacer la comparación sin importar mayúsculas o minúsculas
cadena_usuario = cadena_usuario.lower()

#Se eliminan los espacios en blanco de la cadena
cadena_usuario = cadena_usuario.replace(" ", "")

#Obtenemos la versión invertida de la cadena para hacer la comparación
cadena_invertida = ""
for caracter in cadena_usuario:
    cadena_invertida = caracter + cadena_invertida

#Se verifica si la cadena es igual a su versión invertida
if cadena_usuario == cadena_invertida:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")






