listadelineas = []
lista = []

def pasouno(file):
	a = open(file,'r').readlines()
	b=[]
	c = 0
	for i in a:
		c = c + 1
#		print(b)
		if c == len(a):
			b.append(i)
		else:
			b.append(i[0:-1])
#	print(b)
	return b

def pasodos(lista):
	x = 0
	templist = []
	for i in lista:
		templist.append([])
		for j in i:
			templist[x].append(j.split())
		x = x + 1
#	print(templist)
	listadelineas = templist
	return templist

def pasotres(lista):
	templist = []
	templistnames = []
	templistfinal = []
	for i in lista:
		for j in i:
			templist.append(j)
	for i in templist:
		i[1] = int(i[1])
	
	for i in range(len(templist)):
		if templistnames.count(templist[i][0]) == 0:
			templistnames.append(templist[i][0])


	for i in range(len(templistnames)):
		templistfinal.append([])
		templistfinal[i].append(templistnames[i])


	for i in templistfinal:
		for j in templist:
			if i[0] == j[0]:
				try:
					i[1] = i[1] + j[1]
				except IndexError:
					i.append(j[1])

	return templistfinal


for i in range(1,4):
#	print(i)
	listadelineas.append(pasouno('3/files/'+str(i)))

lista = pasodos(listadelineas)

lista = pasotres(lista)

print(pasouno('3/files/'+str(i)))

