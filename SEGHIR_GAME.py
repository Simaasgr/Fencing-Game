import keyboard
import time
import os
import enum
import random

#Classe pour répertorier les états des joueurs
class States(enum.Enum):
   REST = 1
   ATTACK = 2
   BLOCK = 3

#CONSTANTES DU JEU: 
movement_speed= 0.2
attacking_speed=4
blocking_time=4
fps=5
attacking_speed_AI=2

#INTELLIGENCE ARTIFICIELLE 
AI=False

#scores par défaut des joueurs 
score1=0
score2=0


#états par défaut des joueurs 
state1= States.REST
state2= States.REST
saut1=False
saut2=False

#PARTIES DES JOUEURS 
head= "<o>"
first_piece= " |_/" 
second_piece=" |" 
third_piece=" |"
last_piece="/|"

first_piece_d= "\_|"  
second_piece_d="|"  
third_piece_d="|"
last_piece_d="|\\"


#récuperer la scène du jeu:
file="stage.ffscene"
with open(file) as f:
   path = f.readline()
initial_path =path


#Fonction qui affiche la scène de jeu 
def print_scene(path, state1, state2, saut1=False, saut2=False): 

    os.system('clear')
    #GESTION DES ATTAQUES
    if state1== States.ATTACK:
        first_piece=" |__"
    elif state1== States.BLOCK: 
        first_piece=" |_|"
    else:
        first_piece=" |_/"
    
    if state2== States.ATTACK:
        first_piece_d= "__|"
    elif state2== States.BLOCK: 
        first_piece_d= "|_|"
    else:
        first_piece_d= "\_|"

    print("#"* (len(path)+2), end="")
    print()
    print(" "*int((len(path))/2), end="")
    print(str(score1) +" , "+ str(score2))
    print()

    #PREMIÈRE LIGNE   (VIDE QUAND Y A PAS DE SAUT)
    for i in range(len(path)): 
       if(i==len(path)-3):
        break
   
       if(path[i]=="_"):
        print(" ", end="")

       if(path[i]=="x"):
        print(" ", end="")


       if(path[i]=="1") and saut1:
        print(head, end="")

       if(path[i+3]=="2") and saut2: #comme la tete fait trois caractères on s'y prend à l'avance de 3
        print(head, end="")

       if(path[i]=="1") and not saut1:
         print("   ", end="")

       if(path[i]=="2") and not saut2:
         print("   ", end="")

    print()
    #DEUXIÈME LIGNE 
    for i in range(len(path)): 

     if(i==len(path)-4):
        break

     if(path[i]=="_"):
        print(" ", end="")

     if(path[i]=="x"):
        print(" ", end="")


     if(path[i]=="1") and not saut1:
        print(head, end="")
      
     if(path[i+3]=="2") and not saut2 and not saut1:  #comme la tete fait trois caractères on s'y prend à l'avance de 3
        print(head, end="")  
     if(path[i+4]=="2") and not saut2 and saut1: #comme la tete fait trois caractères on s'y prend à l'avance de 3
        print(head, end="") 
      
     if(path[i]=="1") and  saut1:
        print(first_piece, end="")

     if(path[i+4]=="2") and saut2:           
        print(first_piece_d, end="")
    print()

    #TROISIÈME LIGNE
    for i in range(len(path)): 

     if(i==len(path)-5):
        break

     if(path[i]=="x"):
        print(" ", end="")

     if(path[i]=="_"):
        print(" ", end="")

     if(path[i]=="1") and not saut1:
        print(first_piece, end="")

     if(path[i+3]=="2") and not saut2 and saut1:
        print(first_piece_d, end="")

     if(path[i+5]=="2") and not saut2 and not saut1:
        print(first_piece_d, end="")

     if(path[i]=="1") and saut1:
        print(second_piece, end="")

     if(path[i+3]=="2") and saut2 and not saut1:
        print(second_piece_d, end="") 

    #QUATRIÈME LIGNE
    print()
    for i in range(len(path)): 

     if(path[i]=="_"):
        print(" ", end="")

     if(path[i]=="x"):
        print(" ", end="")

     if(path[i]=="1"):
        print(second_piece, end="")

     if(path[i]=="2"):
        print(second_piece_d, end="")

    print()

    #CINQUIÈME LIGNE
    for i in range(len(path)): 
     if(path[i]=="_"):
        print(" ", end="")

     if(path[i]=="x"):
        print(" ", end="")

     if(path[i]=="1") and not saut1:
        print(third_piece, end="")

     if(path[i]=="2") and not saut2:
        print(third_piece_d, end="")

     if(path[i]=="1") and  saut1:
        print(last_piece, end="")

     if(path[i]=="2") and  saut2:
        print(last_piece_d, end="")

    print()
    #SIXIÈME LIGNE 
    for i in range(len(path)):

     if(path[i]=="_"):
        print("_", end="")

     if(path[i]=="x"):
        print("x", end="")

     if(path[i]=="1") and not saut1:
        print(last_piece, end="")

     if(path[i]=="1") and  saut1:
        print("__", end="")

     if(path[i]=="2") and not saut2:
        print(last_piece_d, end="")

     if(path[i]=="2") and  saut2:
        print("__", end="")
    print() 

