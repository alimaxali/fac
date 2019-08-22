g='\033[1;32m'
p='\033[1;35m'
c='\033[1;36m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
reset='\033[0m'
y='\033[1;33m'
from os import system as gg
import time
sb = input("passwoed ")
if sb == "999":
 f = open("max.txt", "r")
 for i in f:

  print (g + "good" + c + "------> " + y + i)
  time.sleep(4)
  s = input("entar")
  gg("payload")
else:
  print "erorr"
  time.sleep(3)
  gg("payload")
