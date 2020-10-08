import pygame

pygame.init()
window_resolution = (700, 230)

Choix = str(input("Quel personnage bas level avez-vous le plus ? "))
if Choix == "Maokai" or Choix == "maokai":
    choixMao = str(input("Si vous avez une Lulu, tapez " + "oui" + " sinon tapez " + "non : "))
if Choix == "Lissandra" or Choix == "lissandra":
    choixLissan = str(input("Si vous avez une Diana, tapez " + "oui" + " sinon tapez " + "non : "))
if Choix == "Vayne" or Choix == "vayne":
    choixVayne = str(input("Si vous avez une Nidalee, tapez " + "oui" + " sinon tapez " + "non : "))
    
pygame.display.set_caption("TFT COMPO V1")
window_surface = pygame.display.set_mode(window_resolution)

#COMPO TIER S

CrepusculeFanatique = pygame.image.load("Images/TFT-Compo-Crepuscule-Fanatique-2.jpg")
OmbreEsprit = pygame.image.load("Images/TFT-Compo-Ombre-Esprit-2.jpg")
ArhiMystique = pygame.image.load("Images/TFT-Compo-Ahri-Mystique.jpg")

#COMPO TIER A

SageAssassin = pygame.image.load("Images/TFT-Compo-Assassin-Sage-3.jpg")
DuellisteExilé = pygame.image.load("Images/TFT-Compo-6-Duellistes-2.jpg")
BagarreurChasseur = pygame.image.load("Images/TFT-Compo-Bagarreur-Chasseur-5.jpg")
SeleniteAssassin = pygame.image.load("Images/TFT-Compo-Selenite-Assassin.jpg")
SeleniteEsprit = pygame.image.load("Images/TFT-Compo-Selenite-Esprit-3.jpg")
SylvestreMage = pygame.image.load("Images/TFT-Compo-Sylvestre-Mage-2.jpg")

#COMPO TIER B

MagesMystique = pygame.image.load("Images/TFT-Compo-6-Mages-2.jpg")
TireursInitiateur = pygame.image.load("Images/TFT-Compo-6-Tireurs-delite-2.jpg")
InitiateurMystique = pygame.image.load("Images/TFT-Compo-Initiateur-Mystique.jpg")
MaitreSentinelle = pygame.image.load("Images/TFT-Compo-6-Maitres-de-guerre.jpg")
Fanatiques = pygame.image.load("Images/TFT-Compo-Fanatique-2.jpg")

Boucle = True
while Boucle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Boucle = False
    
    if Choix == "Vayne" or Choix == "vayne":
        if choixVayne == "Oui" or choixVayne == "oui":
            window_surface.blit(TireursInitiateur, [0,0])    
        else:           
            window_surface.blit(CrepusculeFanatique, [0,0])
    if Choix == "Zed" or Choix == "zed" or Choix == "Teemo" or Choix == "teemo":
        window_surface.blit(OmbreEsprit, [0, 0])
    if Choix == "Tresh" or Choix == "tresh":
        window_surface.blit(ArhiMystique, [0, 0])
    if Choix == "Janna" or Choix == "janna" or Choix == "Pyke" or Choix == "pyke":
        window_surface.blit(SageAssassin, [0, 0])
    if Choix == "Fiora" or Choix == "fiora" or Choix == "Yasuo" or Choix == "yasuo":
        window_surface.blit(DuellisteExilé, [0, 0])        
    if Choix == "Maokai" or Choix == "maokai":
        if choixMao == "Oui" or choixMao == "oui":
            window_surface.blit(SylvestreMage, [0, 0])
        else:
            window_surface.blit(BagarreurChasseur, [0, 0])    
    if Choix == "Diana" or Choix == "diana":
        window_surface.blit(SeleniteAssassin, [0, 0])
    if Choix == "Lissandra" or Choix == "lissandra":
        if choixLissan == "Oui" or choixLissan == "oui":
            window_surface.blit(SeleniteAssassin, [0, 0])
        else:
            window_surface.blit(SeleniteEsprit, [0, 0])
    if Choix == "Nami" or Choix == "nami":
        window_surface.blit(MagesMystique, [0, 0])
    if Choix == "Wukong" or Choix == "wukong":
        window_surface.blit(InitiateurMystique, [0, 0])
    if Choix == "Garen" or Choix == "garen":   
        window_surface.blit(MaitreSentinelle, [0, 0])
    if Choix == "Elise" or Choix == "elise" or Choix == "Twisted Fate" or Choix == "TF" or Choix == "twisted fate":
        window_surface.blit(Fanatiques, [0, 0])   
        
    pygame.display.flip()