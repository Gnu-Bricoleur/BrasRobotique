from serial import Serial
from math import *

serial_port = Serial(port='/dev/ttyACM0', baudrate=9600)

continuer = True

rot = 0
rot2 = 0
base = 0
base2 = 0
seg1 = 0
seg12 = 0
seg2 = 0
seg22 = 0
seg3 = 0
seg32 = 0
i = 0
j = 0

taillesegment = 16.5



def deuxsegments(taillesegment,xf,yf,zf,xo,yo,zo):
	#calcul du premier angle teta1 =  90 - teta11 - teta111
	distanceorigineextremite = sqrt((xf-xo)**2 + (yf-yo)**2)
	print distanceorigineextremite
	teta11 = atan((yf-yo)/(xf-xo))
	teta11 = (teta11*360)/(2*pi)
	print teta11
	teta111 = acos((distanceorigineextremite)/(2*taillesegment))
	teta111 = (teta111*360)/(2*pi)
	print teta111
	teta1 = 90 - teta11 - teta111
	# calcul du deuxieme angle teta2 = 180 - teta22 - teta22
	teta22 = asin((distanceorigineextremite)/(2*taillesegment))
	teta22 = (teta22*360)/(2*pi)
	print teta22
	teta2 = 180 - 2*teta22
	return teta1, teta2




while continuer:
	xf=input("Position de l'extremitee selon X _")
	yf=input("Position de l'extremitee selon Y /")
	zf=input("Position de l'extremitee selon Z |")
	xf=float(xf)
	yf=float(yf)
	zf=float(zf)
	teta1 ,teta2 = deuxsegments(taillesegment*2,xf,yf,zf,0,0,0)
	print teta1, teta2
	
	
	#Sans obstacles
	teta1 = int(teta1)
	teta2 = int(teta2)
	base2 = int(teta1/10)
	base = int(teta1 - 10*base2) 
	seg22 = int(teta2/10)
	seg2 = int(teta2 - 10*seg22) 
	
	
	
	while continuer :
		lu = serial_port.readline()
		chaine = lu.decode('ascii')
		print chaine
		if chaine == "rot\r\n":
			serial_port.write(str(rot2).encode('ascii'))
			serial_port.write(str(rot).encode('ascii'))
		elif chaine == "base\r\n":
			serial_port.write(str(base2).encode('ascii'))
			serial_port.write(str(base).encode('ascii'))
		elif chaine == "seg1\r\n":
			serial_port.write(str(seg12).encode('ascii'))
			serial_port.write(str(seg1).encode('ascii'))
		elif chaine == "seg2\r\n":
			serial_port.write(str(seg22).encode('ascii'))
			serial_port.write(str(seg2).encode('ascii'))
		elif chaine == "seg3\r\n":
			serial_port.write(str(seg32).encode('ascii'))
			serial_port.write(str(seg3).encode('ascii'))




