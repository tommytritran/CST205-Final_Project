# SET IMAGE SYNTAX: ex.setImage("map.png")

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
import random
import pygame
import sys
class GUISetup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,650,650)
    def initUI(self):
        self.resize(600,500)
        self.setWindowTitle('the Yawhg')
        self.label = QLabel(self)
        height_of_label = 500
        self.label.resize(self.width(), height_of_label)
        self.show() 
    def setImage(self, url):
        self.pixmap = QPixmap(url)
        self.label.setPixmap(self.pixmap.scaled(self.label.size()))   
if __name__ == '__main__':
    app = QApplication(sys.argv)
#----- UI Setup --------------------------
    ex = GUISetup()
    ex.initUI()
#----- Audio Setup -----------------------
#Need pygame to run aduio, (pip install pygame)
    pygame.init()
    pygame.mixer.music.load("Misc/bgsound.mp3")
    pygame.mixer.music.play()
#-----------------------------------------

ex.setImage("Misc/title.jpg")
input("Hit enter.")

ex.setImage("Portraits/blueportrait.jpg")
p1 = input("Who is a antisocial huntress who goes bear trapping? ")

ex.setImage("Portraits/greenportrait.jpg")
p2 = input("\nWho is a gladiator who has a soft spot for animals? ")

ex.setImage("Portraits/redportrait.jpg")
p3 = input("\nWho is a Princess who dresses in red? ")

ex.setImage("Portraits/yellowportrait.jpg")
p4 = input("\nWho is the scientist grandson of the Great Hero? ")

p1Physique = 5
p1Finesse = 5
p1Magic = 5
p1Mind = 5
p1Charm = 5
p1Wealth = 0

p2Physique = 5
p2Finesse = 5
p2Magic = 5
p2Mind = 5
p2Charm = 5
p2Wealth = 0

p3Physique = 5
p3Finesse = 5
p3Magic = 5
p3Mind = 5
p3Charm = 5
p3Wealth = 0

p4Physique = 5
p4Finesse = 5
p4Magic = 5
p4Mind = 5
p4Charm = 5
p4Wealth = 0

p1turns = [1,5,9,13,17,21,25]
p2turns = [2,6,10,14,18,22,26]
p3turns = [3,7,11,15,19,23,27]
p4turns = [4,8,12,16,20,24,28]


ex.setImage("Misc/title.jpg")

Continue = input("\n... (Enter to Continue on all text)")
Continue = input("\nThe YAWHG came... long ago.")
Continue = input("\nIt destroyed all things, we had to build up from the wreckage.")
Continue = input("\nWe Succeeded, but have we Forgotten?")
Continue = input("\nThe YAWHG will be here in six weeks ... and no one expects it.")
Continue = input("\nNot a one of us.")
Continue = input("\nWe just keep on living our lives, week by week, unaware.")
Continue = input("\n...\n")

turn = 0
week = 0

