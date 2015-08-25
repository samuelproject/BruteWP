# BruteWP

Existe una herramienta muy buena para la auditoría de CMS WordPress, su nombre es Wpscan, esta herramienta permite realizar un análisis de vulnerabilidades para este tipo de gestor de contenidos. Además, esta herramienta permite realizar un ataque de fuerza bruta, el problema radica principalmente en que el ataque de fuerza bruta que hace esta herramienta entrega muchos falsos positivos, por esta razón se comprobó que no es muy fiable al momento de realizar este tipo de ataques.

Por esta razón se desarrolló una herramienta escrita en Python la cual se denominó BruteWP. Esta herramienta permite realizar un ataque de fuerza bruta de manera efectiva y para cualquier versión de WordPress


Usage
----

./BruteWP.py -h 

./BruteWP.py -t [target] -u [user] -w [wordlist] -r [restaurar ataque]      



Screenshots
----


![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9469601/65fcc94c-4b1e-11e5-8362-50968127ae0e.JPG)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9444491/73bf481e-4a5d-11e5-920b-21886337e2f3.JPG)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9443293/b09fa118-4a56-11e5-927e-2f419219d907.JPG)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9443295/b0a25084-4a56-11e5-9454-57579c15fb15.JPG)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9444763/db527b4e-4a5e-11e5-95ce-47b6e384772b.JPG)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9443296/b0a38bc0-4a56-11e5-9b50-4715eb7072c4.JPG)

Como se puede observar en la imagen anterior, este script  requiere parámetros obligatorios como son, la URL ejemplo : www.mipagina.com/wp-login.php, el username (Para obtener el username se puede utilizar la herramienta Wpscan), y finalmente el diccionario.

El valor agregado que posee esta herramienta, es que si se desea pausar el escaneo, es posible reanudarlo en cualquier momento con la opción -r, esto es muy útil, ya que así se podrá continuar con la auditoría sin ningún problema.

Nota Legal
----

Es importante mencionar que este script está hecho con fines netamente Éticos. No me hago responsable por el mal uso que puedan brindarle.


Contacto
----
Para contactarse conmigo [@saamux](https://twitter.com/saamux) con cualquier pregunta o característica que les gustaría ver en la próxima actualización.

