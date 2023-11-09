# stateCompanyDocker

## Introducción
Este es uno de los dos proyectos realizados para esta prueba, con la configuración de docker compose.

# Descripción Proyecto
An enormous Real Estate company going to require create an API to get in information about 
properties at United States, you must use ER such us next image. Your task it will create follow 
services:

a) Create Property Building

b) Add Image from property

c) Change Price


# Arquitectura del proyecto

- Version python: Python 3.11.5
- Entorno virtual: virtualenv 20.24.6
- Nombre del Proyecto: stateCompany
  - Version FastApi: 0.104.1 
  - pymongo --> base de datos mongo 4.5.0
  - Docker version 24.0.5
  - Archivo requirements.txt: Contenido de las librerias utilizadas

$\color{red}{Nota:}$\
   $\color{red}{\  * El\ proyecto\ se\ crea\ con\ una\ base\ de\ datos\ MONGO,\ nombre\ de\ la\ base\ de\ datos\ "state_company"\ sin\ usuario\ y\ contraseña.}$\
   $\color{red}{\  * Se\ crea\ una\ carpeta\ con\ nombre\ mermaiddb,\ la\ cual\ contiene\ el\ MER,\ de\ la\ base\ de\ datos.}$


## *Puesta en marcha del proyecto*
#### PASO 1:
*clonar el proyecto desde https://github.com/edimoredev/state_company_docker*

![image](https://github.com/edimoredev/state_company_docker/assets/125479887/6a87520c-e46d-4016-849b-6f44b72fd628)
#### PASO 2:
*descargar y instalar docker compose desde https://docs.docker.com/desktop/install/windows-install/*

![image](https://github.com/edimoredev/state_company_docker/assets/125479887/8626b818-9b6d-452c-9334-f447825ba036)
#### PASO 3:
*abrir docker desktop*

![image](https://github.com/edimoredev/state_company_docker/assets/125479887/2bc97b13-170c-4e6a-8bc4-eb065e5d904c)
#### PASO 4:
*Ingresamos a la ruta donde esta el archivo docker-compose.yml y ejecutar el siguiente comando  docker-compose up --build*
  
![image](https://github.com/edimoredev/state_company_docker/assets/125479887/5469bf25-0940-448d-924f-9689e5acd5cc)
#### PASO 5:
*Ingresamos al docker desktop y vemos la imagen*

![image](https://github.com/edimoredev/state_company_docker/assets/125479887/c965b249-3561-4de6-8298-22979bc5648d)

#### PASO 6:
*Verificar en el navegador localhost url http://localhost:8000/docs SWAGER*

![image](https://github.com/edimoredev/state_company_docker/assets/125479887/afb9bfd1-9886-4aba-b7ba-e0f30833120d)

#### PASO 7 Test:
*Realizamos un metodo POST del collect owner, property, propertyImage, propertyTrace con su respuesta*

![image](https://github.com/edimoredev/state_company_docker/assets/125479887/c9adafc7-f679-44e9-8032-e0c5e9ce45c1)
#### PASO 8:
*Realizamos pruebas unitarias, en este caso pytest ejemplo owner para ello se realiza lo siguiente*

1. En consola ejecutar el siguiente comando "docker-compose ps", saber los contenedores que estan ejecución
   
![image](https://github.com/edimoredev/state_company_docker/assets/125479887/35c2baa0-d738-47c8-acf7-712033cc70bb)
2. luego "docker exec -it nombre del doker /bin/sh" --> docker exec -it app-app-1 /bin/sh, para saber si estamos en el repositorio 

![image](https://github.com/edimoredev/state_company_docker/assets/125479887/581f9b8e-4de1-4c37-91b8-393afcd5080f)
3. Ingresamos a test para realizar las pruebas

![image](https://github.com/edimoredev/state_company_docker/assets/125479887/280807f5-a8a7-46f5-bc67-2a97d49f9879)
4. se realiza la prueba ejemplo owner 
![image](https://github.com/edimoredev/state_company_docker/assets/125479887/a44153c5-2b4c-410a-ad96-f1cba74293cb)





### *Agradecimientos a la empresa Million and Up*