for move in range(1,25):
  turn += 1

  if turn in p1turns:
    week += 1
    
    if week == 1:
      Continue = input("\n... (Enter to Continue on all text)")
      ex.setImage("Week/1.jpg")  

    if week == 2:
      Continue = input("\n... (Enter to Continue on all text)")
      ex.setImage("Week/2.jpg")
      input("They say the last time it came, the YAWHG devoured houses whole. Stole lives. Tore families (and family members) apart. But that was so very long ago...\n")

    if week == 3:
      Continue = input("\n... (Enter to Continue on all text)")
      ex.setImage("Week/3.jpg")
      input("It was on us in a heartbeat -or so the stories go. The earth shook... the air went... still...\n")

    if week == 4:
      Continue = input("\n... (Enter to Continue on all text)")
      ex.setImage("Week/4.jpg")
      input("...and then the world was a howling fury. Chaos. Screaming. The sound of all we knew being pulled in half...\n") 

    if week == 5:
      Continue = input("\n... (Enter to Continue on all text)")
      ex.setImage("Week/5.jpg")
      input("When it arrives this time... how will we fare? Will we once more rebuild, move on, be strong... or have we forgotten?\n") 

    if week == 6:
      Continue = input("\n... (Enter to Continue on all text)")
      ex.setImage("Week/6.jpg")
      input("The YAWHG. It's almost here. Almost, almost.\n") 

    input("Week " + str(week))
    
    input(p1+", it's your turn!")
    
  if turn in p2turns:
    input(p2+", it's your turn!")
    
  if turn in p3turns:
    input(p3+", it's your turn!")
    
  if turn in p4turns:
    input(p4+", it's your turn!")
  

  print("\n1.Forest")
  print("2.Arena")
  print("3.Alchemy Tower")
  print("4.Gardens")
  print("5.Palace")
  print("6.Tavern")
  print("7.Hospital")
  print("8.Slums\n")

  Location = input("Where do you want to go? (1-8) ")

  if Location == "1":
    ForestActivity = input("\nWould you like to: 1.Chop Wood or 2.Hunt ")
    
    if ForestActivity == "1":
      Continue = input("\nYou spend the week chopping wood for the town. You gain 1 Physique, 1 Finesse, and earn yourself 1 Wealth!\n")
      
      if turn in p1turns:
        ex.setImage("InsetPanels/1/11.jpg")
        p1Physique = p1Physique+1
        p1Finesse = p1Finesse+1
        p1Wealth = p1Wealth+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/1/12.jpg")
        p2Physique = p2Physique+1
        p2Finesse = p2Finesse+1
        p2Wealth = p2Wealth+1 
        
      if turn in p3turns:
        ex.setImage("InsetPanels/1/13.jpg")
        p3Physique = p3Physique+1
        p3Finesse = p3Finesse+1
        p3Wealth = p3Wealth+1
      
      if turn in p4turns:
        ex.setImage("InsetPanels/1/14.jpg")
        p4Physique = p4Physique+1
        p4Finesse = p4Finesse+1
        p4Wealth = p4Wealth+1
      
    if ForestActivity == "2":
      Continue = input("\nYou spend the week hunting defenseless critters. You gain 2 Finesse and earn yourself 1 Wealth!\n")

      if turn in p1turns:
        ex.setImage("InsetPanels/1/21.jpg")
        p1Finesse = p1Finesse+2
        p1Wealth = p1Wealth+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/1/22.jpg")
        p2Finesse = p2Finesse+2
        p2Wealth = p2Wealth+1 
        
      if turn in p3turns:
        ex.setImage("InsetPanels/1/23.jpg")
        p3Finesse = p3Finesse+2
        p3Wealth = p3Wealth+1
        
      if turn in p4turns:
        ex.setImage("InsetPanels/1/24.jpg")
        p4Finesse = p4Finesse+2
        p4Wealth = p4Wealth+1


  if Location == "2":
    ArenaActivity = input("\nWould you like to: 1.Compete in fight or 2.Bet on fight ")
    
    if ArenaActivity == "1":
      Continue = input("\nYou spend the week fighting brutes in the arena. You gain 2 Physique and 1 Finesse!\n")
      
      if turn in p1turns:
        ex.setImage("InsetPanels/2/11.jpg")
        p1Physique = p1Physique+2
        p1Finesse = p1Finesse+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/2/12.jpg")
        p2Physique = p2Physique+2
        p2Finesse = p2Finesse+1
        
      if turn in p3turns:
        ex.setImage("InsetPanels/2/13.jpg")
        p3Physique = p3Physique+2
        p3Finesse = p3Finesse+1
      
      if turn in p4turns:
        ex.setImage("InsetPanels/2/14.jpg")
        p4Physique = p4Physique+2
        p4Finesse = p4Finesse+1

        
    if ArenaActivity == "2":
      Continue = input("\nYou spend the week placing bets on your favorite fighters. You gain 5 Wealth!\n")
      
      if turn in p1turns:
        ex.setImage("InsetPanels/2/21.jpg")
        p1Wealth = p1Wealth+5
        
      if turn in p2turns:
        ex.setImage("InsetPanels/2/22.jpg")
        p2Wealth = p2Wealth+5 
        
      if turn in p3turns:
        ex.setImage("InsetPanels/2/23.jpg")
        p3Wealth = p3Wealth+5
        
      if turn in p4turns:
        ex.setImage("InsetPanels/2/24.jpg")
        p4Wealth = p4Wealth+5


  if Location == "3":
    AlchemyTowerActivity = input("\nWould you like to: 1.Clean lab or 2.Brew potion ")
    
    if AlchemyTowerActivity == "1":
      Continue = input("\nYou spend the week cleaning up noxious chemicals. You're paid 1 Wealth for you labor and gain 1 Physique and 1 Magic!\n")
      
      if turn in p1turns:
        ex.setImage("InsetPanels/3/11.jpg")
        p1Wealth = p1Wealth+1
        p1Physique = p1Physique+1
        p1Magic = p1Magic+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/3/12.jpg")
        p2Wealth = p2Wealth+1
        p2Physique = p2Physique+1
        p2Magic = p2Magic+1

      if turn in p3turns:
        ex.setImage("InsetPanels/3/13.jpg")
        p3Wealth = p3Wealth+1
        p3Physique = p3Physique+1
        p3Magic = p3Magic+1
      
      if turn in p4turns:
        ex.setImage("InsetPanels/3/14.jpg")
        p4Wealth = p4Wealth+1
        p4Physique = p4Physique+1
        p4Magic = p4Magic+1


    if AlchemyTowerActivity == "2":
      Continue = input("\nYou spend the week experimenting with different potion brews. You gain 2 Magic and 1 Mind!\n")

      if turn in p1turns:
        ex.setImage("InsetPanels/3/21.jpg")
        p1Magic = p1Magic+2
        p1Mind = p1Mind+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/3/22.jpg")
        p2Magic = p2Magic+2
        p2Mind = p2Mind+1

      if turn in p3turns:
        ex.setImage("InsetPanels/3/23.jpg")
        p3Magic = p3Magic+2
        p3Mind = p3Mind+1

      if turn in p4turns:
        ex.setImage("InsetPanels/3/24.jpg")
        p4Magic = p4Magic+2
        p4Mind = p4Mind+1


  if Location == "4":
    GardensActivity = input("\nWould you like to: 1.Landscape or 2.Meditate ")
    
    if GardensActivity == "1":
      Continue = input("\nYou spend the week maintaining the plants in the royal garden. You gain 1 Finesse, 1 Physique and earn yourself 1 Wealth!\n")
      
      if turn in p1turns:
        ex.setImage("InsetPanels/4/11.jpg")
        p1Finesse = p1Finesse+1
        p1Physique = p1Physique+1
        p1Wealth = p1Wealth+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/4/12.jpg")
        p2Finesse = p2Finesse+1
        p2Physique = p2Physique+1
        p2Wealth = p2Wealth+1

      if turn in p3turns:
        ex.setImage("InsetPanels/4/13.jpg")
        p3Finesse = p3Finesse+1
        p3Physique = p3Physique+1
        p3Wealth = p3Wealth+1
      
      if turn in p4turns:
        ex.setImage("InsetPanels/4/14.jpg")
        p4Finesse = p4Finesse+1
        p4Physique = p4Physique+1
        p4Wealth = p4Wealth+1

        
    if GardensActivity == "2":
      Continue = input("\nYou spend the week in deep meditation. You gain 1 Magic and 2 Mind!\n")

      if turn in p1turns:
        ex.setImage("InsetPanels/4/21.jpg")
        p1Magic = p1Magic+1
        p1Mind = p1Mind+2
        
      if turn in p2turns:
        ex.setImage("InsetPanels/4/22.jpg")
        p2Magic = p2Magic+1
        p2Mind = p2Mind+2

      if turn in p3turns:
        ex.setImage("InsetPanels/4/23.jpg")
        p3Magic = p3Magic+1
        p3Mind = p3Mind+2

      if turn in p4turns:
        ex.setImage("InsetPanels/4/24.jpg")
        p4Magic = p4Magic+1
        p4Mind = p4Mind+2

  if Location == "5":
    PalaceActivity = input("\nWould you like to: 1.Do administrative work or 2.Attend ball ")
    
    if PalaceActivity == "1":
      Continue = input("\nYou spend the week doing paperwork for the palace. You're paid 2 Wealth and gain 1 Mind!\n")
      
      if turn in p1turns:
        ex.setImage("InsetPanels/5/11.jpg")
        p1Wealth = p1Wealth+2
        p1Mind = p1Mind+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/5/12.jpg")
        p2Wealth = p2Wealth+2
        p2Mind = p2Mind+1

      if turn in p3turns:
        ex.setImage("InsetPanels/5/13.jpg")
        p3Wealth = p3Wealth+2
        p3Mind = p3Mind+1
      
      if turn in p4turns:
        ex.setImage("InsetPanels/5/14.jpg")
        p4Wealth = p4Wealth+2
        p4Mind = p4Mind+1

        
    if PalaceActivity == "2":
      Continue = input("\nYou spend the week attending fancy gatherings. You gain 2 Charm and 1 Finesse!\n")

      if turn in p1turns:
        ex.setImage("InsetPanels/5/21.jpg")
        p1Charm = p1Charm+2
        p1Finesse = p1Finesse+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/5/22.jpg")
        p2Charm = p2Charm+2
        p2Finesse = p2Finesse+1

      if turn in p3turns:
        ex.setImage("InsetPanels/5/23.jpg")
        p3Charm = p3Charm+2
        p3Finesse = p3Finesse+1

      if turn in p4turns:
        ex.setImage("InsetPanels/5/24.jpg")
        p4Charm = p4Charm+2
        p4Finesse = p4Finesse+1


  if Location == "6":
    TavernActivity = input("\nWould you like to: 1.Bartend or 2.Drink ")
    
    if TavernActivity == "1":
      Continue = input("\nYou spend the week serving drinks at the tavern. You earn 1 Wealth in tips and gain 2 Charm!\n")
      
      if turn in p1turns:
        ex.setImage("InsetPanels/6/11.jpg")
        p1Wealth = p1Wealth+1
        p1Charm = p1Charm+2
        
      if turn in p2turns:
        ex.setImage("InsetPanels/6/12.jpg")
        p2Wealth = p2Wealth+1
        p2Charm = p2Charm+2

      if turn in p3turns:
        ex.setImage("InsetPanels/6/13.jpg")
        p3Wealth = p3Wealth+1
        p3Charm = p3Charm+2
      
      if turn in p4turns:
        ex.setImage("InsetPanels/6/14.jpg")
        p4Wealth = p4Wealth+1
        p4Charm = p4Charm+2

        
    if TavernActivity == "2":
      Continue = input("\nYou spend the week getting wasted. You gain 2 Charm and 1 Physique!\n")

      if turn in p1turns:
        ex.setImage("InsetPanels/6/21.jpg")
        p1Charm = p1Charm+2
        p1Physique = p1Physique+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/6/22.jpg")
        p2Charm = p2Charm+2
        p2Physique = p2Physique+1

      if turn in p3turns:
        ex.setImage("InsetPanels/6/23.jpg")
        p3Charm = p3Charm+2
        p3Physique = p3Physique+1

      if turn in p4turns:
        ex.setImage("InsetPanels/6/24.jpg")
        p4Charm = p4Charm+2
        p4Physique = p4Physique+1


  if Location == "7":
    HospitalActivity = input("\nWould you like to: 1.Clean up or 2.Tend to patients ")
    
    if HospitalActivity == "1":
      Continue = input("\nYou spend the week steeling your mind against the horrors of the hospital, making sure it is as clean as can be. You gain 1 Mind, 1 Physique and earn 1 Wealth!\n")
      
      if turn in p1turns:
        ex.setImage("InsetPanels/7/11.jpg")
        p1Mind = p1Mind+1
        p1Physique = p1Physique+1
        p1Wealth = p1Wealth+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/7/12.jpg")
        p2Mind = p2Mind+1
        p2Physique = p2Physique+1
        p2Wealth = p2Wealth+11

      if turn in p3turns:
        ex.setImage("InsetPanels/7/13.jpg")
        p3Mind = p3Mind+1
        p3Physique = p3Physique+1
        p3Wealth = p3Wealth+1
      
      if turn in p4turns:
        ex.setImage("InsetPanels/7/14.jpg")
        p4Mind = p4Mind+1
        p4Physique = p4Physique+1
        p4Wealth = p4Wealth+1

        
    if HospitalActivity == "2":
      Continue = input("\nYou spend the week diagnosing and tending to the sick. You gain 2 Mind and 1 Wealth!\n")

      if turn in p1turns:
        ex.setImage("InsetPanels/7/21.jpg")
        p1Mind = p1Mind+2
        p1Wealth = p1Wealth+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/7/22.jpg")
        p2Mind = p2Mind+2
        p2Wealth = p2Wealth+1

      if turn in p3turns:
        ex.setImage("InsetPanels/7/23.jpg")
        p3Mind = p3Mind+2
        p3Wealth = p3Wealth+1

      if turn in p4turns:
        ex.setImage("InsetPanels/7/24.jpg")
        p4Mind = p4Mind+2
        p4Wealth = p4Wealth+1


  if Location == "8":
    SlumsActivity = input("\nWould you like to: 1.Pickpocket or 2.Fight crime ")
    
    if SlumsActivity == "1":
      Continue = input("\nYou spend the week performing petty theft. You earn 1 Wealth and 2 Finesse!\n")
      
      if turn in p1turns:
        ex.setImage("InsetPanels/8/11.jpg")
        p1Wealth = p1Wealth+1
        p1Finesse = p1Finesse+2
        
      if turn in p2turns:
        ex.setImage("InsetPanels/8/12.jpg")
        p2Wealth = p2Wealth+1
        p2Finesse = p2Finesse+2

      if turn in p3turns:
        ex.setImage("InsetPanels/8/13.jpg")
        p3Wealth = p3Wealth+1
        p3Finesse = p3Finesse+2
      
      if turn in p4turns:
        ex.setImage("InsetPanels/8/14.jpg")
        p4Wealth = p4Wealth+1
        p4Finesse = p4Finesse+2

        
    if SlumsActivity == "2":
      Continue = input("\nYou spend the week outsmarting and beating up criminals. You gain 1 Mind, 1 Physique and 1 Finesse!\n")

      if turn in p1turns:
        ex.setImage("InsetPanels/8/21.jpg")
        p1Mind = p1Mind+1
        p1Physique = p1Physique+1
        p1Finesse = p1Finesse+1
        
      if turn in p2turns:
        ex.setImage("InsetPanels/8/22.jpg")
        p2Mind = p2Mind+1
        p2Physique = p2Physique+1
        p2Finesse = p2Finesse+1

      if turn in p3turns:
        ex.setImage("InsetPanels/8/23.jpg")
        p3Mind = p3Mind+1
        p3Physique = p3Physique+1
        p3Finesse = p3Finesse+1

      if turn in p4turns:
        ex.setImage("InsetPanels/8/24.jpg")
        p4Mind = p4Mind+1
        p4Physique = p4Physique+1
        p4Finesse = p4Finesse+1

