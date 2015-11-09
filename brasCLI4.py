#!/usr/bin/python3
# -*- coding: Utf-8 -*-
from math import *
import pygame
from pygame.locals import *

def repereun(x,y):
	return((x+20,))





continuer=1

taillesegment=15
#marge entre moteur D et obstacle
marge=5
epaisseurobstacle=5
xa,ya,xb,yb,xc,yc,xd,yd,xe,ye,xf,yf,zf=0,0,0,0,0,0,0,0,0,0,0,0,0
aa,ab,ac,ad,ae,af=0,0,0,0,0,0
xo,yo,zo=0,0,0

#grossissemnet
g=7

print("######################################################################")
print("Calcul des angles pour les servomoteurs d'un bras robotique 4 segments")
print("Les conventions utilisees sont les suivantes :")
print("   - les distances sont en centimetres et les segments font 15cm")
print("   - le moteur B est situé au centre du repere")
print("   - la liaison AB est une pivot d'axe y, toutes les autres liaisons sont des pivots d'axe z")
print("   - l'epaisseur des obstacles est 5cm")
print("   - les angles sont en radians")
print("   - les coordonnes de l'obstacle sont celle du point interieur gauche haut en se placant au centre du repere")
print("")
print("       y            C    E   ")
print("       |_ x        / \\  / \\")
print("      /           B    D  ")
print("     z            A       ")
print("######################################################################")

#Determination de la position que l'on souhaite atteindre avec le bras
xf=input("Position de l'extremitee selon X")
yf=input("Position de l'extremitee selon Y")
zf=input("Position de l'extremitee selon Z")
xf=int(xf)
yf=int(yf)
zf=int(zf)

#Determination de la position de l'obstacle
xo=input("position de l'obstacle selon X")
yo=input("position de l'obstacle selon Y")
zo=input("position de l'obstacle selon Z")
xo=int(xo)
yo=int(yo)
zo=int(zo)

#Reduction a un probleme plan (-> determination de l'angle pour le servo A)

print("####   Resultats   ####")

print("L'angle pour le moteur A est :")
aa=atan(yf/xf)
print(aa)

#1er partie du bras (poser Dsur l'obstacle)

xd=xo+epaisseurobstacle/2
yd=yo+marge

print("xd : "+str(xd))
print("yd : "+str(yd))

bd=sqrt((xd**2)+(yd**2))

print("bd : "+str(bd))

solb=atan(yd/xd)
triangleb=acos(bd/(taillesegment*2))
ab=(solb)+(triangleb)

ac=180*((2*pi)/360)-2*(acos((bd/2)/taillesegment))

xc=taillesegment*cos(ab)
yc=taillesegment*sin(ab)



df=sqrt(((abs(xf-xd))**2)+((abs(yd-yf))**2))

triangled=acos(df/(2*taillesegment))
sold=asin((xf-xd)/taillesegment)
#ad=triangled+sold
ad=(triangled+solb)-90*((2*pi)/360)

xe=(taillesegment*cos(ad))+xd
ye=(taillesegment*sin(ad))+yd




# Partie GUI

pygame.init()
fenetre = pygame.display.set_mode((700,500))
fenetre.fill((0, 0, 0))
pygame.display.flip()

#Repere du bas de fenetre et reperes des vues

pygame.draw.line(fenetre, (0, 0, 255), (20, 480), (20, 440), 2)
pygame.draw.line(fenetre, (255, 0, 0), (20, 480), (60, 480), 2)
pygame.draw.line(fenetre, (0, 255, 0), (20, 480), (30, 495), 2)

pygame.draw.line(fenetre, (0, 0, 255), (20, 400), (20, 100), 2)
pygame.draw.line(fenetre, (255, 0, 0), (20, 400), (320, 400), 2)

pygame.draw.line(fenetre, (255, 0, 0), (350, 400), (350, 100), 2)
pygame.draw.line(fenetre, (0, 255, 0), (350, 400), (650, 400), 2)

#Desssin de l'obstacle

pygame.draw.rect(fenetre, (255,255,255), (20+xo*g,400-yo*g,epaisseurobstacle*g,yo*g), 0)
pygame.draw.rect(fenetre, (255,255,255), (350+xo*4,400,xo*4,-5), 0)
#Dessin du bras

pygame.draw.line(fenetre, (0, 255, 255), (20, 400), (20+xc*g, 400-yc*g), 2)
pygame.draw.line(fenetre, (255, 255, 0), (20+xc*g, 400-yc*g), (20+xd*g, 400-yd*g), 2)
pygame.draw.line(fenetre, (255, 0, 255), (20+xd*g, 400-yd*g), (20+xe*g, 400-ye*g), 2)
pygame.draw.line(fenetre, (139, 105, 20), (20+xe*g, 400-ye*g), (20+xf*g, 400-yf*g), 2)


pygame.display.flip()

while continuer==1:
	for event in pygame.event.get():   
		if event.type == QUIT:     
			continuer = 0 
