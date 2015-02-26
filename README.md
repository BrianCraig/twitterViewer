# twitterViewer
Lector de Tweets por tag en tiempo real, probado en python 2.7 y Django 1.7, la carpeta app es una App independiente
  
Instalación  
-----------
configurar el archivo app.settings.py, ingresando las credenciales de google maps v3 API, y la API de twitter.

instalar dependencias utilizando el comando
> pip install -r requirements.txt
  
Uso  
-----------  
Para iniciarlo de forma local, se debe utilizar estos dos comandos  
> python manage.py runserver

Y luego ir a http://localhost:8080/app/

si se quiere utilizar de forma independiente, se deben copiar los archivos estáticos dentro de la carpeta static a su nuevo proyecto.  