ex.setImage("Misc/title.jpg")

Ending = input("The storm arrives in the night. By the morning it still rages. For 3 full days the tempest puts us through a grinder -drowns us, crushes us ruins us...\n")

Ending = input("...but then it ends. We see the graveyard our home has become.\n")

Ending = input("Our home.\n")

ex.setImage("Week/7.jpg")

Ending = input("Does anything yet live?\n")

Ending = input("Is it, are we, past saving?\n")


for move in range(25,29):
  turn += 1

  if turn in p1turns:
    print(p1+", final turn!")
    
  if turn in p2turns:
    print(p2+", final turn!")
    
  if turn in p3turns:
    print(p3+", final turn!")
    
  if turn in p4turns:
    print(p4+", final turn!")
  
  print("\n1.the LEADER")
  print("2.the BUILDER")
  print("3.the CONJURER")
  print("4.the DOCTOR")
  print("5.the SMELTER")
  print("6.the TAILOR")
  print("7.the LOOTER")
  print("8.the TOWN DRUNK\n")

  Role = input("Choose your role (1-8) ")

  if Role == "1" and turn in p1turns:
    ex.setImage("InsetPanels/Ending/good1.jpg")
    Leader = input("\nYou take it upon yourself to be the leader of the survivors.")

    Leader = input("\nYou expertly delegate and prioritize tasks.")

    Leader = input("\nYou give motivational speeches and act as an effective mediator in disputes.")

    Leader = input("\nThis helps the rebuilding effort significantly!")


  if Role == "1" and turn in p2turns:
    ex.setImage("InsetPanels/Ending/good2.jpg")
    Leader = input("\nYou take it upon yourself to be the leader of the survivors.")

    Leader = input("\nYou expertly delegate and prioritize tasks.")

    Leader = input("\nYou give motivational speeches and act as an effective mediator in disputes.")

    Leader = input("\nThis helps the rebuilding effort significantly!")

  if Role == "1" and turn in p3turns:
    ex.setImage("InsetPanels/Ending/good3.jpg")
    Leader = input("\nYou take it upon yourself to be the leader of the survivors.")

    Leader = input("\nYou expertly delegate and prioritize tasks.")

    Leader = input("\nYou give motivational speeches and act as an effective mediator in disputes.")

    Leader = input("\nThis helps the rebuilding effort significantly!")

  if Role == "1" and turn in p4turns:
    ex.setImage("InsetPanels/Ending/good4.jpg")
    Leader = input("\nYou take it upon yourself to be the leader of the survivors.")

    Leader = input("\nYou expertly delegate and prioritize tasks.")

    Leader = input("\nYou give motivational speeches and act as an effective mediator in disputes.")

    Leader = input("\nThis helps the rebuilding effort significantly!")

  if Role == "2" and turn in p1turns:
    ex.setImage("InsetPanels/Ending/okay1.jpg")
    Builder = input("\nYou take it upon yourself to help rebuild the town by hand!")

    Builder = input("\nYou rebuild homes at breakneck speed, impressing the rest of the survivors.")

    Builder = input("\nThis helps the rebuilding effort significantly.")

  if Role == "2" and turn in p2turns:
    ex.setImage("InsetPanels/Ending/okay2.jpg")
    Builder = input("\nYou take it upon yourself to help rebuild the town by hand!")

    Builder = input("\nYou rebuild homes at breakneck speed, impressing the rest of the survivors.")

    Builder = input("\nThis helps the rebuilding effort significantly.")

  if Role == "2" and turn in p3turns:
    ex.setImage("InsetPanels/Ending/okay3.jpg")
    Builder = input("\nYou take it upon yourself to help rebuild the town by hand!")

    Builder = input("\nYou rebuild homes at breakneck speed, impressing the rest of the survivors.")

    Builder = input("\nThis helps the rebuilding effort significantly.")

  if Role == "2" and turn in p4turns:
    ex.setImage("InsetPanels/Ending/okay4.jpg")
    Builder = input("\nYou take it upon yourself to help rebuild the town by hand!")

    Builder = input("\nYou rebuild homes at breakneck speed, impressing the rest of the survivors.")

    Builder = input("\nThis helps the rebuilding effort significantly.")

  if Role == "3" and turn in p1turns:
    ex.setImage("InsetPanels/Ending/okay1.jpg")
    Conjurer = input("\nYou take it upon yourself to help conjure up supplies for the town!")

    Conjurer = input("\nWith your magic, you summon a small amount of supplies!")

    Conjurer = input("\nYou struggle a lot to keep up with demand, but can barely summon the amount of lumber and food required.")

    Conjurer = input("\nThis helps a little in the rebuilding effort.")

  if Role == "3" and turn in p2turns:
    ex.setImage("InsetPanels/Ending/okay2.jpg")
    Conjurer = input("\nYou take it upon yourself to help conjure up supplies for the town!")

    Conjurer = input("\nWith your magic, you summon a small amount of supplies!")

    Conjurer = input("\nYou struggle a lot to keep up with demand, but can barely summon the amount of lumber and food required.")

    Conjurer = input("\nThis helps a little in the rebuilding effort.")

  if Role == "3" and turn in p3turns:
    ex.setImage("InsetPanels/Ending/okay3.jpg")
    Conjurer = input("\nYou take it upon yourself to help conjure up supplies for the town!")

    Conjurer = input("\nWith your magic, you summon a small amount of supplies!")

    Conjurer = input("\nYou struggle a lot to keep up with demand, but can barely summon the amount of lumber and food required.")

    Conjurer = input("\nThis helps a little in the rebuilding effort.")

  if Role == "3" and turn in p4turns:
    ex.setImage("InsetPanels/Ending/okay4.jpg")
    Conjurer = input("\nYou take it upon yourself to help conjure up supplies for the town!")

    Conjurer = input("\nWith your magic, you summon a small amount of supplies!")

    Conjurer = input("\nYou struggle a lot to keep up with demand, but can barely summon the amount of lumber and food required.")

    Conjurer = input("\nThis helps a little in the rebuilding effort.")

  if Role == "4" and turn in p1turns:
    ex.setImage("InsetPanels/Ending/good1.jpg")
    Doctor = input("\nYou take it upon yourself to help the sick and injured from the YAWHG.")

    Doctor = input("\nYou're able to fix up most of your patients in no time at all.")

    Doctor = input("\nThis means there are more people to help with rebuilding the town.")

    Doctor = input("\nThis helps the survival effort considerably!")

  if Role == "4" and turn in p2turns:
    ex.setImage("InsetPanels/Ending/good2.jpg")
    Doctor = input("\nYou take it upon yourself to help the sick and injured from the YAWHG.")

    Doctor = input("\nYou're able to fix up most of your patients in no time at all.")

    Doctor = input("\nThis means there are more people to help with rebuilding the town.")

    Doctor = input("\nThis helps the survival effort considerably!")

  if Role == "4" and turn in p3turns:
    ex.setImage("InsetPanels/Ending/good3.jpg")
    Doctor = input("\nYou take it upon yourself to help the sick and injured from the YAWHG.")

    Doctor = input("\nYou're able to fix up most of your patients in no time at all.")

    Doctor = input("\nThis means there are more people to help with rebuilding the town.")

    Doctor = input("\nThis helps the survival effort considerably!")

  if Role == "4" and turn in p4turns:
    ex.setImage("InsetPanels/Ending/good4.jpg")
    Doctor = input("\nYou take it upon yourself to help the sick and injured from the YAWHG.")

    Doctor = input("\nYou're able to fix up most of your patients in no time at all.")

    Doctor = input("\nThis means there are more people to help with rebuilding the town.")

    Doctor = input("\nThis helps the survival effort considerably!")

  if Role == "5" and turn in p1turns:
    ex.setImage("InsetPanels/Ending/good1.jpg")
    Smelter = input("\nYou volunteer to smelt your, now-useless coins, into building materials!")

    Smelter = input("\nWith the modest amount of riches you have you manage to provide a significant amount of metal.")

    Smelter = input("\nYou melt it all down and the smiths take it and work it into various tools and building materials.")

    Smelter = input("\nThis helps the survival effort a lot!")

    Smelter = input("\nYou lose 3 Wealth.")

  if Role == "5" and turn in p2turns:
    ex.setImage("InsetPanels/Ending/good2.jpg")
    Smelter = input("\nYou volunteer to smelt your, now-useless coins, into building materials!")

    Smelter = input("\nWith the modest amount of riches you have you manage to provide a significant amount of metal.")

    Smelter = input("\nYou melt it all down and the smiths take it and work it into various tools and building materials.")

    Smelter = input("\nThis helps the survival effort a lot!")

    Smelter = input("\nYou lose 3 Wealth.")

  if Role == "5" and turn in p3turns:
    ex.setImage("InsetPanels/Ending/good3.jpg")
    Smelter = input("\nYou volunteer to smelt your, now-useless coins, into building materials!")

    Smelter = input("\nWith the modest amount of riches you have you manage to provide a significant amount of metal.")

    Smelter = input("\nYou melt it all down and the smiths take it and work it into various tools and building materials.")

    Smelter = input("\nThis helps the survival effort a lot!")

    Smelter = input("\nYou lose 3 Wealth.")

  if Role == "5" and turn in p4turns:
    ex.setImage("InsetPanels/Ending/good4.jpg")
    Smelter = input("\nYou volunteer to smelt your, now-useless coins, into building materials!")

    Smelter = input("\nWith the modest amount of riches you have you manage to provide a significant amount of metal.")

    Smelter = input("\nYou melt it all down and the smiths take it and work it into various tools and building materials.")

    Smelter = input("\nThis helps the survival effort a lot!")

    Smelter = input("\nYou lose 3 Wealth.")

  if Role == "6":
    Tailor = input("\nYou volunteer to weave and mend clothing for the survivors to keep warm!")

    Tailor = input("\nYOu make and mend clothing faster than anyone would have ever expected.")

    Tailor = input("\nEvery survivor has now an excess number of scarves, socks, and hats to keep warm.")

    Tailor = input("\nThis helps the survival effort immensely!")

  if Role == "7":
    Looter = input("\nYou break into abandoned buildings and hoard together everything for yourself.")

    Looter = input("\nYou gain 3 Wealth!")

    Looter = input("\nYou gain another 3 Wealth!")

    Looter = input("\nThis hurts the survival effort.")

  if Role == "8":
    Drunk = input("\nYou scavenge together as much alcohol as you can and drink excessively!")

    Drunk = input("\nYou gain 2 Physique and 1 Charm.")


