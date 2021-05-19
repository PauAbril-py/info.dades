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


lis = [[['Jose','1'],['Alvaro','2']],[['Jose','3'],['Alvaro','1']],[['Jose','3'],['Alvaro','1']]]

print(pasotres(lis))