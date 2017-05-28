import pygame

def ecrire_entete_ppm (of,l,h,txt):
	of.write ("P3\n")
	of.write ("#"+txt+"\n")
	of.write (str(l)+" "+str(h)+"\n")
	of.write ("255\n")
# fin de fonction

def ouvrir_fichier (typef,mode):
	if mode == 'r' :
		ok = 1
		while ok :
			nomf = input("Donner le nom du fichier (.{} ou rien) :".format(typef))
			if nomf == "" :
				of = None
				break
			try :
				of = open (nomf,mode)
			except :
				print("!!!Erreur pour l'ouverture de {}, recommencer !".format(nomf))
			else :
				ok = 0

	elif mode == 'w' :
		nomf = input("Donnez le nom du fichier (.{}): ".format(typef))
		of = open(nomf,mode)
	return of
# fin de fonction

def ecrire_par_ligne_dans_fichier(of,l_val,tl):
	n=len(l_val)
	q=n//tl
	r=n%tl
	m=q*tl
	for a in range(0,m,tl):
		ligne=""
		for b in range(tl):
			ligne = ligne+str(l_val[a+b])+" "
		ligne = ligne +'\n'
		obf.write(ligne)
	if r :
		ligne = ""
		for b in range (r):
			ligne = ligne+str(l_val[m+b])+" "
		ligne = ligne + "\n"
		obf.write(ligne)
# fin de fonction

def lire_fichier_ppm(of):
	l_rvb=[]
	try :
		li1 = of.readline()
	except :
		return 0,0,l_rvb
	if li1[0] !="P" or li1[1] !="3" :
		return 0,0,l_rvb
	li = of.readline()
	if li[0] == "#" :
		while li[0] == "#" :
			li = of.readline()
	l_mots=li.split()
	larg,haut = int(l_mots[0]),int(l_mots[1])
	of.readline ()
	texte_RVB = of.read()
	l_mots = texte_RVB.split()
	l_rvb = [int(m) for m in l_mots]
	return larg,haut,l_rvb
# fin de fonction

def liste_vers_tab2D (l,h,l_rvb):
	tab = []
	for y in range (h) :
		lig = []
		for x in range (l) :
			n = 3*l*y+3*x
			r = l_rvb[n]
			v = l_rvb[n+1]
			b = l_rvb[n+2]
			pix = (r,v,b)
			lig.append(pix)
		tab.append(lig)
	return tab
# fin de fonction

def niv_gris_zone (tab1,l,h):
	li2 = []
	for y in range (0,h):
		for x in range (0,l):
			z = 3*(l*y+x)
			g = ((tab1[z+0])+(tab1[z+1])+(tab1[z+2]))//3
			li2.append(g),li2.append(g),li2.append(g)
	return li2
# fin de fonction

def engendre_liste_image_monochrome (l,h,coul):
	l_c = []
	for a in range (l*h):
		l_c.append(coul[0])
		l_c.append(coul[1])
		l_c.append(coul[2])
	return l_c
# fin de fonction

def inverse_couleurs(l1):
	l2 = []
	for n in l1 :
		l2.append (255-n)
	return l2
# fin de fonction

def liste_vers_surface(l,h,l_rvb):
	liste_rvb = []
	chaine_img = bytes(l_rvb)
	surf_img = pygame.image.fromstring(chaine_img,(l,h),'RGB')
	return surf_img
# fin de fonction

def ouvrir_fichier_img_pygame():
	ok=1
	while ok :
		nomf = input("Donnezl le nom du fichier image : ")
		if nomf == "" :
			of = None
			break
		try :
			of = pygame.image.load(nomf)
		except :
			print ("!!! Erreur pour l'ouverture de {}, recommencer !".format(nomf))
		else :
			ok = 0
	return of
# fin de fonction

def ouvrir_fichier_img_pygame0():
    ok=1
    while ok :
            nomf = "invert_color.png"
            try :
                    of = pygame.image.load(nomf)
            except :
                    print ("!!! Erreur pour l'ouverture de {}, recommencer !".format(nomf))
            else :
                    ok = 0
    return of
# fin de fonction

def ouvrir_fichier_img_pygame1():
        ok=1
        while ok :
                nomf = "color-to-black-white.jpg"
                try :
                        of = pygame.image.load(nomf)
                except :
                        print ("!!! Erreur pour l'ouverture de {}, recommencer !".format(nomf))
                else :
                        ok = 0
        return of
# fin de fonction

def lecture_fichier_image() :
	rep = input("Ouvrir un fichier image ? ('o' ou 'n')")
	if rep == 'o' :
		surf_img = ouvrir_fichier_img_pygame()
		if surf_img != None :
			l = surf_img.get_width()
			h = surf_img.get_height()
			chaine_img = pygame.image.tostring(surf_img,'RGB')
			l_rvb_img = [int(e) for e  in chaine_img]
			return l,h,surf_img,l_rvb_img
		else :
			return 0,0,[],None
	else :
		return 0,0,[],None
# fin de fonction

print("fonctions chargées")