Ending = input("\nAnd so:\n")

Ending = input("We set about our tasks, once more living our lives, this time in a way we might never have expected...\n")

Ending = input("(or even wanted...)\n")

Ending = input("BUT IN THE END...\n")

def rand():
  return random.randint(1,3)

newEnd = rand()

if newEnd == 1:
  Ending = input("...we flourished.\n")
  Ending = input("Towers, once wrecked & ravaged, rose towards the sky.\n")
  Ending = input("Trees again took root, then blossomed.\n")
  Ending = input("We all blossomed.\n")
  Ending = input("And though it took a long while, and though it took a lot from us,\n")
  Ending = input("our future is bright\n")
  Ending = input("Should the YAWHG ever return, we will be ready.\n")
  print('THE END')

if newEnd == 2:
  Ending = input("...we were defeated.\n")
  Ending = input("Those of us left struggled to put our homes to rights-\n")
  Ending = input("but the effort was futile.\n")
  Ending = input("Doomed.\n")
  Ending = input("The city bled survivors, eventually becoming a husk,\n")
  Ending = input("a dead thing.\n")
  Ending = input("And perhaps the YAWHG was only partly to blame...\n")
  print('THE END')

if newEnd == 3:
  Ending = input("...it wa a struggle, but a struggle we never abandoned.\n")
  Ending = input("Though our home had been stripped apart, we did not let it languish -and whether we succeed or fail... we did our best.\n")
  Ending = input("Who knows if the YAWHG will visit us again.\n")
  Ending = input("Who knows if we will ever be,\n")
  Ending = input("CAN ever be,\n")
  Ending = input("ready for it.\n")
  print('THE END')
  
#----- TODO PASTE IN LOGIC CODE HERE -----
#Call 'ex.setImage(imageURL)' to display new image
#Need PyGt5 to run
#-----------------------------------------
sys.exit(app.exec_())



