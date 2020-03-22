import zipfile

TRESSHOLD = 0
WAR_ANTERIOR = "Desktop.zip"
WAR_NUEVO = "Desktop1.zip"

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


				
	print("\nArchivos diferentes: ")
	for f in diffList:
		print("\t" + f)

	print("\nArchivos existentes en", warAnterior, "pero no en", warNuevo + ":")
	for f in oldDict:
		print("\t" + f)

	print("\nArchivos existentes en", warNuevo, "pero no en", warAnterior + ":")
	for f in newDict:
		print("\t" + f)

while(true):
	sizeCompare(WAR_ANTERIOR, WAR_NUEVO, TRESSHOLD)