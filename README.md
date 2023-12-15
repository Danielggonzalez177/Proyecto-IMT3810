# Proyecto-IMT3810

## Instalación

Todas las dependencias están manejadas por Poetry. Una vez clonado el repositorio del proyecto, se deben seguir los siguientes pasos:

- Instalar Poetry en Python: ```pip install poetry```
- Correr ```poetry config virtualenvs.in-project true``` para que la carpeta ```.venv``` se cree en la misma carpeta del proyecto.
- Correr ```poetry install``` para instalar todas las dependencias del proyecto.
- Para entrar a la consola del entorno virtual se debe correr ```poetry shell```.

Adicionalmente, es necesario tener la aplicación de Gmsh en el ```PATH``` de nuestro computador. Para realizar lo anterior se pueden seguir los siguientes pasos:

- Descargar Gmsh desde el siguiente [link](https://gmsh.info/#Download).
- El archivo ```.zip``` descargado debe ser extraído en algún directorio de nuestro computador. OJO: es mejor que el path al archivo no contenga carpetas con espacios para evitar problemas en el futuro.
- Una vez extraído el archivo, copiar su path y agregarlo al ```PATH```. En Windows:

  - Ingresar 'editar las variables de entorno' en el buscador de Windows.
  - Clickear en 'Variables de entorno...'
  - Bajo el cuadro de 'Variables del sistema', clickear 'Path' y editar.
  - Agregar nueva variable de entorno y pegar el path de Gmsh. Por ejemplo: ```C:\gmsh-4.11.1-Windows64```.
  - Aceptar todos los cambios.
  - Finalmente, reiniciar el PC para que los cambios hagan efecto.

En VS Code se debe elegir el kernel asociado al entorno virtual ```.venv``` para ejecutar los códigos.

Para probar que el entorno virtual está funcionando bien, se puede correr el ejemplo del archivo ```BEM_Test.ipynb```, el que corresponde a un notebook de ejemplo de la librería Bempp-cl.