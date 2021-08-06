# ExamenAD1
LOCATION
1. Empezamos con el location donde debemos de ejecutar ciudad por ciudad el scrip 1.py agregando nuestras propias API keys y token para su respectivo funcionamiento




1.1 Tambien implementaremos una clase listener la cual nos generara un id unico para almacenar nuestros datos recolectados, al igual q tambien tendremos que agragar la autentificacion de los parametros establecidos

![image](https://user-images.githubusercontent.com/66786471/127721750-b90d4f35-9ecf-4d61-9353-241f67057590.png)

1.2 Procederemos a la conexion y creacion de nuestra base de datos en CouchDB y por ultimo implementamos el filtro location para poder asi buscar en una zona en especifico

![image](https://user-images.githubusercontent.com/66786471/127721819-9d23b3a2-03e9-41cd-809a-293373dae9b9.png)

1.3 En nuestro CouchDB podremos observar la conexion y creacion de la DB

![image](https://user-images.githubusercontent.com/66786471/127721867-3f4a729e-3079-4026-b831-06c0413e1ed0.png)

1.4 Ahora procederemos a hacer un filtro desde el CoushDB para que nos muestre solo informacion relacionada con los Juegos olimpicos


1.5 Y asi podremos obtener los usuarios relacionados con el #Olympics


TRACK

2. Para este ejercicio usaremos el mismo scrip con la diferencia de que aumentaremos el filtro track para que su busqueda sea mas profunda y solo sea respecto a temas de los Juegos Olimpicos.

![image](https://user-images.githubusercontent.com/66786471/127723121-08b3bcd1-2b19-406e-9bc3-16c9551494ec.png)

2.1Se generara nuestra DB en el CouchDb donde obtuvimos la informacion

![image](https://user-images.githubusercontent.com/66786471/127723200-bb4dadba-a7af-4064-8ade-537cc4d7929b.png)


TIKTOK

5. En este parametro usaremos tiktok-scraper que nos ayudara a crear un documento csv, para ello mediante consola ingresaremos a una carpeta TikTok (previamente creada) y dentro de lla ejecutaremos el comando junto con el nombre del usuario del cual se esta recolectando la informacion y cual sera el formato deseado que en este caso es csv

![image](https://user-images.githubusercontent.com/66786471/127723983-62d26de8-5394-4d4f-b127-ad073a61baaa.png)


COUCHDB A MONGODB

7. Para ello generamos el JSON desde nuestro CouchDBen la parte superior izquierda

![image](https://user-images.githubusercontent.com/66786471/127725027-75614440-103e-4644-970a-c6fcf7d54478.png)

7.1 Procedemos a copiar el archivo JSON en un bloc de notas y lo guardamos con la terminacion .csv

![image](https://user-images.githubusercontent.com/66786471/127725122-727e03fc-e787-4d82-9d2f-363e7f445b0e.png)

7.2 Acontinuacion en MongoDB creamos las bases de datos y luego procedemos a subir los archivos JSON

![image](https://user-images.githubusercontent.com/66786471/127725215-1b8e2f31-ca87-4a70-bf1e-d31336621dea.png)

![image](https://user-images.githubusercontent.com/66786471/127725271-931e9c57-0573-4d6e-9210-485229d4ecfd.png)


MONGODBATALS

8. Para este preoceso procederemos a conectarnos mediante Atlas a nuestro Compass

![image](https://user-images.githubusercontent.com/66786471/127725341-92595c30-9c6f-4cc5-8487-7521b277790c.png)


![image](https://user-images.githubusercontent.com/66786471/127725373-804b02fa-5522-4b57-be69-6b0ac3b65b44.png)

