#Mary had a little lamb
#little lamb, little lamb
#Mary had a little lamb
#Whose fleece was white as snow
#And everywhere that Mary went

def mary():
    return " Mary"

def lamb():
    return "lamb"
    
def hada():
    print (mary(), "had a little", lamb())

def little(animal):
    print ("little", lamb(), "little", lamb())

def fleece(white):
    print("whose fleece was", white+",", "as snow.")

def verse(lamb, white):
    hada()
    little(lamb)
    fleece(white)
    hada()

def main():
    for w in [("blue"), ("green"), ("yellow")]:
        verse(w)
        print()

main()
