"""
================= FLAG : jaimlefr0m4g =================
"""
import math
import os
import socket
import time

"""
I share here this script that required a lot of effort to understand and make it a success. 
I put it here in the hope of helping others to understand it. 
However, I have modified it so as not to divulge the solution. 
Good Luck 
"""

def envoie_psmg():
    while 1:
        bot.send(b"PRIVMSG " + enemy + b" :!ep1\n")
        if message.find(enemy) > -1:  # Verifier que l'on reçoie le bon message
            message = message[(message[1:].find(b":")) + 2:]  # géré le message pour obtenir
            message = message[:message.find(b".")]  # la forme message = "nb1/nb2"
            nb1 = int(message[:message.find(b"/")])  # stocker le nb1
            nb2 = int(message[(message.find(b"/")) + 1:])  # stocker le nb2
            answer = round(math.sqrt(nb1) * nb2, 2)  # calculer la réponse
            # envoyer la réponse
            bot.send(b"PRIVMSG " + enemy + b" :!ep1 -rep " + bytes(str(answer).encode("ASCII")) + b"\r\n")
            bot.send(b"Au revoir !")  # Dire au revoir au bot
            break


host = "irc.root-me.org"  # Challenge's IRC server
port = 6667  # Connection port
channel = b"#Root-Me_Challenge"  # Challenge's channel
enemy = b"Candy"  # Challenge's bot

try:
    print("[+] Création du socket")
    bot = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    print("[+] Connection en cours --> %s:%d" % (host, port))
    bot.connect((host, port))
except:
    print("[!] Connexion impossible")

else:
    print("[+] Envoie du nom")
    bot.send(b"NICK Gone716\n")
    print("[+] Envoie de la cmd user")
    bot.send(b"USER Gone716 irc.root-me.org root-me : ChallengeBot")
    print("[+] Join", channel)
    bot.send(b"JOIN " + channel)
    print("[+] Envoie de la requète en cours...")

print("[+] Challenge terminé")
bot.close()