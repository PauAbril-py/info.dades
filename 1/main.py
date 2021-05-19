def htmlcheck(dir):
	file = open(dir,'r').read()
	line0 = '<!DOCTYPE HTML>'
	line1 = '<!doctype html>'
	add = 0

	for i in range(len(line0)):
		if file[i] == line0[i] or file[i] == line1 [i]:
			add = add + 1

	if add == len(line0):
		return 'es html'
	else:
		return 'no es html'
	

print(htmlcheck('html/index.html'))