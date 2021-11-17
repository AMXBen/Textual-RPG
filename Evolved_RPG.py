#!/usr/bin/env python

from random import*

print("Bienvenue dans votre dernière demeure, fier combattant. Croyez-vous être à la hauteur ? Pensez-vous être capable de survivre à mon arène de la mort ? C'est ce que nous verrons. Voici votre premier adversaire. Bonne chance.")

DPS_Héros=""
fight=1
Classe=int(input ("Quelle classe souhaitez-vous choisir ? 1=Guerrier, 2=Chasseur/Huntard, 3=Paladin, 4=Voleur, 5=Mage"))
critique=randint(1,6)
Heal=15
Force_Bonus=2
DPS_Héros=0
DPS_mob=0
if int (Classe)==1:
    PV_Héros=40
    DPS_Sword=randint(8,13) #capacité 2=berserker (+10 PV pour 2), pas de potion de force, pas de maana => bourrin, pas de sorts
    DPS_Héros=DPS_Sword
elif int(Classe)==2:
    PV_Héros=35
    DPS_Bow=randint(10,15) #capacité 2=deadly shot (+5 aux dégâts pour un tour pour 4), pas de potion de force, pas de potion de maana => bourrin, pas de sorts
    DPS_Héros=DPS_Bow
elif int(Classe)==3:
    PV_Héros=30
    DPS_Marteau=randint(7,12) #capacité 2=impo des mains (full heal pour 6), pas de soins => prodiges
    DPS_Héros=DPS_Marteau
elif int(Classe)==4:
    PV_Héros=25
    DPS_Dague=randint(4,9) #capacité 2=camouflage (attaquer sans subir de dégâts pendant 1 tours pour 7)
    DPS_Héros=DPS_Dague
else :
    PV_Héros=20
    DPS_Ping=randint(5,10) #capacité 2=pyro face (35 dégâts pour 10), pas de potions de force => potion mana = mana +10
    DPS_Héros=DPS_Ping
Maana_Héros=1

def setatkmob():
    if Nom_mob=="Gobelin":
        DPS_mob=DPS_Gob
    elif Nom_mob=="Orque":
        DPS_mob=DPS_Orc
    elif Nom_mob=="Troll":
        DPS_mob=DPS_Troll
    else:
        DPS_mob=DPS_Drag

fight=1
critique=randint(1,6)
Taille_monstre=randint(1,20)
if Taille_monstre==1 or Taille_monstre==2 or Taille_monstre== 3 or Taille_monstre==4 or Taille_monstre==5 or Taille_monstre==6 or Taille_monstre==7 or Taille_monstre==8 or Taille_monstre==9 or Taille_monstre==10 :
    PV_mob=randint(10,25)
    print("Vous croisez un gobelin quelque peu hostile.")
    DPS_Gob=randint(1,6)
    Nom_mob="Gobelin"
    setatkmob()
elif Taille_monstre==11 or Taille_monstre==12 or Taille_monstre==13 or Taille_monstre==14 or Taille_monstre==15:
    PV_mob=randint(30,50)
    print("Vous croisez un orque un peu bourrin.")
    DPS_Orc=randint(5,10)
    Nom_mob="Orque"
    setatkmob()
elif Taille_monstre==16 or Taille_monstre==17 or Taille_monstre==18 or Taille_monstre==19 :
    PV_mob=randint(60,75)
    print("Un gros troll un peu bourré vous barre la route.")
    DPS_Troll=randint(4,15)
    Nom_mob="Troll"
    setatkmob()
else :
    PV_mob=randint(80,100)
    print("Vous avez eu la malchance de réveiller un dragon. Vous affrontez le boss.")
    DPS_Drag=randint(9,20)
    Nom_mob="Dragon"
    setatkmob()

Maana_Héros=(1)

def setatkj():
    if Classe==1:
        DPS_Héros=DPS_Sword
    elif Classe==2:
        DPS_Héros=DPS_Bow
    elif Classe==3:
        DPS_Héros=DPS_Marteau
    elif Classe==4:
        DPS_Héros=DPS_Dague
    elif Classe==5:
        DPS_Héros=DPS_Ping

