print('This program tests if the sequence of positive numbers you input are unique')
print('Enter -1 to quit')

ul = []
x =set()

number = int(input("Enter a number (Enter -1 to quit) >> "))

while number!=-1:
    
    ul.append(number )
    
    x.add(number)
    
    number = int(input("Enter a number (Enter -1 to quit) >> "))
    
if len(x)!=len(ul):
    
    print('The sequence',ul,'is NOT unique!')
    
else:
    print('The sequence',ul,'is unique!')