import os

matricula = open('5/files/matricula.csv', 'r')
lineas_matricula = matricula.readlines()
print(lineas_matricula)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def crear(alumno, directorio):
	try:
		if directorio[-1] == '/':
			directorio = directorio[0:-1]
	except IndexError:
		pass

	alumnos = []
	for i in lineas_matricula:
		linea = i.split()
		alumnos.append(linea[0])
	if alumno+',' in alumnos:
		pass
	else:
		cls()
		crear(input('El alumno que has escogido ('+alumno+') no exsiste,\nElije otro alumno:\n\t'), directorio)

	if os.path.exists(directorio):
		pass
	else:
		cls()
		crear(alumno, input('El directorio que has escogido no exsiste,\nElije otro directorio:\n\t'))
		exit()

	alumno = str(alumno)
	for i in lineas_matricula:
		linea = i.split()
		if linea[0] == alumno+',':
			file = open(directorio+'/'+alumno+'.md', 'w')

			texto = [
				'# '+alumno,
				'\n## Estas matriculado en:\n',
			]
			for l in range(len(linea)):
				if l != 0:	
					texto.append('- '+linea[l].strip(',')+'\n')

			file.writelines(texto)

			file.close()


crear('d', input('En que directorio quieres guardarlo:\n\t'))
#	5/files/matriculas/