def reroll ():
    DPS_Sword=randint(8,13)
    DPS_Dague=randint(4,9)
    DPS_Bow=randint(10,15)
    DPS_Marteau=randint(7,12)
    DPS_Ping=randint(5,10)
    setatkj()
    Maana_Pot=randint(1,4)
    DPS_Gob=randint(1,6)
    DPS_Orc=randint(5,10)
    DPS_Troll=randint(4,15)
    DPS_Drag=randint(9,20)
    setatkmob()

while PV_mob>0 and fight==1 and PV_Héros>0 :
    if Nom_mob=="Orque" :
        CombatX=print("L'", Nom_mob,"a",PV_mob,"PV. Vous avez ",Maana_Héros,"Maana et",PV_Héros,"PV. Que souhaitez-vous faire ?")
    else :
        CombatX=print("Le", Nom_mob,"a",PV_mob,"PV. Vous avez ",Maana_Héros,"Maana et",PV_Héros,"PV. Que souhaitez-vous faire ?")
    if Classe==1:
        Combatx=input ("Quelle sera votre action ? 1=Coup d'épée, 2=Lever de bouclier (5 Maana), 3=Potions (le guerrier n'en a pas), 4=Parade.")
    elif Classe==2:
        Combatx=input ("Quelle sera votre action ? 1=Aller face, 2=Tir mortel (4 Maana), 3=Soins, 4=Esquive.")
    elif Classe==3:
        Combatx=input ("Quelle sera votre action ? 1=Coup de marteau, 2=Imposition des mains, 3=Potions, 4=Parade.")
    elif Classe==4:
        Combatx=input ("Quelle sera votre action ? 1=Coup de dague, 2=camouflage, 3=Potions, 4=Parade.")
    else :
        Combatx=input ("Quelle sera votre action ? 1=Boule de feu, 2=Explosion pyrotechnique, 3=Potions, 4=Bouclier magique.")

    if int(Combatx)==1 :
        PV_mob=PV_mob-DPS_Héros
        Maana_Héros=Maana_Héros+1
        print("Vous infligez",DPS_Héros,"dégâts.")
        PV_Héros=PV_Héros-DPS_mob
        print("Le",Nom_mob,"vous inflige",DPS_mob,"dégâts.")
        reroll ()

    elif int(Combatx)==2:
        if Classe==1:
            if Maana_Héros>=2:
                PV_Héros=PV_Héros+10
                Maana_Héros=Maana_Héros-4
                print ("Votre armure vous rend plus résistant.")
            else:
                print("Vous n'êtes pas encore prêt.")
        if Classe==2:
            if Maana_Héros>=4:
                DPS_Héros=DPS_Bow+5
                Maana_Héros=Maana_Héros-3
                print ("Votre flèche est prête à empaler l'ennemi.")
            else:
                print("Votre flèche n'est pas encore prête.")
        if Classe==3:
            if Maana_Héros>=6:
                PV_Héros=30
                Maana_Héros=Maana_Héros-5
                print ("Vous sentez votre force vitale vous revenir, et votre santé revenir au maximum.")
            else :
                print ("Vous ne pouvez pas vous soigner.")
        if Classe==4:
            if Maana_Héros>=7:
                DPS_mob=0
                print ("Vous vous dissimulez parmi les ombres. Votre adversaire ne peut pas vous attaquer ce tour-ci, mais vous pouvez le frapper.")
            else:
                print ("Vous n'avez pas le Maana nécessaire pour vous camoufler.")
        elif Classe==5 :
            if Maana_Héros>=10:
                PV_mob=PV_mob-35
                print ("Vous lancez une énorme boule de feu à la gueule de votre adversaire, lui infligeant ainsi beaucoup de dégâts.")
            else :
                print ("Vous n'avez pas assez de Mana pour faire exploser votre ennemi.")
    elif int(Combatx)==3:
        if Classe==1:
            Pot=input ("Vous n'avez pris aucune potion avec vous. Vous devez continuer à vous battre, et résister avec votre armure. Tapez 1.")
            if int(Pot)==1:
                 if Nom_mob=="Orque" :
                    CombatX=print("L'", Nom_mob,"a",PV_mob,"PV. Vous avez ",Maana_Héros,"Maana et",PV_Héros,"PV. Que souhaitez-vous faire ?")
                 else :
                    CombatX=print("Le", Nom_mob,"a",PV_mob,"PV. Vous avez ",Maana_Héros,"Maana et",PV_Héros,"PV. Que souhaitez-vous faire ?")
                 Combatx=input ("Quelle sera votre action ? 1=Coup d'épée, 2=Lever de bouclier (5 Maana), 3=INUTILE, 4=Parade.")
                 if int(Combatx)==1 :
                    PV_mob=PV_mob-DPS_Héros
                    Maana_Héros=Maana_Héros+1
                    print("Vous infligez",DPS_Héros,"dégâts.")
                    PV_Héros=PV_Héros-DPS_mob
                    print("Le",Nom_mob,"vous inflige",DPS_mob,"dégâts.")
                    reroll ()

                 elif int(Combatx)==2:
                    if Maana_Héros>=5:
                        PV_Héros=PV_Héros+10
                        Maana_Héros=Maana_Héros-4
                        print ("Votre armure vous rend plus résistant.")
                    else:
                        print("Vous n'êtes pas assez énervé.")

                 elif int(Combatx)==4:
                    luck=randint(1,100)
                    if luck>=95:
                        PV_Héros=PV_Héros-critique
                        print("Vous tentez de parrer l'attaque, mais cette attaque critique vous inflige quand même",critique,"dégâts.")
                        Maana_Héros=Maana_Héros+1
                        reroll ()
                    else :
                        PV_Héros=PV_Héros
                        print("Vous parrez l'attaque.")
                        Maana_Héros=Maana_Héros+1
                        reroll ()
        if Classe==2:
            Pot=input ("Les seules potions à votre disposition sont des potions de soin. Tapez 1 pour vous soigner (3 points de Mana).")
            if int(Pot)==1 :
                PV_Héros=PV_Héros+Heal
                print ("Vous sentez votre force vitale vous revenir, et votre santé revenir.")
                Maana_Héros=Maana_Héros-2
                reroll ()

        if Classe==3:
            Pot=int(input ("Vous avez le choix entre deux potions : potion de force (3 points de Mana) et potion de Mana. 1=Force, 2=Mana."))
            if int(Pot)==1:
                if Maana_Héros>=3:
                    DPS_Marteau=DPS_Marteau+Force_Bonus
                    print ("Vous sentez une force nouvelle parcourir votre corps, prêt à vous jeter dans la mêlée.")
                else :
                    print ("Votre potion n'est pas encore prête.")
            else:
                Maana_Héros=Maana_Héros+Maana_Pot
                print ("Une gorgée de potion suffit à rebooster vos capacités prodigiales.")

        if Classe==4:
            Pot=int(input ("Vous avez droit à tous les types de potions : force (3 points de Mana), soins (3 points) et Mana. 1=force, 2=soins, 3=Mana"))
            if Pot==1:
                if Maana_Héros>=3:
                    DPS_Dague=DPS_Dague+Force_Bonus
                    print ("Vous sentez une force nouvelle parcourir votre corps, prêt à vous jeter dans la mêlée.")
                else :
                    print ("Votre potion n'est pas encore prête.")
            if Pot==2:
                if Maana_Héros>=3:
                    PV_Héros=PV_Héros+Heal
                    print ("Vous sentez votre force vitale vous revenir, et votre santé revenir.")
                else :
                    print ("Votre potion n'est pasz encore prête.")
            else :
                Maana_Héros=Maana_Héros+(Maana_Pot*2)
                print ("Vous sentez votre pouvoir revenir en vous. Vous gagnez", Maana_Pot,"points de mana.")

        if Classe==5:
            Pot=int(input("Vous avez le choix entre deux potions : potion de soins (3 points de Mana) et potion de Mana. 1= soins, 2=Mana."))
            if Pot==1:
                if Maana_Héros>=3:
                    PV_Héros=PV_Héros+Heal
                    print ("Vous sentez votre force vitale vous revenir, et votre santé revenir.")
                else :
                    print ("Votre potion n'est pasz encore prête.")
            else :
                Maana_Héros=Maana_Héros+(Maana_Pot*2)
                print ("Vous sentez votre pouvoir revenir en vous. Vous gagnez", Maana_Pot*2,"points de mana.")

    else :
        luck=randint(1,100)
        if luck>=95:
            PV_Héros=PV_Héros-critique
            print("Vous tentez de parrer l'attaque, mais cette attaque critique vous inflige quand même",critique,"dégâts.")
            Maana_Héros=Maana_Héros+1
            reroll ()
        else :
            if Classe==2:
                PV_Héros=PV_Héros
                print("Vous esquivez l'attaque.")
                Maana_Héros=Maana_Héros+1
                reroll ()

            elif Classe==5:
                PV_Héros=PV_Héros
                print("Votre bouclier magique absorbe l'attaque.")
                Maana_Héros=Maana_Héros+1
                reroll ()
            else :
                PV_Héros=PV_Héros
                print("Vous parrez l'attaque.")
                Maana_Héros=Maana_Héros+1
                reroll ()


    if PV_mob<=0 :
            print("Bien joué. Vous avez écrasé votre ennemi.")
            qst=input("Bien joué, fier guerrier. Prêt pour un autre défi ?")
            if qst=="oui":
                fight=1
                Taille_monstre=randint(1,20)
                Maana_Héros=1
                if Taille_monstre==1 or Taille_monstre==2 or Taille_monstre== 3 or Taille_monstre==4 or Taille_monstre==5 or Taille_monstre==6 or Taille_monstre==7 or Taille_monstre==8 or Taille_monstre==9 or Taille_monstre==10 :
                    PV_mob=randint(10,25)
                    print("Vous croisez un gobelin quelque peu hostile.")
                    DPS_Gob=randint(1,6)
                    Nom_mob="Gobelin"
                elif Taille_monstre==11 or Taille_monstre==12 or Taille_monstre==13 or Taille_monstre==14 or Taille_monstre==15:
                    PV_mob=randint(30,50)
                    print("Vous croisez un orque un peu bourrin.")
                    DPS_Orc=randint(5,10)
                    Nom_mob="Orque"
                elif Taille_monstre==16 or Taille_monstre==17 or Taille_monstre==18 or Taille_monstre==19 :
                    PV_mob=randint(60,75)
                    print("Un gros troll un peu bourré vous barre la route.")
                    DPS_Troll=randint(4,15)
                    Nom_mob="Troll"
                else :
                    PV_mob=randint(80,100)
                    print("Vous avez eu la malchance de réveiller un dragon. Vous affrontez le boss.")
                    DPS_Drag=randint(9,20)
                    Nom_mob="Dragon"
                setatkmob()
            else :
                fight=0
                print("En espérant vous revoir bientôt dans notre  arène.")

    if PV_Héros<=0 :
        print("Belle tentative, mais votre faiblesse vous a rattrapée. Vous méritez amplement cette mort.")
        qst=input("Bien tenté, mais vous étiez trop faibles pour pouvoir le vaincre. Vous êtes mort. Souhaitez-vous affronter un adversaire à votre hauteur ?")
        if qst=="oui":
            fight=1
            Taille_monstre=randint(1,20)
            Maana_Héros=1
            if Taille_monstre==1 or Taille_monstre==2 or Taille_monstre== 3 or Taille_monstre==4 or Taille_monstre==5 or Taille_monstre==6 or Taille_monstre==7 or Taille_monstre==8 or Taille_monstre==9 or Taille_monstre==10 :
                PV_mob=randint(10,25)
                print("Vous croisez un gobelin quelque peu hostile.")
                DPS_Gob=randint(1,6)
                Nom_mob="Gobelin"
            elif Taille_monstre==11 or Taille_monstre==12 or Taille_monstre==13 or Taille_monstre==14 or Taille_monstre==15:
                PV_mob=randint(30,50)
                print("Vous croisez un orque un peu bourrin.")
                DPS_Orc=randint(5,10)
                Nom_mob="Orque"
            elif Taille_monstre==16 or Taille_monstre==17 or Taille_monstre==18 or Taille_monstre==19 :
                PV_mob=randint(60,75)
                print("Un gros troll un peu bourré vous barre la route.")
                DPS_Troll=randint(4,15)
                Nom_mob="Troll"
            else :
                PV_mob=randint(80,100)
                print("Vous avez eu la malchance de réveiller un dragon. Vous affrontez le boss.")
                DPS_Drag=randint(9,20)
                Nom_mob="Dragon"
            setatkmob()
        else :
            fight=0
            print("Revenez quand vous serez plus entraîné et plus fort.")
