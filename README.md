# Comparador de Zip/War

## Comenzando ☕

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Funcionamiento** para conocer como utilizar el comparador.


### Pre-requisitos 📋

Para poder utilizar el comparador, necesitarás tener instalado Python3 en tu máquina, para comprobar si está correctamente instalado, ejecuta en la consola de tu preferencia (terminal, cmd, powershell, etc) el siguiente comando:

```
python --version
```
Al ejecutar este comando, la consola mostrará la versión de Python actualmente instalada (o error, si no tienes ninguna versión en tu máquina); si la versión mostrada es mayor a 3, puedes continuar, si tienes la versión 2 de Python, o la consola te arroja error, debes revisar tu instalación de Python3 antes de continuar.

### Instalación 🔧

_El comparador es un script portable, por tanto no tienes que realizar ninguna instalación._

## Funcionamiento ⚙️

### Ejecución 🚀

Este script recibe 3 parámetros:

1. **_Nombre del zip/war #1 a comparar:_** _Este archivo debe estar en el mismo directorio en que clonaste el repositorio, junto con main.py y algorythms.py. De aquí en adelante nos referiremos a él como **archivo1**._
2. **_Nombre del zip/war #2 a comparar:_** _Este archivo debe estar en el mismo directorio en que clonaste el repositorio, junto con archivo1, main.py y algorythms.py. De aquí en adelante nos referiremos a él como **archivo2**._
3. **_Tresshold o sensibilidad de la comparación:_** _Corresponde a un número entero mayor o igual a cero, dependiendo de qué tan estricta quieres que sea la comparación, representa la cantidad de bytes de diferencia en tamaño que pueden tener dos archivos para que sean considerados similares, entre mayor sea el número, menos estricta será la comparación. De aquí en adelante nos referiremos a él como **tresshold**_.

Así que para ejecutarlo, debes ejecutar en la consola un comando con la siguiente estructura:
```
python main.py archivo1 archivo2 tresshold
```
En el repositorio están incluidos los archivos Desktop.war y Desktop1.war para que pruebes y entiendas cómo funciona el comparador, así que vamos a usarlos como ejemplo; para iniciar el script con estos dos archivos, y un tresshold de 5, el comando que debes ejecutar es:
```
python main.py Desktop.war Desktop1.war 5
```

Para comparar tus propios archivos, simplemente cópialos a la carpeta, y ejecuta el script con los nombres de los archivos, y el tresshold que creas indicado.

### Operación 🕹

Al ejecutar el Script, verás en la consola un menú con tres opciones:

1. _Comparación por tamaño de archivos_
2. _Comparación por contenido de archivos_
3. _Salir_

y el mensaje "_Selecciona una opción (1,2,3)_". Para seleccionar una opción, escribe el número que corresponde, y pulsa enter.

Si quieres hacer una comparación rápida, pero no tan precisa de los archivos, selecciona la comparación por tamaños; te mostrará los archivos que son considerados diferentes según el tresshold que hayas ingresado, además de los archivos que se encuentran únicamente en alguno de los dos zip/war comparados.

Si necesitas una comparación más profunda y precisa, aunque puede consumir un poco más de tiempo y recursos computacionales, selecciona la comparación por contenido; esta te mostrará una lista de todos los archivos que son diferentes, resaltando los que tienen una diferencia en tamaño mayor al tresshold; al igual que la comparación por tamaños, también te mostrará los archivos que no se encuentran en los dos zip/war.

Si deseas ver las diferencias exactas entre dos archivos, verás que al final de la lista de diferencias tienes esta opción; para seleccionar el archivo que quieres comparar, ingresa el número que corresponde; verás este número a la izquierda de cada archivo en el cual se encontraron diferencias. Al pulsar enter, verás en pantalla las diferencias encontradas en formato diff unificado (el usado por git), si quieres saber más de este formato, ingresa [aquí](https://www.it-swarm.dev/es/git/como-leer-la-salida-de-git-diff/968227917/). Si no quieres comparar ningún archivo, puedes ingresar 0 y retornar al menú principal.

Cuando hayas terminado las comparaciones, selecciona 3 para salir.

## Construido con 🛠️

* [Python3](https://docs.python.org/3/) 

## Versionado 📌

Se usa [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/alejosaur/ZipComparer/tags).

## Autores ✒️

* **Alejandro Santamaría** - *Desarrollo* - [alejosaur](https://github.com/alejosaur)

## Licencia 📄
Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE.md](LICENSE.md) para detalles.


---
⌨️ con ❤️ por [Alejosaur](https://github.com/alejosaur) 🐙
