# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:20:29 2015

@author: Pierre
"""

from PIL import Image

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
    
    
    
    for y in range (H): # y prend une les valeurs de 0 à H (parcours les pixels à la verticale)
    
        for x in range (L):
        
            p = im1.getpixel((x,y)) #la fct getpixel prend les coord du pixel en entrée et retourne un tableau de taille 3 avec la valeur des composantes du pixel de 0 à 255 (RGB)
            
            n = (p[0]+p[1]+p[2])/3 # je transforme l'image couleur en noir et blanc (en faisant la somme des valeurs du rouge vert et bleu en les divisant par 3 )
            
            im3.putpixel((x,y),(n,n,n)) # décolorise image 1 dans image 3 (chaque pixel(x,y) prend la valeur moyenne des intensités des couleurs)
    
    
    
    filtre (im3,im2,matlaplace,H,L) # application de matrice Laplacienne 
        
        
    """filtre ( im2 , im3, matpassehaut)
    im3.show()"""
    
    for y in range (4,H-4): #met l'image en noir ou blanc
        print y
        coox [:] = [] # liste vidée pour chaque nouvelle ligne 
        for x in range (L-1):
            gris = im2.getpixel((x,y))       
            if ( gris[0] < seuil ):
                im4.putpixel((x,y),(0,0,0))
            else :
                im4.putpixel((x,y),(255,255,255))
                """coox.append(x) # coordonées sur X des pixels blanc """
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



    
    



#########################################################################################

"""if (coox[i] <= coox[-3]) :            
    m =im4.getpixel(((coox[i]-1),y))

    if ( coox[i+1] - coox[i] == 1 ): #si la distance entre 2 pix blanc consecutifs est de 1 
                      
        im4.putpixel((i+coox[0],y),(255,0,0))
        
        rouge.append(i+coox[0]) # recup coord pixel rouge
                 
        i = i+1 
    elif (coox[i+1] - coox[i] == 2):
        im4.putpixel((coox[i]+1,y),(255,0,0))
        rouge.append(coox[i+1])
        im4.putpixel((coox[i],y),(255,0,0))
        rouge.append(coox[i])
        i = i+1

    else : 
        i = i+1
        
else   : 
    i = i+1 

                  
        """


####################################################################################