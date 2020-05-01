import zipfile
import difflib
import io
import differences_printer as pr

def size_compare(old_zip, new_zip, tresshold):
	"""Compare file by file based on file size (fast, not precise)

    Parameters:
    	old_zip: name of base(original, old) compressed file
		new_zip: name of edited(new) compressed file
		tresshold: permited tresshold 
    """

	old_list = []
	new_list = []
	shared_list = []
	diff_list = []
	
	try:
		old = zipfile.ZipFile(old_zip, "r")
		new = zipfile.ZipFile(new_zip, "r")

		old_list = [x for x in old.namelist() if not (x in new.namelist())]#files only in old zip/war
		new_list = [x for x in new.namelist() if not (x in old.namelist())]#files only in new zip/war
		shared_list = [x for x in old.namelist() if (x in new.namelist())]#files in both zips/wars

		for name in shared_list:
			old_data = old.read(name)
			new_data = new.read(name)
			if abs(len(new_data) - len(old_data)) > tresshold: 
				#if size difference is greather than tresshold,add to diff_list
				diff_list.append(name)

		old.close()
		new.close()
					
		#Files existing in both versions, but with diferent content
		pr.print_different_files(diff_list)

		#Files existing only in old version
		pr.print_non_existing(old_list,old_zip,new_zip)

		#Files existing only in new version
		pr.print_non_existing(new_list,new_zip,old_zip)

		file_compare(old_zip,new_zip,diff_list)
	except Exception as e:
		print("No se pudo realizar la comparación, revise que el nombre de los archivos sea correcto y se encuentren en el mismo directorio que main.py" + str(e))
#-------------------------------------------------------------------------------------------------------------------#

def data_compare(old_zip, new_zip, tresshold):
	"""Compare file by file based on file content (slower, but very precise)

    Parameters:
    	old_zip: name of base(original, old) compressed file
		new_zip: name of edited(new) compressed file
		tresshold: permited tresshold 
    """

	old_list = []
	new_list = []
	shared_list = []
	diff_dict = {}
	try:
		old = zipfile.ZipFile(old_zip, "r")
		new = zipfile.ZipFile(new_zip, "r")

		old_list = [x for x in old.namelist() if not (x in new.namelist())]#files only in old zip/war
		new_list = [x for x in new.namelist() if not (x in old.namelist())]#files only in new zip/war
		shared_list = [x for x in old.namelist() if (x in new.namelist())]#files in both zip/wars

		for name in shared_list:
			old_data = old.read(name)
			new_data = new.read(name)
			if not(old_data == new_data):
				old_size = len(old_data)
				new_size = len(new_data)
				#if content is not the same,add to diff_dict, with the size of both files, highlighting when size diff is greater than tresshold
				if abs(new_size - old_size) > tresshold: 
					diff_dict[name] = "\033[1mTamaño antiguo: " + str(old_size) + ", Tamaño nuevo:" + str(new_size) + "\033[0m"
				else:
					diff_dict[name] = "Tamaño antiguo: " + str(old_size) + ", Tamaño nuevo:" + str(new_size)

		old.close()
		new.close()

		#Files existing in both versions, but with diferent content
		pr.print_different_files(diff_dict)

		#Files existing only in old version	
		pr.print_non_existing(old_list,old_zip,new_zip)

		#Files existing only in new version
		pr.print_non_existing(new_list,new_zip,old_zip)

		file_compare(old_zip,new_zip,diff_dict)

	except Exception as e :
		print("No se pudo realizar la comparación, revise que el nombre de los archivos sea correcto y se encuentren en el mismo directorio que main.py" + str(e))

#-------------------------------------------------------------------------------------------------------------------#


def file_compare(old_zip, new_zip, diff):
	"""Compare two versions of a file, print differences in diff format

    Parameters:
    	old_zip: name of base(original, old) compressed file
		new_zip: name of edited(new) compressed file
		diff: list or dictionary of differing files 
    """

	print("\033[1m\n\nSi desea ver las diferencias entre las dos versiones de algún archivo, escriba a continuación el número correspondiente [1," + str(len(diff)) + "], o 0 para salir: ",end="")
	try:
		option = int(input())
	except ValueError:
		option = 0

	pr.cls()
	
	#If option corresponds to a file
	if(option > 0 and option <= len(diff)):

		#open compressed
		old = zipfile.ZipFile(old_zip, "r")
		new = zipfile.ZipFile(new_zip, "r")
		
		#get file name either for list or dict
		if(isinstance(diff, list)):
			file_name = diff[option-1]	
		elif(isinstance(diff, dict)):
			file_name = list(diff.keys())[option-1]	

		#print file name
		print(file_name, "\n")

		#open filed from compressed
		file1 = io.TextIOWrapper(io.BytesIO(old.read(file_name))).readlines()
		file2 = io.TextIOWrapper(io.BytesIO(new.read(file_name))).readlines()

		#check for differences and print
		for line in difflib.unified_diff(file1, file2, n=0):
			print(line)

		#close files
		old.close()
		new.close()