from discord_webhook import DiscordWebhook
import string
import random
import os
import requests
from urllib.request import urlopen
from colorama import init, Fore,  Back,  Style
import time


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
cls()
title = """
███    ██ ██ ████████ ██   ██  █████  ████████ 
████   ██ ██    ██    ██  ██  ██   ██    ██    
██ ██  ██ ██    ██    █████   ███████    ██    
██  ██ ██ ██    ██    ██  ██  ██   ██    ██    
██   ████ ██    ██    ██   ██ ██   ██    ██    
Nitro Code Checker and Generator Opensource
"""

print(title)
time.sleep(2)
print(Fore.GREEN + "Developed By Katast - Inspirated By logicguy1" + Fore.WHITE)

spamurl = input("Configura una Webhook (url): ")
webhookurl = DiscordWebhook(url=spamurl, content="Webhook Configurada.", username="NitKat [ NITRO GEN ]", avatar_url="https://media.discordapp.net/attachments/935362744302059550/1027341431033040946/imagen.png").execute()
code = string.ascii_letters

def rand_pass(size):
    generate_pass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
                          
    return generate_pass
file = open("nitro.txt", "w")
    

print("Started. CTRL + C para parar.")
resp2 = input("¿Deseas checkear los nitros? (y/n): ")
if resp2 == "y":
  print("Genial. Los nitros ahora se " + Fore.GREEN + "Checkearan")
  xeck = "true"
else:
  print(Fore.RED + "No se checkearan los nitros..")
  xeck = "false"
  
resp = input("Deseas Guardar los nitros en un .txt? (y/n): ")
if resp == "y":
  print("Los archivos se guardaran en un txt con el nombre de" + Fore.GREEN + " nitro.txt")
  crear = "true"
else:
  print(Fore.RED + "No se guardaran los nitros.")
  crear = "false"
  
if xeck == "false":
  maxamount = input("¿Cuantos codigos deseas generar?: ")


def checkerNotW():
  nitro = rand_pass(16)
  url = "https://discordapp.com/api/v9/entitlements/gift-codes/"+nitro+"?with_application=false&with_subscription_plan=true"
  response = requests.get(url)
  respuesta = response.status_code
  if response.status_code == "404":
    print(Fore.GREEN + "[Nitro Valido] " + Fore.WHITE + "https://discord.gift/" + nitro)
    webhookurl = DiscordWebhook(url=spamurl, content="@everyone Valido: https://discord.gift/" + nitro, username="NitKat [ NITRO GEN ]", avatar_url="https://media.discordapp.net/attachments/935362744302059550/1027341431033040946/imagen.png").execute()
    valid = 1 + valid
  else:
    print(Fore.RED+ "[Nitro Invalido] " + Fore.WHITE + "https://discord.gift/" + nitro)
    
    
    
    
    
def checkerWrite():
  nitro = rand_pass(16)
  url = "https://discordapp.com/api/v9/entitlements/gift-codes/"+nitro+"?with_application=false&with_subscription_plan=true"
  response = requests.get(url)
  respuesta = response.status_code
  if response.status_code == "404":
    print(Fore.GREEN + "[Nitro Valido] " + Fore.WHITE + "https://discord.gift/" + nitro)
    webhookurl = DiscordWebhook(url=spamurl, content="@everyone Valido: https://discord.gift/" + nitro, username="NitKat [ NITRO GEN ]", avatar_url="https://media.discordapp.net/attachments/935362744302059550/1027341431033040946/imagen.png").execute()
    file.write("https://discord.gift/" + nitro + os.linesep)
    valid = 1 + valid
  else:
    print(Fore.RED+ "[Nitro Invalido] " + Fore.WHITE + "https://discord.gift/" + nitro)
    file.write("https://discord.gift/" + nitro + os.linesep)
    
    
try:
  if xeck == "true":
    
    if crear == "true":
      while 1:
        checkerWrite()
    else:
      while 1:
        checkerNotW()
  
  
  if xeck == "false":
    i = 1
    
    def write():
        file.write("https://discord.gift/" + nitro + os.linesep)
        
    if crear == "true":
      while int(i) < int(maxamount):
        nitro = rand_pass(16)
        print(Fore.RED + "[ " + str(i) + "/" + maxamount + " ]" + Fore.WHITE + " https://discord.gift/" + nitro)
        file.write("https://discord.gift/" + nitro + os.linesep)
        if str(1) == maxamount:
          webhook = DiscordWebhook(url=spamurl, content="**Gracias por usar esta herramienta. Considera Apoyarme** https://github.com/Katast666", username="NitKat [ NITRO GEN ]", avatar_url="https://media.discordapp.net/attachments/935362744302059550/1027341431033040946/imagen.png")
          webhook.execute()
          break
        i = 1 + i
    else:
      while int(i) < int(maxamount):
        nitro = rand_pass(16)
        print(Fore.RED + "[ " + str(i) + "/" + maxamount + " ]" + Fore.WHITE + " https://discord.gift/" + nitro)
        if str(1) == maxamount:
          webhook = DiscordWebhook(url=spamurl, content="**Gracias por usar esta herramienta. Considera Apoyarme** https://github.com/Katast666", username="NitKat [ NITRO GEN ]", avatar_url="https://media.discordapp.net/attachments/935362744302059550/1027341431033040946/imagen.png")
          webhook.execute()
          break
        i = 1 + i
except KeyboardInterrupt:
  print(Fore.RED + "El Proceso ha Terminado")
  webhook = DiscordWebhook(url=spamurl, content="**Gracias por usar esta herramienta. Considera Apoyarme** https://github.com/Katast666", username="NitKat [ NITRO GEN ]", avatar_url="https://media.discordapp.net/attachments/935362744302059550/1027341431033040946/imagen.png")
  webhook.execute()
  
  
