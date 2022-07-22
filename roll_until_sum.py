from random import randrange

print ("This program rolls two 6-sided ice until their sum is a given target value.")
    
input_sum = int(input("Enter the target sum to roll for: "))

def main():
    
 roll = 0
    
    if target< 2 or target> 13:
         
        print ("Enter a correct sum")
        
        return
    
    while roll != target:
        
        roll1 = randrange (1,7)
        roll2 = randrange (1,7)
        
        roll = roll1 + roll2
        
        output = "Roll: {} and {}, sum is {}".format (roll1,roll2,roll)
        
        print (output)
        
        if roll == target:
            
            print("Got it in ",roll," rolls")
            
            main()
