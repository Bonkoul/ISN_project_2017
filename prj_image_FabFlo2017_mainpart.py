import pygame
from prj_image_FabFlo2017_def_fonctions import *
pygame.init
fen = pygame.display.set_mode((980,650))
surf_img = ouvrir_fichier_img_pygame0()
if surf_img != None :
        l0 = surf_img.get_width()
        h0 = surf_img.get_height()
        chaine_img = pygame.image.tostring(surf_img,'RGB')
        l_rvb_img = [int(e) for e  in chaine_img]
pos = pygame.Rect ((10,20),(l0,h0))
fen.blit(surf_img,pos)
surf_img0 = ouvrir_fichier_img_pygame1()
if surf_img0 != None :
        l1 = surf_img0.get_width()
        h1 = surf_img0.get_height()
        chaine_img = pygame.image.tostring(surf_img0,'RGB')
        l_rvb_img0 = [int(e) for e  in chaine_img]
pos0 = pygame.Rect ((140,20),(l1,h1))
fen.blit(surf_img0,pos0)
pygame.display.update()
pygame.font.init()
myfont = pygame.font.SysFont("Arial", 15)
label = myfont.render("Cliquez sur l'icône correspondante à l'action voulue.", 1, (255,255,0))
fen.blit(label,(10,90))
pygame.display.update()
ok = 1
while ok :
    e = pygame.event.get()
    for a in e :
            if a.type == pygame.MOUSEBUTTONUP :
                    x,y = pygame.mouse.get_pos()
                    if 10<=x<=130 and 20<=y<=80 :
                            label = myfont.render("***** inverser les couleurs de l'image du fichier ppm . *****",1,(0,0,255))
                            rep = "inv"
                            ok = 0
                    elif 140<=x<=300 and 20<=y<=80 :
                            label = myfont.render("***** rendre monochrome l'image du fichier ppm . *****",1,(0,255,255))
                            rep = "mon"
                            x1,y1,x2,y2 = 10,120,20,130
                            ok = 0
l,h,surf_img1,l_rvb_img1= lecture_fichier_image()
pygame.image.load("test1.jpg")
pygame.display.update

if len(l_rvb_img1) :
	pos1 = pygame.Rect((10,120),(l,h))
	fen.blit(surf_img1,pos1)
	pygame.display.update()
	pygame.time.wait(3000)
	if rep == "inv" :
		l_rvb_img2 = inverse_couleurs(l_rvb_img1)
	if rep == "mon" :
		x1,y1 = 10,120
		x2,y2 = 10+l,120+h
		l_rvb_img2 = niv_gris_zone (l_rvb_img1,l,h)
	surf_img2 = liste_vers_surface(l,h,l_rvb_img2)
	pos2 = pygame.Rect((l+20,120),(l,h))
	fen.blit(surf_img2,pos2)
	pygame.display.update()

print ("***** Fin du programme *****")
pygame.quit
