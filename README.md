# Proyecto Final Bermudez+Lucas+50210 - Football Blog

## Link al video mostrando la página
https://youtu.be/tQpQjnQ3k00

## Asegurarse de tirar los siguientes comandos para crear las bases de datos:
1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py runserver` para correr el servidor


## URLS:
Las urls a las que tenemos que entrar manualmente son:
1. 'admin/'
2. 'PageApp/'

Luego a las demás, se puede entrar por hipervínculos!!

## Superuser:
User : Admin
Password : 1234

## Modelos:
Tenemos 4 modelos principales:
1. Jugador
   Podemos indicarle nombre, país, posición y equipo.
2. Equipo
   Podemos indicarle nombre, país, liga y división.
3. Liga
   Podemos indicarle nombre, país y división.
4. Torneo
   Podemos indicarle nombre y cantidad de equipos.

## Funcionalidad:
1. Registro
2. Iniciar Sesión
3. Cerrar Sesión
4. Editar Usuario
5. Agregar Avatar


6.Ver/Crear/Editar/Eliminar/Buscar
- Jugadores
- Equipos
- Ligas
- Torneos

Cada uno yendo a su correspondiente página en la barra de navegación.

## Orden:
El registro, inicio, etc tiene un orden intuitivo.

Para crear, ver, editar, etc a los modelos, podemos hacerlo en el orden que se quiera, teniendo en cuenta cosas como que no vamos a poder editar un jugador que no existe!
