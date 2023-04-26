import datetime

nombre = input ('Escriba tu Nombre: ')
apellido1 = input ('Escriba tu Primer apellido: ')
apellido2 = input ('Escriba tu segundo apellido: ')
año_nacimiento = input('Escriba su año de nacimiento: ')
dia_nacimiento = input('Escriba su día de nacimiento: ')
mes_nacimiento =input ('Escriba su mes de nacimiento: ')

print (nombre)

print(apellido1)

print (apellido2)

print(año_nacimiento)

print (mes_nacimiento,dia_nacimiento)

nombre_Mayuscula = nombre.upper()+' '+apellido1.upper()+' '+apellido2.upper()
nombre_minuscula = nombre.lower()+' '+apellido1.lower()+' '+apellido2.lower()
nombre_completo = nombre+' '+apellido1+' '+apellido2

print ('Este es tu nombe completo en Mayuscula',nombre_Mayuscula)
print ('Este es tu nombe completo en minuscula',nombre_minuscula)

Fecha_Nacimiento =  dia_nacimiento+'-'+mes_nacimiento+'-'+año_nacimiento
print('Esta es tu fecha de nacimiento', Fecha_Nacimiento)

fecha_nacimiento = datetime.datetime.strptime(Fecha_Nacimiento, '%d-%m-%Y')
edad = datetime.datetime.now().year - fecha_nacimiento.year

print('Tu edad es',edad)

def contar_vocales(nombre_completo):
	contador = 0
	for letra in nombre_completo:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

cantidad = contar_vocales(nombre_completo)
print('Tu nombre completo tiene',contar_vocales(nombre_completo),'vocales')




def contar_letras(nombre_completo):
	contador = 0
	for letra in nombre_completo:
		if letra.lower() in "bcdfghjklmnñpqrstvwxyz":
			contador += 1
	return contador

cantidad = contar_letras(nombre_completo)
print('Tu nombre completo tiene',contar_letras(nombre_completo),'letras')

print('¿Tu edad en 10 años será', edad+10)

media = [30, 50]

def mean(dataset):
    return sum(dataset) / len(dataset)

print('El promedio de mi edad actual y mi edad en 20 años es',mean(media))

print ('¿Tu edad es un carácter de tipo número?' ) 
print(type(año_nacimiento))

print ('¿Tu nombre completo es un carácter de tipo alfanumérico?' )
print(type(nombre_completo))
