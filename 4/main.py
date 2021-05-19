archivo=input("Dime el archivo que quieras abrir")
fichero=open('4/files/'+str(archivo),"r")
b=fichero.read()
print(b)

def ContarPalabras():
	contar=len(b.split())
	print(contar)

def MasRepetida(frase):
	return max(set(frase.split()), key = frase.split().count)

def NumeroDePalabras(frase):
	lista = frase.split()
	print(lista)
	frecuencia = []
	for w in lista:
		frecuencia.append(lista.count(w))
		print(frecuencia)
	final = []
	repetidos = []
	for i in range(len(lista)):
		if lista[i] in repetidos:
			pass
		else:
			final.append([lista[i],frecuencia[i]])
			repetidos.append(lista[i])
	return final

#ContarPalabras()
#print(MasRepetida(b))
print(NumeroDePalabras(b))