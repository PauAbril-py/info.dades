import os

#directory = open('7-country/files/country-1.csv', 'r')
directory = open('countrys.csv', 'r') #ToDO: move to function
file = directory.readlines()

header = []
countrylist = []

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def opn():
	#turn into list and remove extra " #TODO: remove \n
	for i in file:
		i = i.replace('"', '')

		if i == file[0].replace('"', ''):
			for k in i.split(','):
				header.append(k)

		else:
			countrylist.append(i.split(','))

	for i in countrylist:
		for j in range(len(i)):
			try:
				i[j] = float(i[j])
			except:
				pass

opn()


print(header,' \n')

#for i in countrylist:
#	print(i)


def ui():
	choice = str(input('''
What do you want to do:\n
1. search | 2. continent info | 3. Life expectancy | 4. choose storage | 5. help | 6. exit\n'''))

#TODO: do
	cls()
	if choice == '1' or choice.lower() == 'search':
		search(input('What do you want to search:\n\t'),input('Name:\n\t'))
	elif choice == '2' or choice.lower() == 'help':
		continent()
	elif choice == '3' or choice.lower() == 'help':
		life_expectancy(input('Income per capita:\n\t'),input('Life expectancy:\n\t'))
	elif choice == '4' or choice.lower() == 'choose file': #TODO: directory
		store_dir = input('Choose directory to save the files')	
	elif choice == '5' or choice.lower() == 'help':
		help()
	elif choice == '6' or choice.lower() == 'exit':
		cls()
		exit()	
	ui()

def search_ui():
	pass

def search(what, name):
	for i in range(len(header)):
		if what.lower() == header[i].lower():
			what = int(i) #TODO: error correction
			break
	#	else:
	#		what = 'F'
	if what == 'F':
		print('Error')
		ui()
	else:
		results = []
		for i in countrylist:
			if i[what].lower() == name.lower():
				print()
			#	print(header)
			#	print(i)
				output(i, 'out.txt').print_result() #TODO: directory
				
				results.append(i)
		
		yn = input('Do you want to store it on a file? [y/N] ')
		if yn == 'y':
			if len(results) == 1:
				for i in results:
					output(i, 'out.txt').store_result() #TODO: directory
			else:
				output(i, 'out.txt').clear_file()
				for i in results:
					output(i, 'out.txt').store_multiple_results() #TODO: directory
				#return i

def life_expectancy(IncomePerCapita, LifeExpectancy):	#GNP [8] / Population [6]
	results = []
	for i in countrylist:
		#print(i)
		try:
			IPC = float(round(i[8]/i[6], num_after_point(IncomePerCapita)))
			LE = float(round(i[7], num_after_point(LifeExpectancy)))
	#		print(IPC, IncomePerCapita,' | ',LE,LifeExpectancy)
			if float(IncomePerCapita) == IPC and float(LifeExpectancy) == LE:
				print(i)
				results.append(i)
		except:
	#		print('no va')
			pass
		#print(IPC)
		
	pass


def help():
	print('''\n------------------------------\n
search:  Searches for what you want on the file;
	first:
	second:

choose storage:  Lets you choose the directory to save the output file.

help:  Shows help page.

exit:  Exits the program.
\n------------------------------\n''')

def format_output(inoutput):
#	outputlist = []
	output = str()
	for i in range(len(header)):
		#outputlist.append(str(header[i])+': '+str(inoutput[i]))
		output = output + str(header[i])+': '+str(inoutput[i])+'\n'
	#for i in outputlist:
	#	print(i)
	return(output)

class output:
	def __init__(self, content, directory):
		self.content = format_output(content)
		self.directory = directory

	def store_result(self):
		fil = open(self.directory, 'w')
		fil.write(str(self.content))
		print('Saved to "'+self.directory+'"')
		fil.close()

	def store_multiple_results(self):
		fil = open(self.directory, 'a')
		fil.write(str(self.content))
		print('Saved to "'+self.directory+'"')
		fil.close()
	
	def clear_file(self):
		fil = open(self.directory, 'w')
		fil.write('')
		fil.close()
	
	def print_result(self):
		print(self.content)

def num_after_point(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1




ui()
#search(input('What do you want to search:\n\t'),input('Name:\n\t'))