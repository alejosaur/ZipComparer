import zipfile

#Compare file by file based on file size (fast, not precise)
def sizeCompare(warAnterior, warNuevo, tresshold):
	oldDict = {}
	newDict = {}
	diffList = []

	with zipfile.ZipFile(warAnterior, "r") as f:
		for name in f.namelist():
			data = f.read(name)
			oldDict[name] = len(data)

	with zipfile.ZipFile(warNuevo, "r") as f:
		for name in f.namelist():
			data = f.read(name)
			if(name in oldDict):
				if(oldDict[name] - len(data) > tresshold):
					diffList.append(name)
				del oldDict[name]
			else:
				newDict[name] = len(data)
				
	#Files existing in both versions, but with diferent content
	if(diffList):
		print("\n\033[1mArchivos diferentes: \033[0m")
		for f in diffList:
			print("\t" + f)
	else:
		print("\n\033[1mNo hay archivos con tamaño diferente.\033[0m")

	#Files existing only in old version
	if(oldDict):
		print("\n\033[1mArchivos existentes en", warAnterior, "pero no en", warNuevo + ":\033[0m")
		for f in oldDict:
			print("\t" + f)
	else:
		print("\n\033[1mNo hay archivos existentes en", warAnterior, "pero no en", warNuevo + ".\033[0m")

	#Files existing only in new version
	if(newDict):
		print("\n\033[1mArchivos existentes en", warNuevo, "pero no en", warAnterior + ":\033[0m")
		for f in newDict:
			print("\t" + f)
	else:
		print("\n\033[1mNo hay archivos existentes en", warNuevo, "pero no en", warAnterior + ".\033[0m")

#Compare file by file based on file size (slower, but very precise)
def dataCompare(warAnterior, warNuevo, tresshold):
	oldDict = {}
	newDict = {}
	diffList = []

	with zipfile.ZipFile(warAnterior, "r") as f:
		for name in f.namelist():
			data = f.read(name)
			oldDict[name] = data


	with zipfile.ZipFile(warNuevo, "r") as f:
		for name in f.namelist():
			data = f.read(name)
			if(name in oldDict):
				if(oldDict[name] != data):
					diffList.append(name)
				del oldDict[name]
			else:
				newDict[name] = data
	
	#Files existing in both versions, but with diferent content
	if(diffList):
		print("\n\033[1mArchivos diferentes: \033[0m")
		for f in diffList:
			print("\t" + f)
	else:
		print("\n\033[1mNo hay archivos con contenido diferente.\033[0m")

	#Files existing only in old version	
	if(oldDict):
		print("\n\033[1mArchivos existentes en", warAnterior, "pero no en", warNuevo + ":\033[0m")
		for f in oldDict:
			print("\t" + f)
	else:
		print("\n\033[1mNo hay archivos existentes en", warAnterior, "pero no en", warNuevo + ".\033[0m")

	#Files existing only in new version
	if(newDict):
		print("\n\033[1mArchivos existentes en", warNuevo, "pero no en", warAnterior + ":\033[0m")
		for f in newDict:
			print("\t" + f)
	else:
		print("\n\033[1mNo hay archivos existentes en", warNuevo, "pero no en", warAnterior + ".\033[0m")