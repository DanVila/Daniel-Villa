'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo con el sexo y el
nombre. 
El grupo A está formado por las mujeres con un nombre anterior a la M y los
hombres con un nombre posterior a la N y el grupo B por el resto. 

Deberás escribir un programa que pregunte al usuario su nombre y sexo, y muestre por
pantalla el grupo que le corresponde.
'''

 
Genero = input ('Escribe tu Genero Hombre / Mujer : ')
Nombre = input ('Escribe tu Nombre : ')
print(Nombre)
 
for x in Nombre.upper()[0]:
    if Genero == 'Mujer':
        if x in ("A","B","C","D","E","F","G","H","I","J","K","L",'M'):
            print("Perteneces al GRUPO A")
        else:
            print("Perteneces al GRUPO B")
    elif Genero == 'Hombre':
        if x in ("N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"):
             print("Perteneces al GRUPO A")
        else:
            print("Perteneces al GRUPO B")
    elif Genero != 'Hombre' or Genero != 'Mujer':
        print("Genero incorrecto")

      