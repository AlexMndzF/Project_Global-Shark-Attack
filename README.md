# Global Shark Attack

En este proyecto se analíza un data set de ataques de tiburones a nivel mundial, registrado por http://www.sharkattackfile.net/index.htm.

## Pasos

### Limpieza de datos y búsqueda de la hipótesis:
Lo primero a realizar con el data set es analizar las columnas y ver las que tienen todos sus datos nulos y cuales no arrojan información, mirando estas dos cosas me di cuenta que las columnas Unmamed: 22 y Unnamed:23 podía descartarlas por tener casi todos sus valores nulos y no estar etiquetada la información que aparece en ellas.

Una vez eliminadas esas columnas, mi siguiente paso fue buscar series que pudiera categorizar fácilmente y pudieran darme datos de estos ataques, elegí las columnas de sexo, tipo de ataque y el desenlace del ataque. Estas series tenía valores con caracteres erróneos o categorías que no podía asignar al sexo de la persona que atacaban, tipo de ataque o desenlace. Limpie estos datos para reducirlo a las categorías mínimas que representasen las diferentes opciones que podían tomar:

   1.- Serie sexo: en esta serie partía de tener 6 posibles categorías, entre las que se incluían algunas correctas con caracteres añadidos al principio o final y otras que no correspondían a ningún sexo, para procesar todos esos datos decidí modificar los valores de las que podía incluir en categoría y las que no las cambie por unknown.
   
   2.- Serie tipo de ataque: en esta serie veo dos grandes tipos de ataques, provocados y no provocados, para reducir las categorías, el resto las metí en una nueva categoría llamada otras.
   
   3.- Serie desenlace: Al igual que en la serie anterior, el tipo de desenlace era claro, el afectado moría o sobrevivía. Por lo que limpie las categorías en las que había caracteres delante o detrás y las que no podía asignar a ninguna de esas las metí en unknown.

Con estas series limpias y categorizadas el siguiente paso fue hacer un filtro primero por año, para evitar trabajar con ataques demasiado antiguos y poco documentados y empezar a buscar una hipótesis.
En mi caso intento demostrar que el numero de supervivientes es mayor con el paso de los años debido a los avances médicos.

Con la hipótesis clara es el momento de empezar a crear gráficas que muestren datos de ataques con el desenlace en función de si el ataque es provocado o no:

#### Supervivientes de ataques provocados y no provocados:
Azul => Atacks 

Naranja => Survivals-provoked 

Verde => Survivals-unprovoked

<p align="center"> <img  src="https://github.com/AlexMndzF/Project_Global-Shark-Attack/blob/master/src/Global%20shark_survivals-type.png"></p>

#### Muertos de ataques provocados y no provocados:
Azul => Atacks 

Naranja => Fatals-provoked 

Verde => Fatals-unprovoked

<p align="center"> <img  src="https://github.com/AlexMndzF/Project_Global-Shark-Attack/blob/master/src/Global%20shark_fatals-type.png"></p>

Al ver estos datos me doy cuenta de que una gráfica con el número de ataques globales y su desenlace me valdría para validar o no mi hipótesis, por lo que genero una gráfica general:

#### Ataques globales con muertos y supervivientes:
Azul => Total Ataks

Naranja => Survivals

Verde => Fatals 
<p align="center"> <img  src="https://github.com/AlexMndzF/Project_Global-Shark-Attack/blob/master/src/Global%20shark_Totals.png"></p>

## Hipótesis:
Al finalizar el análisis con los datos obtenidos mi hipótesis se confirmae, dejando claro que el número de supervivientes ha aumentado con el paso de los años, he podido ver que en ataques provocados el número de supervivientes si es mayor que en ataques no provocados, esto puede ser debido a tener un mayor control de la situación y no ser tan impredecible como en un ataque no provocado.