import ctypes
import os,sys, time

#golobal vars
def_theme = 'matrix'

#main soft
print os.path.dirname(__file__)
SPI_SETDESKWALLPAPER = 20 
for i in range(1,151):
    time.sleep(0.04)
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, os.path.dirname(__file__)+"/themes/"+def_theme+"/"+str(i)+".jpg" , 0)
    file = open('config.ini','r')
    lines  = file.read().splitlines()
    print lines
    if lines[1]== "off":
        print "exit"
        break
    print 'i='+str(i)
    file.close() 
sys.exit(1)