#Fonction qui affiche les différents controles 
def print_controls(): 
   print("""
    JOUEUR 1: 
    [Q] move left
    [D] move right
    [A] jump left 
    [E] jump right 
    [Z] attack 
    [S] block

    JOUEUR 2: 
    [<=] move left
    [=>] move right
    [L] jump left 
    [M] jump right 
    [O] attack 
    [F] block
    """) 

#constantes pour le menu
RESUME=1
PICK=3
SAVE=4
LOAD=5
AI=6
BASIC=7
QUIT=8
#affiche le menu 
def menu_pause():
 os.system('clear')
 print("""
    1.Resume
    2.Controls
    3.Pick a different scene
    4.Save game 
    5.Load last game
    6.Play Againt AI
    7.2 Players mode
    8.Quit game
    """)
 while True:
    ans=input("What would you like to do? ")
    print(ans)
    if ans[-1]=="1":
      return RESUME
    elif ans[-1]=="2":
      print_controls()
    elif ans[-1]=="3":
      return PICK
    elif ans[-1]=="4":
      return SAVE
    elif ans[-1]=="5":
      return LOAD
    elif ans[-1]=="6":
     return AI
    elif ans[-1]=="7":
     return BASIC
    elif ans[-1]=="8":
     return QUIT
    else:
       print("\n Not Valid Choice. Try again")

#fonction qui affiche les différents scènes disponibles 
def pick_scene():
   print("1-  ___1________x________2____")
   print("2-  ____1___x____x____x___2___")
   print("3-  ___1_______2___")
   print("4-  ______1_____x____2____")
  
   while True:
    ans=input("Pick a scene! ")
    if ans[-1]=="1":
      return "___1________x________2____"
    elif ans[-1]=="2":
      return "____1___x____x____x___2___"
    elif ans[-1]=="3":
      return "___1_______2___"
    elif ans[-1]=="4":
      return "______1_____x____2____"
    else:
       print("\n Not Valid Choice. Try again")

   

#FONCTIONS POUR LE MOUVEMENT 

#la fonction décalle le joueur à droite d'une case 
def shift_perso_droite(path, perso, mode_saut=False):
   obstacle=False
   index1= path.index("1")
   index2=path.index("2")
   if(index2-index1==5) and (perso==1):
      return path

   #determiner si y a un obstacle 

   if index1<len(path):
    if(perso==1) and path[index1+1]=="x":
      obstacle=True

   if index2<len(path)-1:
    if (perso==2) and path[index2+1]=="x":
      obstacle=True

   if mode_saut and obstacle:
      debut= str(perso)+"x__"
      fin="__x"+ str(perso)
      return path.replace(debut,fin)

   if mode_saut and not obstacle:  
      debut= str(perso)+"__"
      fin="__"+ str(perso)
      return path.replace(debut,fin)

   else:
      debut=str(perso)+"_" #1_
      fin="_"+str(perso)   #_2
      return path.replace(debut,fin)


#la fonction décalle le joueur d'une case à gauche
def shift_perso_gauche(path, perso, mode_saut=False):
   obstacle=False
   index1= path.index("1")
   index2=path.index("2")

   if(index2-index1==5) and (perso==2):
      return path

   if(perso==1) and path[index1-1]=="x":
      obstacle=True
   elif (perso==2) and path[index2-1]=="x":
      obstacle=True

   if mode_saut and obstacle:
      debut= "__x"+str(perso)
      fin= str(perso)+"x__"
      return path.replace(debut,fin)

   if mode_saut and not obstacle:
      debut= "__"+str(perso)
      fin= str(perso)+"__"
      return path.replace(debut,fin)

   else:
      debut="_"+str(perso) #1_
      fin=str(perso)+"_"   #_2
      return path.replace(debut,fin)

#FONCTIONS POUR ATTAQUER  

#cette fonction change l'etat des personnages 
def change_state_perso(perso, new_state): 
   if (perso==1) and new_state==States.ATTACK:
      print("ici")
      first_piece= " |__"
      print("ici first piece "+ first_piece)
      
   if (perso==2) and new_state==States.ATTACK:
      first_piece_d= "__|"
      
   if (perso==1) and new_state==States.BLOCK:
      first_piece= " |_|"

   if (perso==2) and new_state==States.BLOCK:
      first_piece_d= "|_|"
      
   if (perso==1) and new_state==States.REST:
      first_piece= " |_/"

   if (perso==2) and new_state==States.REST:
      first_piece_d= "\_|"


