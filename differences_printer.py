from os import system, name

def cls():
	"""Clear the screen either in windows or mac/linux.
    """
	# windows
	if name == 'nt': 
		system('cls') 
    # mac and linux(here, os.name is 'posix') 
	else: 
		system('clear') 

def print_different_files(diff):
	"""Print files that difers between zips/wars.

    Parameters:
    	diff: list or dictionary of differing files
    """

	print("\n\033[1mArchivos diferentes: \033[0m")
	if(isinstance(diff, list)):
		for index, file_name in enumerate(diff):
			print("\t" + file_name)
	elif(isinstance(diff, dict)):
		for index, file_name in enumerate(diff):
			print("\t[" + str(index + 1) + "] " + file_name + " - " + diff[file_name])
	else:
		print("\n\033[1mNo hay archivos diferentes.\033[0m")

def print_non_existing(file_list, src_name, dest_name):
	"""Print files that exist only in one zip/war.

    Parameters:
    	file_list: list of files
		src_name: name of source(old) file
		dest_name: name of destination(new) file
    """

	if(file_list):
		print("\n\033[1mArchivos existentes en", src_name, "pero no en", dest_name + ":\033[0m")
		for file_name in file_list:
			print("\t" + file_name)
	else:
		print("\n\033[1mNo hay archivos existentes en", src_name, "pero no en", dest_name + ".\033[0m")