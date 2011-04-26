requerimientos

Python 2.6, el sistema esta configurado para usar sqlite3

construccion del proyecto

el proyecto usa buildout para construir el paquete y bajar las dependencias

la secuencia de comandos en Linux seria:

python bootstrap -d
bin/buildout -vvv
bin/django runserver


el recipe usado para soportar un proyecto django es una variacion del djangorecipe, igual genera un bin/django q remplaza al manage.py comun en todo proyecto django generado normalmente.

--
Yonsy Solis
