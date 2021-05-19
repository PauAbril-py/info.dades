import os

#directory = open('7-country/files/country-1.csv', 'r').readlines()
directory = open('countrys.csv', 'r') #ToDO: move to function
file = directory.readlines()

header = []
countrylist = []

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def opn():
	#turn into list and remove extra "
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
1. search | 2. choose storage | 3. help | 4. exit\n'''))

#TODO: do
	cls()
	if choice == '1' or choice.lower() == 'search':
		search(input('What do you want to search:\n\t'),input('Name:\n\t'))
	elif choice == '2' or choice.lower() == 'choose file': #TODO: directory
		store_dir = input('Choose directory to save the files')
	elif choice == '3' or choice.lower() == 'help':
		help()
	elif choice == '4' or choice.lower() == 'exit':
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

	for i in countrylist:
		if i[what].lower() == name.lower():
			print()
		#	print(header)
			#print(i)
			output(i, 'out.txt').print_result() #TODO: directory
			yn = input('Do you want to store it on a file? [y/n] ') #TODO: multiple countries
			if yn == 'y':
				output(i, 'out.txt').store_result() #TODO: directory

#def choose_file():
#	directory.close()

#	directory = open(input('What csv file do you want to open:\n\t'), 'r')
#	
#	file = directory.readlines()
#	opn()

def help():
	print('''\n------------------------------\n
search:  Searches for what you want on the file;
	first:
	second:

choose storage:  Lets you choose the directory to save the output file.

help:  Shows help page.

exit:  Exits the program.
\n------------------------------\n''')

def format_output(output):
	pass

class output:
	def __init__(self, content, directory):
		self.content = content
		self.directory = directory

	def store_result(self):
		fil = open(self.directory, 'w')
		fil.write(str(self.content))
		print('Saved to "'+self.directory+'"')
	
	def print_result(self):
		print(self.content)


def life_expectancy():
	pass



ui()
#search(input('What do you want to search:\n\t'),input('Name:\n\t'))