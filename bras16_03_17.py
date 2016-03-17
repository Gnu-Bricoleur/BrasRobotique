from serial import Serial
from math import *
from PIL import Image
import os

serial_port = Serial(port='/dev/ttyACM0', baudrate=9600)
#serial_port = Serial(port='/dev/ttyUSB1', baudrate=9600)
continuer = True
continuer1 = True
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
rot3 = 0
rot4 = 0
base3 = 0
base4 = 0
seg13 = 0
seg14 = 0
seg23 = 0
seg24 = 0
seg33 = 0
seg34 = 0
i = 0
j = 0

taillesegment = 16.5




def supprerreur (L,resolution,liste):
	i = 0
	if ( liste[0] >= (L/resolution)) :
		liste.insert(0,1)
	if ( liste[-1] <= ((9*L)/resolution)):
		liste.append(L-1)
	while( i < len(liste) - 1 ):
		if ( liste[i+1]-liste[i]<=(L/resolution)):
			liste.pop(i+1)
			i = i + 1
		else:
			i = i + 1
	return liste


def filtre (im3,im2,mat,H,L): #fonction filtre en multipliant la matrice image par une matrice kernel 
	for i in range(H-1):
	
		print i
	
		for j in range (L-1):
	
			if j>=1 and i>=1:
	
				p = im3.getpixel((j,i))
				
				g = im3.getpixel((j-1,i))
				
				d = im3.getpixel((j+1,i))
				
				h = im3.getpixel((j,i-1))
				
				b = im3.getpixel((j,i+1))
				
				hg = im3.getpixel((j-1,i-1))
				
				bg = im3.getpixel((j-1,i+1))
				
				hd = im3.getpixel((j+1,i-1))
				
				bd = im3.getpixel((j+1,i+1))
				
				valP = p[0]*mat[4]
				
				valG = g[0]*mat[1]
				
				valD = d[0]*mat[7]
				
				valH = h[0]*mat[3]
				
				valB = b[0]*mat[5]
				
				valhg = hg[0]*mat[0]
				
				valbg = bg[0]*mat[2]
				
				valhd = hd[0]*mat[6]
				
				valbd = bd[0]*mat[8]
				
				valp = (valG + valD + valH + valB + valP + valhg + valhd + valbd + valbg) /5
				
				im2.putpixel((j,i),(valp,valp,valp))


