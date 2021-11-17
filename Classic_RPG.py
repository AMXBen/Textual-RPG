#!/usr/bin/env python

from random import*

print("Bienvenue dans votre dernière demeure, fier combattant. Croyez-vous être à la hauteur ? Pensez-vous être capable de survivre à mon arène de la mort ? C'est ce que nous verrons. Voici votre premier adversaire. Bonne chance.")
mob_kill=0
kill_Gob=0
kill_Orc=0
kill_Troll=0
kill_Drag=0
fight=1
critique=randint(1,6)
PV_Héros=(30)
Maana_Héros=(1)
DPS_Gob=randint(1,6)
DPS_Orc=randint(5,10)
DPS_Troll=randint(4,15)
DPS_Drag=randint(9,20)
DPS_mob=0
Taille_monstre=randint(1,20)
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

if Nom_mob=="Gobelin":
    DPS_mob=DPS_Gob
elif Nom_mob=="Orque":
    DPS_mob=DPS_Orc
elif Nom_mob=="Troll":
    DPS_mob=DPS_Troll
else:
    DPS_mob=DPS_Drag

DPS_Sword=randint(5,10)
DPS_BDF=randint(10,25)
Maana_Pot=randint(1,4)
Force_Bonus=6
Heal=(15)

def reroll():
    DPS_Sword=randint(5,10)
    DPS_BDF=randint(10,25)
    Maana_Pot=randint(1,4)
    DPS_Gob=randint(1,6)
    DPS_Orc=randint(5,10)
    DPS_Troll=randint(4,15)
    DPS_Drag=randint(9,20)
    if Nom_mob=="Gobelin":
        DPS_mob=DPS_Gob
    elif Nom_mob=="Orque":
        DPS_mob=DPS_Orc
    elif Nom_mob=="Troll":
        DPS_mob=DPS_Troll
    else:
        DPS_mob=DPS_Drag

while PV_mob>0 and fight==1 and PV_Héros>0 :
    if Nom_mob=="Orque" :
        CombatX=print("L'", Nom_mob,"a",PV_mob,"PV. Vous avez ",Maana_Héros,"Maana et",PV_Héros,"PV. Que souhaitez-vous faire ?")
    else :
        CombatX=print("Le", Nom_mob,"a",PV_mob,"PV. Vous avez ",Maana_Héros,"Maana et",PV_Héros,"PV. Que souhaitez-vous faire ?")
    Combatx=input ("Quel sera votre action ?  1=Epee, 2=BDF (4 Maana), 3=Potion (3 Maana sauf Charge de Maana), 4=Parade.")

    if int(Combatx)==1 :
        PV_mob=PV_mob-DPS_Sword
        Maana_Héros=Maana_Héros+1
        print("Vous infligez",DPS_Sword,"dégâts.")
        PV_Héros=PV_Héros-DPS_mob
        print("Le",Nom_mob,"vous inflige",DPS_mob,"dégâts.")
        reroll()

    elif int(Combatx)==2 :
        if Maana_Héros>=4 :
            PV_mob=PV_mob-DPS_BDF
            Maana_Héros=Maana_Héros-3
            print("Vous infligez",DPS_BDF,"dégâts.")
            PV_Héros=PV_Héros-DPS_mob
            print("Votre adversaire vous inflige",DPS_mob,"dégâts.")
            reroll()

        elif Maana_Héros<4 :
            print("Vous n'avez pas assez de mana.")

    elif int(Combatx)==3 :
        Pot=input ("Potion de Maana, de Force ou bien de Soins ? 1=Maana, 2=Force, 3=Soins")
        if int (Pot)==1 :
            Maana_Héros=Maana_Pot+Maana_Héros
            PV_Héros=PV_Héros-DPS_mob
            print("Votre adversaire vous inflige",DPS_mob,"dégâts.")
            reroll()

        elif int (Pot)==2 :
            if Maana_Héros>=3:
                DPS_Sword=DPS_Sword+Force_Bonus
                Maana_Héros=Maana_Héros-2
                PV_Héros=PV_Héros-DPS_mob
                print("Votre adversaire vous inflige",DPS_mob,"dégâts.")
                reroll()

            else :
                print("Vous n'avez pas assez de Maana.")
        else :
            PV_Héros=PV_Héros+Heal
            Maana_Héros=Maana_Héros-2
            reroll()

    else :
        luck=randint(1,100)
        if luck>=95:
            PV_Héros=PV_Héros-critique
            print("Vous tentez de parrer l'attaque, mais cette attaque critique vous inflige quand même",critique,"dégâts.")
            Maana_Héros=Maana_Héros+1
            reroll()

        else :
            PV_Héros=PV_Héros
            print("Vous parrez l'attaque.")
            Maana_Héros=Maana_Héros+1
            reroll()

    if PV_mob<=0 :
        print("Bien joué. Vous avez écrasé votre ennemi.")
        mob_kill=mob_kill+1
        if Nom_mob=="Gobelin":
            kill_Gob=kill_Gob+1
        elif Nom_mob=="Orque":
            kill_Orc=kill_Orc+1
        elif Nom_mob=="Troll":
            kill_Troll==kill_Troll+1
        else :
            kill_Drag==kill_Drag+1
        qst=input("Bien joué, fier guerrier. Prêt pour un autre défi ?")
        if qst=="OUI":
            fight=1
            Taille_monstre=randint(1,20)
            PV_Héros=30
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
            setatk()
        else :
            fight=0
            if kill_Drag>=1 or kill_Troll>=3 or kill_Gob>=15 or kill_Orc>=7 :
                print("Impressionnant ! Vous êtes vraiment doué. Vous avez massacré",kill_Gob,"gobelins,",kill_Orc,"orques,",kill_Troll,"Trolls et ",kill_Drag,"dragons.")
            else:
                print("En espérant vous revoir bientôt dans notre  arène.")

    if PV_Héros<=0 :
        print("Belle tentative, mais votre faiblesse vous a rattrapée. Vous méritez amplement cette mort.")
        qst=input("Bien tenté, mais vous étiez trop faibles pour pouvoir le vaincre. Vous êtes mort. Souhaitez-vous affronter un adversaire à votre hauteur ?")
        if qst=="OUI":
            fight=1
            Taille_monstre=randint(1,20)
            PV_Héros=30
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
            setatk()
        else :
            fight=0
            print("Revenez quand vous serez plus entraîné et plus fort.")