#Fonction qui détermine si l'adversaire est assez proche pour etre atteint d'une attaque 
def are_close_enough(path): 
   index1= path.index("1")
   index2=path.index("2")
   
   if(index2-index1==5):  
      return True
   else:
      return False

#FONCTION POUR SAVE 
def save_game():
   with open("last_game.ffscene", "w") as text_file:
            text_file.write(initial_path+"\n")
            text_file.write(str(score1)+"\n")
            text_file.write(str(score2)+"\n")


#Boolean pour ne pas passer d'un états à un autre 
move_right_bool1=False
move_right_bool2=False
move_left_bool1=False
move_left_bool2=False
block_bool1=False
block_bool2=False
saut_bool1=False
shift_while_saut1=False
descendre_1=False
saut_bool2=False
shift_while_saut2=False
descendre_2=False
saut_g_bool1=False
shift_while_saut_g1=False
descendre_g_1=False
saut_g_bool2=False
shift_while_saut_g2=False
descendre_g_2=False
attack_bool_1=False
attack_bool_2=False



#réucperer le temps de chaque action
move_right_time1=0
move_right_time2=0
move_left_time1=0
move_left_time2=0
block_time1=0
block_time2=0
temps_saut1=0
temps_saut1_1=0
temps_saut1_2=0
temps_saut2=0
temps_saut2_1=0
temps_saut2_2=0
temps_saut_g1=0
temps_saut_g1_1=0
temps_saut_g1_2=0
temps_saut_g2=0
temps_saut_g2_1=0
temps_saut_g2_2=0
attack_time_1=0
attack_time_2=0



play_AI=False
over=True
GAME=True

