import zipfile

#Compare file by file based on file size (fast, not precise)
def sizeCompare(warAnterior, warNuevo, tresshold):
	oldList = []
	newList = []
	sharedList = []
	diffList = []
	
	try:
		old = zipfile.ZipFile(warAnterior, "r");
		new = zipfile.ZipFile(warNuevo, "r")

		oldList = [x for x in old.namelist() if not (x in new.namelist())]#files only in old war
		newList = [x for x in new.namelist() if not (x in old.namelist())]#files only in new war
		sharedList = [x for x in old.namelist() if (x in new.namelist())]#files in both wars

		for name in sharedList:
			oldData = old.read(name)
			newData = new.read(name)
			if abs(len(newData) - len(oldData)) > tresshold: 
				#if size difference is greather than tresshold,add to diffList
				diffList.append(name)

		old.close()
		new.close()
					
		#Files existing in both versions, but with diferent content
		if(diffList):
			print("\n\033[1mArchivos diferentes: \033[0m")
			for f in diffList:
				print("\t" + f)
		else:
			print("\n\033[1mNo hay archivos con tamaño diferente.\033[0m")

		#Files existing only in old version
		if(oldList):
			print("\n\033[1mArchivos existentes en", warAnterior, "pero no en", warNuevo + ":\033[0m")
			for f in oldList:
				print("\t" + f)
		else:
			print("\n\033[1mNo hay archivos existentes en", warAnterior, "pero no en", warNuevo + ".\033[0m")

		#Files existing only in new version
		if(newList):
			print("\n\033[1mArchivos existentes en", warNuevo, "pero no en", warAnterior + ":\033[0m")
			for f in newList:
				print("\t" + f)
		else:
			print("\n\033[1mNo hay archivos existentes en", warNuevo, "pero no en", warAnterior + ".\033[0m")
	except:
		print("No se pudo realizar la comparación, revise que el nombre de los archivos sea correcto y se encuentren en el mismo directorio que main.py")
#-------------------------------------------------------------------------------------------------------------------#
#Compare file by file based on file content (slower, but very precise)
def dataCompare(warAnterior, warNuevo, tresshold):
	oldList = []
	newList = []
	sharedList = []
	diffDict = {}
	try:
		old = zipfile.ZipFile(warAnterior, "r");
		new = zipfile.ZipFile(warNuevo, "r")

		oldList = [x for x in old.namelist() if not (x in new.namelist())]#files only in old war
		newList = [x for x in new.namelist() if not (x in old.namelist())]#files only in new war
		sharedList = [x for x in old.namelist() if (x in new.namelist())]#files in both wars

		for name in sharedList:
			oldData = old.read(name)
			newData = new.read(name)
			if not(oldData == newData):
				oldSize = len(oldData)
				newSize = len(newData)
				#if content is not the same,add to diffDict, with the size of both files, highlighting when size diff is greater than tresshold
				if abs(newSize - oldSize) > tresshold: 
					diffDict[name] = "\033[1mTamaño antiguo: " + str(oldSize) + ", Tamaño nuevo:" + str(newSize) + "\033[0m"
				else:
					diffDict[name] = "Tamaño antiguo: " + str(oldSize) + ", Tamaño nuevo:" + str(newSize)

		old.close()
		new.close()

		#Files existing in both versions, but with diferent content
		if(diffDict):
			print("\n\033[1mArchivos diferentes: \033[0m")
			for f in diffDict:
				print("\t" + f + " - " + diffDict[f])
		else:
			print("\n\033[1mNo hay archivos con contenido diferente.\033[0m")

		#Files existing only in old version	
		if(oldList):
			print("\n\033[1mArchivos existentes en", warAnterior, "pero no en", warNuevo + ":\033[0m")
			for f in oldList:
				print("\t" + f)
		else:
			print("\n\033[1mNo hay archivos existentes en", warAnterior, "pero no en", warNuevo + ".\033[0m")

		#Files existing only in new version
		if(newList):
			print("\n\033[1mArchivos existentes en", warNuevo, "pero no en", warAnterior + ":\033[0m")
			for f in newList:
				print("\t" + f)
		else:
			print("\n\033[1mNo hay archivos existentes en", warNuevo, "pero no en", warAnterior + ".\033[0m")
	except Exception as e:
		print("No se pudo realizar la comparación, revise que el nombre de los archivos sea correcto y se encuentren en el mismo directorio que main.py")