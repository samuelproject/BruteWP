# BruteWP

Existe una herramienta muy buena para la auditoría de CMS WordPress, su nombre es Wpscan, esta herramienta permite realizar un análisis de vulnerabilidades para este tipo de gestor de contenidos. Además, esta herramienta permite realizar un ataque de fuerza bruta, el problema radica principalmente en que el ataque de fuerza bruta que hace esta herramienta entrega muchos falsos positivos, por esta razón se comprobó que no es muy fiable al momento de realizar este tipo de ataques.

Por esta razón se desarrolló una herramienta escrita en Python la cual se denominó BruteWP. Esta herramienta permite realizar un ataque de fuerza bruta de manera efectiva y para cualquier versión de WordPress


Usage
----

./BruteWP.py -h 

./BruteWP.py -t [target] -u [user] -w [wordlist] -r [restaurar ataque]      



Screenshots
----


![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9443298/b0aaefb4-4a56-11e5-9197-345ea189f2fc.JPG)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9443294/b0a0dac4-4a56-11e5-928c-bc21ae9d8c57.JPG)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9443293/b09fa118-4a56-11e5-927e-2f419219d907.JPG)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9443295/b0a25084-4a56-11e5-9454-57579c15fb15.JPG)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9443297/b0a51314-4a56-11e5-8ef0-6dadb517d08f.JPG)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/9443296/b0a38bc0-4a56-11e5-9b50-4715eb7072c4.JPG)

Como se puede observar en la imagen anterior, este script  requiere parámetros obligatorios como son, la URL ejemplo : www.mipagina.com/wp-login.php, el username (Para obtener el username se puede utilizar la herramienta Wpscan), y finalmente el diccionario.

Nota Legal
----

Es importante mencionar que este script esta hecho con fines netamente Éticos. No me hago responsable por el mal uso que puedan brindarle.

