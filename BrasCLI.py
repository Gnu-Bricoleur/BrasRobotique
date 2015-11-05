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

print("######################################################################")
print("Calcul des angles pour les servomoteurs d'un bras robotique 4 segments")
print("Les conventions utilisees sont les suivantes :")
print("   - les distances sont en centimetres et les segments font 15cm")
print("   - le moteur A est situé au centre du repere")
print("   - la liaison AB est une pivot d'axe Z, toutes les autres liaisons sont des pivots d'axe Y")
print("   - l'epaisseur des obstacles est 5cm")
print("   - les angles sont en radians")
print("les coordonnes de l'obstacle sont celle du point exterieur gauche en se placant au centre du repere")
print("")
print("       z            C    E   ")
print("       |_ x        / \\  / \\")
print("      /           B    D  ")
print("     y            A       ")
print("######################################################################")

#Determination de la position que l'on souhaite atteindre avec le bras
x=input("Position de l'extremitee selon X")
y=input("Position de l'extremitee selon Y")
z=input("Position de l'extremitee selon Z")
x=int(x)
y=int(y)
z=int(z)

#Determination de la position de l'obstacle
ox=input("position de l'obstacle selon X")
oy=input("position de l'obstacle selon Y")
oz=input("position de l'obstacle selon Z")
ox=int(ox)
oy=int(oy)
oz=int(oz)

#Reduction a un probleme plan (-> determination de l'angle pour le servo A)

print("####   Resultats   ####")

print("L'angle pour le moteur A est :")
alpha=atan(y/x)
print(alpha)


#Determination de l'hypothenuse h forme par les moteurs BCD, D étant "pose" (5cm de marge) sur l'obstacle 

h=sqrt(sqrt((ox**2)+(oy**2))+(oz+marge)**2)

#Determination angle moteur B (angle triangle precedant + angle du triangle avec l'horizontale)

beta=(asin((oz+marge)/h)+acos((taillesegment**2 + h**2 - taillesegment**2)/(2*taillesegment*h)))

print("L'angle pour le moteur B est :")
print(beta)

#Determination de l'angle pour le moteur C (Al quashi)

gamma=acos((taillesegment**2 + taillesegment**2 - h**2)/(2*taillesegment*taillesegment))
print("L'angle pour le moteur C est :")
print(gamma)


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

pygame.draw.rect(fenetre, (255,255,255), (20+ox*4,400,ox*4,-oz*4), 0)
pygame.draw.rect(fenetre, (255,255,255), (350+ox*4,400,ox*4,-5), 0)
#Dessin du bras




pygame.display.flip()

while continuer==1:
	for event in pygame.event.get():   
		if event.type == QUIT:     
			continuer = 0 