start_time=time.time()
while GAME:
    
    
    #PAUSE MENU 
    if keyboard.is_pressed("y"):
       PAUSE=True
       ans=menu_pause()
       if ans==RESUME: 
          continue 
       elif ans==QUIT: 
          GAME=False
       elif ans==PICK: 
          initial_path=pick_scene()
          path=initial_path
       elif ans==AI and not play_AI:
          play_AI=True
          score1=0
          score2=0
          initial_path=path
       elif ans==BASIC and play_AI:
          play_AI=False
          score1=0
          score2=0
          initial_path=path
       elif ans==SAVE:
          save_game()
       elif ans==LOAD:
          if(os.path.exists("last_game.ffscene")):
            with open("last_game.ffscene") as f:
             lines=f.readlines()
             path= lines[0]
             initial_path=lines[0]
             score1=int(lines[1])
             score2=int(lines[2])
          else: 
             print("No last game saved.")
             time.sleep(5)
       else: 
          continue


    #raffraichissement 
    if (time.time()  >= (1/fps + start_time)):
       print_scene(initial_path, state1, state2, saut1, saut2)
       start_time=time.time()
       AI_luck = random.randint(0,10)

    #AI 
    if(are_close_enough(initial_path)) and over and play_AI: #u need to attack/block/or maybe not
   
     if(AI_luck==0):    
       attack_time_2=time.time()
       attack_bool_2=True
       state2= States.ATTACK
       over=False 
     elif(AI_luck==1):
       block_time2=time.time()
       block_bool2=True
       state2=States.BLOCK
       over=False

    #MOUVEMENT

    if keyboard.is_pressed("q"):
        move_right_time1=time.time()
        move_right_bool1=True
       
    if (time.time() - move_right_time1 >= (movement_speed/fps)) and move_right_bool1: 
        initial_path=shift_perso_gauche(initial_path, 1)
        if play_AI:
         initial_path=shift_perso_droite(initial_path, 2)
        move_right_bool1=False

    if keyboard.is_pressed("d"):
        move_right_time2=time.time()
        move_right_bool2=True

    if (time.time()  >= (movement_speed/fps + move_right_time2)) and move_right_bool2:
        initial_path=shift_perso_droite(initial_path, 1)
        if(not are_close_enough(initial_path)) and play_AI:
         initial_path=shift_perso_gauche(initial_path, 2) 
        move_right_bool2=False

    if keyboard.is_pressed("right arrow") and not play_AI:
        move_left_time1=time.time()
        move_left_bool1=True

    if (time.time()  >= (movement_speed/fps + move_left_time1))and move_left_bool1:
        initial_path=shift_perso_droite(initial_path, 2)
        move_left_bool1=False
        
    if keyboard.is_pressed("left arrow") and not play_AI:
        move_left_time2=time.time()
        move_left_bool2=True

    if (time.time()  >= (movement_speed/fps + move_left_time2))and move_left_bool2:
        initial_path=shift_perso_gauche(initial_path, 2)
        move_left_bool2=False

    #ATTACK
    if keyboard.is_pressed("z"):   #JOUEUR 1  
        attack_time_1=time.time()
        attack_bool_1=True
        state1= States.ATTACK

    if (time.time() - attack_time_1 >= (attacking_speed/fps )) and attack_bool_1:
        #check relevance of attack
        if state2==States.REST and are_close_enough(initial_path):
           score1+=1
           initial_path=path
        attack_bool_1=False   
        state1= States.REST

    if keyboard.is_pressed("o") and not play_AI:   #JOUEUR 2
        attack_time_2=time.time()
        attack_bool_2=True
        state2= States.ATTACK

    if (time.time() - attack_time_2 >= (attacking_speed/fps )) and attack_bool_2:
        #check relevance of attack
        if state1==States.REST and are_close_enough(initial_path):
           score2+=1
           initial_path=path
        attack_bool_2=False   
        state2= States.REST
        if play_AI:
         over=True

    #BLOCK 
    if keyboard.is_pressed("s"):
        block_time1=time.time()
        block_bool1=True
        state1=States.BLOCK  
     
    if (time.time()  >= (blocking_time/fps + block_time1))and block_bool1:
        state1=States.REST
        block_bool1=False

    if keyboard.is_pressed("p") and not play_AI:
        block_time2=time.time()
        block_bool2=True
        state2=States.BLOCK

    if (time.time()  >= (blocking_time/fps + block_time2)) and block_bool2:
        state2=States.REST
        block_bool2=False
        if play_AI: 
           over=True

   #SAUT
   #JUMP RIGHT JOUEUR 1 
    if keyboard.is_pressed("e"):    
       temps_saut1=time.time()
       saut_bool1=True
       saut1=True

    if (time.time()  >= (movement_speed/fps + temps_saut1))and saut_bool1:
       temps_saut1_1=time.time()
       saut_bool1=False
       shift_while_saut1=True

    if (time.time()  >= (movement_speed/fps + temps_saut1_1))and shift_while_saut1:  #pour aller à droite 
       temps_saut1_2=time.time()
       initial_path=shift_perso_droite(initial_path, 1, True)
       shift_while_saut1=False
       descendre_1=True

    if (time.time()  >= (movement_speed/fps + temps_saut1_2))and descendre_1:
       saut1=False
       descendre_1=False

   #JUMP LEFT JOUEUR 1

    if keyboard.is_pressed("a"):    
       temps_saut_g1=time.time()
       saut_g_bool1=True
       saut1=True

    if (time.time()  >= (movement_speed/fps + temps_saut_g1))and saut_g_bool1:
       temps_saut_g1_1=time.time()
       saut_g_bool1=False
       shift_while_saut_g1=True

    if (time.time()  >= (movement_speed/fps + temps_saut_g1_1))and shift_while_saut_g1:  #pour aller à droite 
       temps_saut_g1_2=time.time()
       initial_path=shift_perso_gauche(initial_path, 1, True)
       shift_while_saut_g1=False
       descendre_g_1=True

    if (time.time()  >= (movement_speed/fps + temps_saut_g1_2))and descendre_g_1:
       descendre_g_1=False
       saut1=False

    #JUMP RIGHT JOUEUR 2
    if keyboard.is_pressed("m") and not play_AI:  
       temps_saut1=time.time()
       saut_bool2=True
       saut2=True

    if (time.time()  >= (movement_speed/fps + temps_saut1))and saut_bool2:
       temps_saut2_1=time.time()
       saut_bool2=False
       shift_while_saut2=True

    if (time.time()  >= (movement_speed/fps + temps_saut2_1))and shift_while_saut2:  #pour aller à droite 
       temps_saut2_2=time.time()
       initial_path=shift_perso_droite(initial_path, 2, True)
       shift_while_saut2=False
       descendre_2=True

    if (time.time()  >= (movement_speed/fps + temps_saut2_2))and descendre_2:
       descendre_2=False
       saut2=False

    #JUMP LEFT JOUEUR 2
    if keyboard.is_pressed("l") and not play_AI:    
       temps_saut_g2=time.time()
       saut_g_bool2=True
       saut2=True

    if (time.time()  >= (movement_speed/fps + temps_saut_g2))and saut_g_bool2:
       temps_saut_g2_1=time.time()
       saut_g_bool2=False
       shift_while_saut_g2=True

    if (time.time()  >= (movement_speed/fps + temps_saut_g2_1))and shift_while_saut_g2:  #pour aller à droite 
       temps_saut_g2_2=time.time()
       initial_path=shift_perso_gauche(initial_path, 2, True)
       shift_while_saut_g2=False
       descendre_g_2=True

    if (time.time()  >= (movement_speed/fps + temps_saut_g2_2))and descendre_g_2:
       descendre_g_2=False
       saut2=False

os.system("clear")