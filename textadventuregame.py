from random import random
import amo

class Player:
    

    def __init__(self, name, gold, healthpoints):
        self.name = name
        self.position = 0
        self.gold = coins
        self.healthpoints = healthpoints
        self.weapons = [amo.Sword(), amo.MagicLasso(), amo.Bat()]

        
        
class Enemy:
   
    def __init__(self, name, position, introduction, damage):
        self.name = name
        self.position = 0
        self.introduction = introduction
        self.damage = damage
        
class Swiperfox(Enemy):
    def _int_(self):
        self.name = "Swiper Fox"
        self.postion = 0
        self.damage = 30
        
class LennytheLeprechaun(Enemy):
    def _int_(self):
        self.name = "Lenny the Leprechaun"
        self.damage = 100
        
        
class Game:

    def play(adventurer, enemies, trail):
        
        for i in range(1,trail+1):
            input("Only 10 steps left. Step forward (y/n)?" )
        
        adventurer.position = i
        
        print(adventurer.name + " is at " + str(adventurer.position))
        
        for enemy in enemies:
            if adventurer.position == enemy.position:
               
                adventurer.health_points -= enemy.damage
                
                print("Got attacked by " + enemy.name + " and lost " + str(enemy.damage) + " health_points")
                break
        else: 
            pickup = random.randint(10, 50)
            adventurer.coins += pickup
            
            print("Recieved " + str(pickup) + " coins")
        
        if adventurer.health_points <= 0:
            print("\n\n" + adventurer.name + " lost")
            
            break
        
        else:
            
            print("""You've made it to the pot of gold...
....You've won! Hooray!!!""")

def main():
    def main():
        trail = 10
        adventurer = Adventurer("", 0, 100)
        attackers= r = random.random()
        
        if r < 0.50:
         self.Attacker= enemy.SwiperFox()
         
         self.alive_text = " A fox called Swiper Fox jumps from behind a tree" \
                           "he's blocking your path to the pot of gold!"
         self.dead_text = "the fox is defeated"
        else:
         self.Attacker = enemy.LennytheLeprechaun()
         self.alive_text = " Lenny the Leprechaun is protecing his pot of gold"
         self.dead_text = "Lenny hands the pot of gold to you"
        
    play(adventurer, enemies, trail) 
    
main()
input("\nPress <Enter> to quit")
