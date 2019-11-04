# Global Shark Attack

En este proyecto se analíza un data set de ataques de tiburones a nivel mundial, registrado por http://www.sharkattackfile.net/index.htm.

## Pasos

### Limpieza de datos y búsqueda de la hipótesis:
Lo primero a realizar con el data set es analizar las columnas y ver las que tienen todos sus datos nulos y cuales no arrojan informacion, mirando estas dos cosas me di cuenta que las columnas Unmamed: 22 y Unnamed:23 podia descartarlas por tener casi todos sus valores nulos y no estar etiquetada la informacion que aparece en ellas.

Una vez eliminadas esas columnas, mi sigiente paso fue buscar serias que pudiera categorizar facilmente y pudieran darme datos de estos ataques, elejí las columnas de sexo, tipo de ataque y el desenlace del ataque. Estas series tenian valores con caracteres erroneos o categorias que no podia asignar al sexo de la persona que atacaban, tipo de ataque o desenlace. limpie estos datos para reducirlo a las categorias minimas que representasen las diferentes opciones que podian tomar:

    1.- Serie sexo: en esta serie parita de tener 6 posibles categorias, entre las que se incluian algunas correctas con caracteres añadidos al principio o final y otras que no correspondian a ningun sexo, para procesar todos esos datos decici modificar los valores de las que podia incluir en categoria y las que no las cambie por unknown.
    2.- Serie tipo de ataque: en esta serie veoa dos grandes tipos de ataques, provocados y no provocados, para reducir las categorias el resto las meti en una nueva categoria llamada otras.
    3.- Serie desenlace: Al igual que en la serie anterior, el tipo de desenlace era claro, el afecto moría o sobrevivía. Por lo que limpie las categorias en las que habia caracteres delante o detras y las que no podia asignar a ninguna de esas las metia en unknown.

Con estas series limpias y categorizadas el siguiente paso fue hacer un filtro primero por año, para evitar trabajar con ataques demasiado antiguos y poco documentados y empezar a buscar una hipótesis.
En mi caso intento demostrar que el numero de supervivientes es mayor con el paso de los años debido a los avances medicos.

Con la hipótesis clara es el momento de empezar a crear graficas que muestren datos de ataques con el desenlace
