#!/usr/bin/python
#Script para la raspberry que consulta su ippublica actual y usando la clase Email la envia a mi correo
#Esta script se ejecuta cada minuto comprobando contra un fichero (lastIp.txt) si la ip ha cambiado para enviar el mensaje
import os
from Email import Email

nombreFicheroIp = "resources/lastIp.txt"
ip = os.popen('curl icanhazip.com').read()
lastIp = open(nombreFicheroIp).read()
if (lastIp != ip):
    open(nombreFicheroIp, "w").write(ip)
    email = Email()
    email.asunto = 'IpPublica ' + ip
    email.send_mail()