def detection(photo):

	im1 = Image.open(photo)
	
	L,H = im1.size # L pour largeur H pour hauteur (dim image)
	rouge = []
	coox=[]
	resolution = 10
	seuil = 40
	ortho = [0,L-1]
	orthoy = [0,H-1]
	
	matlaplace = (-1,-1,-1,-1,8,-1,-1,-1,-1)
	matpassebas = (1,1,1,1,4,1,1,1,1)
	matpassehaut = (0,-1,0,-1,5,-1,0,-1,0)
	
	
	im3 = Image.new("RGB",(L,H))
	
	im2 = Image.new("RGB",(L,H))
	
	im4 = Image.new("RGB",(L,H))
	
	
	
	for y in range (H): # y prend une les valeurs de 0 a H (parcours les pixels e la verticale)
	
		for x in range (L):
		
			p = im1.getpixel((x,y)) #la fct getpixel prend les coord du pixel en entree et retourne un tableau de taille 3 avec la valeur des composantes du pixel de 0 a 255 (RGB)
			
			n = (p[0]+p[1]+p[2])/3 # je transforme l'image couleur en noir et blanc (en faisant la somme des valeurs du rouge vert et bleu en les divisant par 3 )
			
			im3.putpixel((x,y),(n,n,n)) # decolorise image 1 dans image 3 (chaque pixel(x,y) prend la valeur moyenne des intensites des couleurs)
	
	
	
	filtre (im3,im2,matlaplace,H,L) # application de matrice Laplacienne 
		
		
	"""filtre ( im2 , im3, matpassehaut)
	im3.show()"""
	
	for y in range (4,H-4): #met l'image en noir ou blanc
		print y
		coox [:] = [] # liste videe pour chaque nouvelle ligne 
		for x in range (L-1):
			gris = im2.getpixel((x,y))       
			if ( gris[0] < seuil ):
				im4.putpixel((x,y),(0,0,0))
			else :
				im4.putpixel((x,y),(255,255,255))
				"""coox.append(x) # coordonees sur X des pixels blanc """
			h = im4.getpixel((x,y))
			if (h[0] == 255):
				a = im4.getpixel((x,(y-1)))
				b = im4.getpixel((x,(y-2)))
				c = im4.getpixel((x,(y-3)))
				d = im4.getpixel((x,(y+1)))
				e = im4.getpixel((x,(y+2)))
				f = im4.getpixel((x,(y+3)))
				if ( a[0] == b[0] == c[0] == 255 or e[0] == d[0] == f[0] == 255  ) :
					if (x  not in ortho and (x-1)  not in ortho and (x-2) not in ortho and (x-3) not in ortho and (x+1) not in ortho and (x+2)  not in ortho and (x+3) not in ortho) :
										  
						ortho.append(x) 
						
		   
	ortho.sort()
	
	supprerreur(L,resolution,ortho)
		#####################################################################################################
	""" if ( len(coox) > 5) : #si il y a plus de 5 pixels blanc sur cette ligne     
			
			i = 0
			while i <= len(coox) - 3   :
				print i
				a =im4.getpixel(((coox[i]),(y-1))) # pixel juste au dessus
				b =im4.getpixel(((coox[i]),(y-2))) # 2 pixels au dessus
				c =im4.getpixel(((coox[i]),(y-3))) # 3
				d =im4.getpixel(((coox[i]),(y+1))) # pixel juste en dessous
				e =im4.getpixel(((coox[i]),(y+2))) # 2 p en dessous
				f =im4.getpixel(((coox[i]),(y+3)))# 3 p en dessous
				if (a[0] == b[0] == c[0] == 255 or e[0] == d[0] == f[0] == 255  ) :
					
					if ( coox[i]  not in ortho ):
						ortho.append(coox[i]) # probable droite perpendiculaire a la droite des x passant par cooxi
						i = i+1
					else:
						i = i+1
				else :
					i = i+1"""
		  #############################################################################################
	print ortho  
	print len(ortho)                 
	for i in ortho :
		for y in range (H-1) :
			im4.putpixel((i,y),(255,0,0))            
	im4.show()           
	
	for x in range (4,L-4): #met l'image en noir ou blanc
		
		for y in range (H-1):
			h = im4.getpixel((x,y))
			if (h[1] == 255):           
				a = im4.getpixel(((x-1),y))
				b = im4.getpixel(((x-2),y)) 
				c = im4.getpixel(((x-3),y))
				d = im4.getpixel(((x+1),y))
				e = im4.getpixel(((x+2),y))
				f = im4.getpixel(((x+3),y))
				if ( a[1] == b[1] == c[1] == 255 or e[1] == d[1] == f[1] == 255  ) :
					if (y not in orthoy and (y-1) not in orthoy and (y+1) not in orthoy and (y+2) not in orthoy ) :
						orthoy.append(y)
						orthoy.sort()
						
			
			
	orthoy.sort() #tri des listes
	print orthoy,ortho
	
	supprerreur(H,resolution,orthoy)    
	supprerreur(H,resolution,orthoy)  
	
	print orthoy  
	print len(orthoy)                 
	for i in orthoy :
		for x in range (L-1) :
			im4.putpixel((x,i),(255,0,0))            
	im4.show()           
	
				
	
	
	
	#for i in ortho :
	 #   for  j in orthoy :
	  #      im4.putpixel((i,j),(0,255,0))
	   #     print  (i,j)
	
		   
	
	
	
	 
	print orthoy,ortho
	if ( len(ortho) >= 4): # distinction de plusieur cas pour la detection des zones 
		if( ortho[2]-ortho[1] > (L/10)): #je m'assure que la zone est suffisament grande pour le passage du bras
			for y in range(orthoy[1]):
				for x in range((ortho[1]),(ortho[2])):
					im1.putpixel((x,y),(0,255,50))
			
		elif(ortho[1]-ortho[0]>ortho[3]-ortho[1]):
			for y in range(orthoy[1]):
				for x in range((ortho[2]),(ortho[3])):
					im1.putpixel((x,y),(0,255,50))
		else:
			for y in range(orthoy[1]):
				for x in range((ortho[0]),(ortho[1])):
					im1.putpixel((x,y),(0,255,50))
			   
	
	
			
	elif (len(ortho) == 3 ):
		if(ortho[1]-ortho[0]<ortho[2]-ortho[1]):
			for y in range(orthoy[1]):
				for x in range((ortho[0]),(ortho[1])):
					im1.putpixel((x,y),(0,255,50))
		else:
			for y in range(orthoy[1]):
				for x in range((ortho[1]),(ortho[2])):
					im1.putpixel((x,y),(0,255,50))
			
	
	im1.show() 
	
	return ortho[1]





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
	yf=input("Position de l'extremitee selon Y |")
	zf=input("Position de l'extremitee selon Z /")
	xf=float(xf)
	yf=float(yf)
	zf=float(zf)
	
	anglealabase = atan(zf/xf)
	print "angle a al base"
	
	anglealabase = int(anglealabase*360/(2*pi))
	print anglealabase
	if anglealabase == abs(anglealabase):
		rot4 = 0
	else :
		rot4 = 1
	anglealabase = abs(anglealabase)
	rot3 = int(anglealabase/100)
	rot2 = int(anglealabase/10)-10*rot3
	rot = int(anglealabase - 10*rot2 - 100*rot3) 	
	
	# Determination obstacle ou pas
	while continuer1 :
		lu = serial_port.readline()
		chaine = lu.decode('ascii')
		print chaine
		if chaine == "rot\r\n":
			serial_port.write(str(rot4).encode('ascii'))
			serial_port.write(str(rot3).encode('ascii'))
			serial_port.write(str(rot2).encode('ascii'))
			serial_port.write(str(rot).encode('ascii'))
		elif chaine == "ultrason\r\n":
			distance = serial_port.readline()
			distance = distance.decode('ascii')
		elif chaine == "base\r\n":
			serial_port.write(str(base4).encode('ascii'))
			serial_port.write(str(base3).encode('ascii'))
			serial_port.write(str(base2).encode('ascii'))
			serial_port.write(str(base).encode('ascii'))
		elif chaine == "seg1\r\n":
			serial_port.write(str(seg14).encode('ascii'))
			serial_port.write(str(seg13).encode('ascii'))
			serial_port.write(str(seg12).encode('ascii'))
			serial_port.write(str(seg1).encode('ascii'))
		elif chaine == "seg2\r\n":
			serial_port.write(str(seg24).encode('ascii'))
			serial_port.write(str(seg23).encode('ascii'))
			serial_port.write(str(seg22).encode('ascii'))
			serial_port.write(str(seg2).encode('ascii'))
		elif chaine == "seg3\r\n":
			serial_port.write(str(seg34).encode('ascii'))
			serial_port.write(str(seg33).encode('ascii'))
			serial_port.write(str(seg32).encode('ascii'))
			serial_port.write(str(seg3).encode('ascii'))
			continuer1 = False
	continuer1 = True
	print distance
	
	hypothenuse = sqrt(xf**2 + yf**2)
	
	if distance < sqrt(hypothenuse**2 - yf**2):
		obstacle = True
		os.system("mplayer -vo png -frames 1 tv:// -tv driver=v4l2:device=/dev/video1")
		h = detection("00000001.png")
		hauteurobstacle = distance*(1/185)*h
	else :
		obstacle = False
	
	
	if obstacle == False:
		teta1 ,teta2 = deuxsegments(taillesegment*2,xf,yf,zf,0,0,0)
		print teta1, teta2
		#Sans obstacles
		teta1 = int(teta1)
		teta2 = int(teta2)
		if teta1 == abs(teta1):
			base4 = 0
		else :
			base4 = 1
		if teta2 == abs(teta2):
			seg24 = 0
		else :
			seg24 = 1
		teta1 = abs(teta1)
		teta2 = abs(teta2)
		base3 = int(teta1/100)
		base2 = int(teta1/10)-10*base3
		base = int(teta1 - 10*base2 - 100*base3) 
		seg23 = int(teta2/100)
		seg22 = int(teta2/10)-10*seg23
		seg2 = int(teta2 - 10*seg22 - 100*seg23) 
		
		print "les angles sont"
		print base4,base3,base2,base
		print seg24 ,seg23, seg22,seg2
	elif obstacle == True:
		teta1 ,teta2 = deuxsegments(taillesegment,xf,yf,zf,distance,hauteurobstacle+5,zf)
		print teta1, teta2
		#Sans obstacles
		teta1 = int(teta1)
		teta2 = int(teta2)
		if teta1 == abs(teta1):
			seg24 = 0
		else :
			seg24 = 1
		if teta2 == abs(teta2):
			seg34 = 0
		else :
			seg34 = 1
		teta1 = abs(teta1)
		teta2 = abs(teta2)
		seg23 = int(teta1/100)
		seg22 = int(teta1/10)-10*seg23
		seg2 = int(teta1 - 10*seg22 - 100*seg23) 
		seg33 = int(teta2/100)
		seg32 = int(teta2/10)-10*seg33
		seg3 = int(teta2 - 10*seg32 - 100*seg33) 
		
		print "les angles sont"
		print seg24,seg23,seg22,seg2
		print seg34,seg33,seg32,seg3
		
		teta1 ,teta2 = deuxsegments(taillesegment,distance,hauteurobstacle+5,zf,0,0,0)
		print teta1, teta2
		#Sans obstacles
		teta1 = int(teta1)
		teta2 = int(teta2)
		if teta1 == abs(teta1):
			base4 = 0
		else :
			base4 = 1
		if teta2 == abs(teta2):
			seg14 = 0
		else :
			seg14 = 1
		teta1 = abs(teta1)
		teta2 = abs(teta2)
		base3 = int(teta1/100)
		base2 = int(teta1/10)-10*base3
		base = int(teta1 - 10*base2 - 100*base3) 
		seg13 = int(teta2/100)
		seg12 = int(teta2/10)-10*seg13
		seg1 = int(teta2 - 10*seg12 - 100*seg13) 
		
		print "les angles sont"
		print base4,base3,base2,base
		print seg14 ,seg13, seg12,seg1
		
		
		
		
	
	while continuer1 :
		lu = serial_port.readline()
		chaine = lu.decode('ascii')
		print chaine
		if chaine == "rot\r\n":
			serial_port.write(str(rot4).encode('ascii'))
			serial_port.write(str(rot3).encode('ascii'))
			serial_port.write(str(rot2).encode('ascii'))
			serial_port.write(str(rot).encode('ascii'))
		elif chaine == "ultrason\r\n":
			distance = serial_port.readline()
			distance = distance.decode('ascii')
		elif chaine == "base\r\n":
			serial_port.write(str(base4).encode('ascii'))
			serial_port.write(str(base3).encode('ascii'))
			serial_port.write(str(base2).encode('ascii'))
			serial_port.write(str(base).encode('ascii'))
		elif chaine == "seg1\r\n":
			serial_port.write(str(seg14).encode('ascii'))
			serial_port.write(str(seg13).encode('ascii'))
			serial_port.write(str(seg12).encode('ascii'))
			serial_port.write(str(seg1).encode('ascii'))
		elif chaine == "seg2\r\n":
			serial_port.write(str(seg24).encode('ascii'))
			serial_port.write(str(seg23).encode('ascii'))
			serial_port.write(str(seg22).encode('ascii'))
			serial_port.write(str(seg2).encode('ascii'))
		elif chaine == "seg3\r\n":
			serial_port.write(str(seg34).encode('ascii'))
			serial_port.write(str(seg33).encode('ascii'))
			serial_port.write(str(seg32).encode('ascii'))
			serial_port.write(str(seg3).encode('ascii'))
			continuer1 = False

