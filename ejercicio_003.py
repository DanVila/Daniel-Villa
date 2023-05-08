'''
    Deberás escribir un programa que almacene la cadena de caracteres contraseña en una
    variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

 
#for x in range (3):
i=0
count =3
while i <3:
    print('Escribe la contraseña: ')
    print('Tienes ', count, 'Intentos disponibles')  
    Contraseña = input()
    
    if Contraseña == 'Welcome123':
    
        print('La Contraseña es correcta')
        break
    else:
        print('La Contraseña es invalida, vuelve a intentar')   
        #print('Tienes ', x, 'Intentos disponibles')  
        i += 1
        count -=1
