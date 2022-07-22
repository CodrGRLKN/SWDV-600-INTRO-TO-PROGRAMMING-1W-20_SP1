originalSales = input("Enter sales file name: ")
newSales = input("Enter name for total sales file: ")

original = open(originalSales, "r")
new = open(newSales, "w")

for total in original:
       
       firstnum, lastnum = line.split()
       
       totalSales = (firstnum[0]+lastnum[:1])
        
       print(totalsales, file=new)

original.close()
new.close()

print("Done writing totals to", newSales)

