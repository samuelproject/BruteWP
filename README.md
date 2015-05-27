# BruteWP

Existe una herramienta muy buena para la auditoría de CMS WordPress, su nombre es Wpscan, esta herramienta permite realizar un análisis de vulnerabilidades para este tipo de gestor de contenidos. Además, esta herramienta permite realizar un ataque de fuerza bruta, el problema radica principalmente en que el ataque de fuerza bruta que hace esta herramienta entrega muchos falsos positivos, por esta razón se comprobó que no es muy fiable al momento de realizar este tipo de ataques.

Por esta razón desarrollé una herramienta escrita en Python la cual denonime BruteWP, esta herramienta permite realizar un ataque de fuerza bruta de manera efectiva y para cualquier versión de WordPress


Usage
----

./BruteWP.py -h 

./BruteWP.py -t [target] -u [user] -w [wordlist]      



Screenshots
----


![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/7840622/aabf92cc-046e-11e5-9947-c74ee0f06d83.png)

![ScreenShot] (https://cloud.githubusercontent.com/assets/12612092/7840776/5ef00614-046f-11e5-974a-4d74f67993b6.png)



Como se puede observar en la imagen anterior, este script  requiere parámetros obligatorios como son, la URL ejemplo : www.mipagina.com/wp-login.php, el username (Para obtener el username se puede utilizar la herramienta Wpscan), y finalmente el diccionario.

Nota Legal
----

Es importante mencionar que este script esta hecho con fines netamente Éticos. No me hago responsable por el mal uso que puedan brindarle.

