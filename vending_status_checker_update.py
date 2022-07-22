import json

class InventoryItem:
    def __init__( self, itemName ):
        self.name = itemName
        self.totalStocked = 0
        self.totalInStock = 0
        self.totalSlots = 0
        
    def addToStocked( self, stockAmt ):
        self.totalStocked = self.totalStocked + stockAmt
        
    def addToInStock( self, inStockAmt ):
        self.totalInStock = self.totalInStock + inStockAmt
        
    def incrementSlots( self ):
        self.totalSlots = self.totalSlots + 1

    def getNumberSold( self ):
        return self.totalStocked - self.totalInStock
    
    def getSoldPct( self ):
        return self.getNumberSold() / self.totalStocked
    
    def getStockNeed( self ):
        return 8 * self.totalSlots - self.totalInStock
    
    def getName( self ):
        return self.name

    def getNumberInStock( self ):
        return self.totalInStock

    def __repr__( self ):
        return '{} In Stock: {}, Stocked: {}, Slots: {}'.format( self.name, self.totalInStock, self.totalStocked, self.totalSlots )


class MachineStatus:

    def __init__( self, machineName ):
        self.name = machineName
        self.previousStocked = 0
        self.totalcurrentInStock = 0
        self.totalIncome = 0
        
    def updatePreviousStocked(self, previousStocked):
        self.previousStocked = self.previousStocked + previousStocked
        
    
    def updateTotalCurrentInStock(self, totalcurrentInStock):
        self.totalcurrentInStock = self.totalcurrentInStock + totalcurrentInStock
        
        
    def updateIncome(self, income):
        self.totalIncome = self.totalIncome + income
    
    def getPctSold(self):
        return (self.previousStocked - self.totalcurrentInStock) / self.previousStocked * 100

    def getName(self):
        return self.name
    
    def gettotalcurrentInStock (self):
        return self.totalcurrentInStock 
    
    def getpreviousStocked(self):
        return self.previousStocked
    
    def getTotalIncome(self):
        return self.totalIncome
    
    def __repr__(self):
        return "Name {}, Income {}, PCt Sold {:2f}".format(self.name, self.totalIncome, self.getPctSold())
        


def main():
    inventoryFileNames = ["REID_1F_20171004.json", "REID_2F_20171004.json", "REID_3F_20171004.json"]
    
    itemNameToInventoryItem = {}
    machineStatusDictionary = {}
    
    
    for inventoryFileName in inventoryFileNames: 
        inventoryFile = open( inventoryFileName, 'r' )
        
        inventoryData = json.loads( inventoryFile.read() )
         
        contents = inventoryData['contents']
        for row in contents:
            for slot in row['slots']:
                itemName = slot['item_name']
                inventoryItem = itemNameToInventoryItem.get( itemName, InventoryItem( itemName ) )
                
                inventoryItem.addToStocked( slot['last_stock'] )
                inventoryItem.addToInStock( slot['current_stock'] )
                inventoryItem.incrementSlots();
                
                machineName = inventoryData['machine_label']
                machineStatus = machineStatusDictionary.get( machineName, MachineStatus(machineName) )
                
                machineStatus.updateIncome(slot['item_price']*(slot['last_stock']-slot['current_stock']))
                machineStatus.updatePreviousStocked(slot['last_stock'])
                machineStatus.updateTotalCurrentInStock(slot['current_stock'])
                
                
                itemNameToInventoryItem[itemName] = inventoryItem
                machineStatusDictionary[machineName] = machineStatus
                 
    sortChoice = input('Would you like the (m)achine report or (i)nventory report? ')
    
    inventoryItemsList = list( itemNameToInventoryItem.values() )
    machineStatusList = list(machineStatusDictionary.values())
    
    if sortChoice == 'm':
        print('{:15} {:15} {:10}'.format('Machine Name', 'Percent Sold', 'Sales Total'))
        for item in machineStatusList:
            print('{:10} {:10.2f}%          ${:8.2f}'.format(item.getName(), item.getPctSold(), item.getTotalIncome()))
    elif sortChoice == 'i':
        
        while sortChoice != 'q':
            sortChoice = input('Sort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ')
        if sortChoice == 'n':
            inventoryItemsList.sort( key=InventoryItem.getName )
        elif sortChoice == 'p':
            inventoryItemsList.sort( key=InventoryItem.getSoldPct )
            inventoryItemsList.reverse()
        elif sortChoice == 's':
            inventoryItemsList.sort( key=InventoryItem.getStockNeed )
            inventoryItemsList.reverse()
        
        print( 'Item Name            Sold     % Sold     In Stock Stock needs')
        for item in inventoryItemsList:
            print( '{:20} {:8} {:8.2f}% {:8} {:8}'.format( item.getName(), item.getNumberSold(), item.getSoldPct() * 100, item.getNumberInStock(), item.getStockNeed()))
        print()
    
main()
