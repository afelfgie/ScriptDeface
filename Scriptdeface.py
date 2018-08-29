#!/system/bin/python
# -*- coding: utf-8 -*-

import random
import time
import unittest

import os, sys, subprocess
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def slowprint2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

#color
underlined='\033[04m'
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
lightgreen='\e[1;32m'
okegreen='\033[92m'
bold='\033[33;1m'

# console colors
W = '\033[37;1m' #white
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

class color:
        P    =  '\033[95m' # purple
        B    =  '\033[94m' # Blue
        BOLD =  '\033[1m'  # Bold
        G    =  '\033[92m' # Green
        Y    =  '\033[93m' # Yellow
        R    =  '\033[91m' # Red
        W    =  '\033[97m' # White
        BL   =  '\033[90m' # Black
        M    =  '\033[95m' # Magenta
        C    =  '\033[96m' # Cyan
        ENDC =  '\033[0m'  # end colors

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    YELLOW = '\033[10m'
    ITALIC = '\033[2m'
    PURPLE = '\033[40m'

# Just some colors and shit
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'


import os
import sys
import time
if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
print B + " ____            _       _  \033[91m ____        __"
print B + "/ ___|  ___ _ __(_)_ __ | |_\033[91m|  _ \  ___ / _| __ _  ___ ___"
print B + "\___ \ / __| '__| | '_ \| __\033[91m| | | |/ _ \ |_ / _` |/ __/ _ \ "
print B + " ___) | (__| |  | | |_) | |_\033[91m| |_| |  __/  _| (_| | (_|  __/"
print B + "|____/ \___|_|  |_| .__/ \__\033[91m|____/ \___|_|  \__,_|\___\___|"
print B + "                  |_|"
print
print """
\033[34;1m[===========================>
\033[92m [+]\033[33;1mAuthor \033[91m: \033[36;1mGunadiCBR
\033[92m [+]\033[33;1mCode   \033[91m: \033[36;1mpython
\033[92m [+]\033[33;1mTeam   \033[91m: \033[36;1mMls18hckr
\033[34;1m[===========================>"""
print
print "\033[34;1m~\033[91m{\033[93m01\033[91m}\033[34;1m~\033[37;1mMulai"
print "\033[34;1m~\033[91m{\033[93m02\033[91m}\033[34;1m~\033[37;1mInformasi Tools Ini"
print "\033[34;1m~\033[91m{\033[93m00\033[91m}\033[34;1m~\033[37;1mKeluar"
print
aa = '"'
menu = raw_input("\033[92mPilih Nomor\033[91m-->\033[36;1m ")

try:
   file = open("FuckYou.html", 'w')
except(IOError):
   print ("ERR...")
   sys.exit()

if menu == '1' or menu == '01':
  os.system("clear")
  print
  defstyletitle_simple = raw_input("\033[36mTitle:\033[37;1m ")
  defstyleimage_src = raw_input("\033[36mLink/Image:\033[37;1m ")
  defstyleimage_width = raw_input("\033[36mLebar:\033[37;1m ")
  defstyleimage_height = raw_input("\033[36mTinggi:\033[37;1m ")
  defstylehacked_simple = raw_input("\033[36mHacked by:\033[37;1m ")
  defstylemessage_simple = raw_input("\033[36mPesan:\033[37;1m ")
  defstyleteam_simple = raw_input("\033[36mNama Team:\033[37;1m ")
  time.sleep(1.90)
  print
  slowprint2("\033[36;1m[+]\033[37;1mDONE...")
  time.sleep(0.90)
  slowprint("\033[36;1m[+]\033[37;1mScript Berhasil Dibuat...")
  print
  time.sleep(2)
  a = '"center"'
  aaa = '"#111111"'
  b = '"100%"'
  bb = '""'
  c = '"0"'
  d = '"align"'
  e = '"#000000"'
  f = '"10"'
  gg = '"1"'
  h = '"#ffffff"'
  hh = '"#b21f25"'
  hhh = '"#333333"'
  
  file.write(" <body bgcolor=black>\n")
  file.write("\n")
  file.write("<br><title>"+defstyletitle_simple+"</title></br>\n")
  file.write("<td><div align="+a+">\n")
  file.write("</div>        <table width="+b+" border="+c+" cellpadding="+c+" cellspacing="+c+">\n")
  file.write("          <tbody><tr>\n")
  file.write("     <center><img src="+aa+""+defstyleimage_src+""+aa+" alt="+bb+" width="+aa+""+defstyleimage_width+""+aa+" height="+aa+""+defstyleimage_height+""+aa+" align="+d+"></a></center>\n")
  file.write("          </tr>\n")
  file.write("        </tbody></table>\n")
  file.write("<table width="+b+" bgcolor="+e+" border="+c+" cellpadding="+f+" cellspacing="+gg+">\n")
  file.write("\n")
  file.write("  <tbody><tr bgcolor="+h+">\n")
  file.write("    <td bgcolor="+h+"><center><b><font color="+hh+">Hacked By "+defstylehacked_simple+"</font></b></center></td>\n")
  file.write("\n")
  file.write("  </tr>\n")
  file.write("\n")
  file.write("  <tr bgcolor="+hhh+">\n")
  file.write("    <td bgcolor="+aaa+"><center><center><font color="+hh+"><b><br>"+defstylemessage_simple+"</center>\n")
  file.write("      <br><center>"+defstyleteam_simple+"</b></center>\n")
  file.write("\n")
  file.write("\n")
  file.write("   </td></tr><tr bgco")
  key = raw_input("\033[36;1mPencet \033[33;1mENTER \033[36;1mUntuk Kembali Ke Menu")
  os.system("python2 Scriptdeface.py")

if menu == '2' or menu == '02':
  os.system("clear")
  print "\033[31m"
  os.system("figlet ScriptDeface")
  print "\033[34;1m|=========================================>"
  print "\033[1;33m[+]Nama Tool : \033[1;32mSateSpam"
  print "\033[01;33m[+]Author   : \033[1;32mGunadiCBR"
  print "\033[01;33m[+]Contack  : \033[1;32m085341899229"
  print "\033[01;33m[+]Version  : \033[1;32m1.2"
  print "\033[01;33m[+]Date     : \033[1;32m17-08-2018"
  print "\033[01;33m[+]code     : \033[1;32mpython"
  print "\033[01;33m[+]Team     : \033[1;32mMls18Hckr"
  print "\033[1;33m[-]Spesial Thanks To:"
  print "\033[01;32m 1. afel"
  print "\033[01;32m 2. ayam"
  print "\033[01;32m 3. anjing"
  print "\033[01;32m[+]And All Member Mls18hckr"
  print "\033[34;1m|=========================================>"
  print "\033[37;1m"
  key = raw_input("Pencet ENTER Untuk Kembali Ke Menu")
  os.system("python2 Scriptdeface.py")
if menu == '0':
  print
  print
  print P + "By...By...:)"
  time.sleep(1.49)
  print W + "[-]Exiting...:)"
  sleep(3)
  sys.exit()
else:
	print
        print R + "[!]WRONG INPUT[!]"
        time.sleep(0.15)
        restart_program()

