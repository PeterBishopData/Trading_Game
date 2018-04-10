#Imports Modules
import csv
from itertools import zip_longest as z
import random
from tkinter import *

#A - Imports Data
#B - Publishes Merchant's Details
#F = Completes a Sale
#G - Completes a Purchase
#M - Sets New Prices
#N - Sails to New Port
#T - Make New Trade
#required flag
restartGame = 'Y'
#X - Exports the Data File


#A - Imports Data

with open('Data/Bank.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')
    
    for row in readCSV:
    
       bankAmount = int(row[2])
  
with open('Data/Cargo.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataListCargo = []
    
    for row in readCSV:
    
        slot= row[1]
        goods= row[2]
        amount= int(row[3])
        price = int(row[4])

        combo = [slot, goods, amount, price, '0']
        
        dataListCargo = dataListCargo + [combo]

with open('Data/Distances.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataListDistances = []
    
    for row in readCSV:
    
        port = row[0]
        d1 = int(row[1])
        d2 = int(row[2])
        d3 = int(row[3])
        d4 = int(row[4])

        combo = [port, d1, d2, d3, d4]
        
        dataListDistances = dataListDistances + [combo]

with open('Data/Merchant.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataListMerchant = []
    
    for row in readCSV:
    
        data = row[2]

        dataListMerchant = dataListMerchant + [data]

with open('Data/Port.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')
    
    for row in readCSV:
    
        portTrade = row[0]

with open('Data/TradeGoods.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataListSPrices = []
    
    for row in readCSV:
    
        place = row[1]
        goods = row[2]
        bprice = int(row[3])
        sprice = int(row[4])
        amount = int(row[5])
        forsale = int(row[6])
        pprice = int(row[7])

        combo = [place, goods, bprice, sprice, amount, forsale, pprice]
        
        dataListSPrices = dataListSPrices + [combo]


#B - Publishes Merchant's Details

class Merchant:
     
    def __init__(self):
        self.master = Tk()
        self.master.title('Merchant Details')
        self.master.geometry('200x140+50+50')
        self.master.configure(bg = "#FFFFFF" )
    
    #B1 - Display Widgits
    
        self.labelEntryA = Label(self.master, text = 'Merchant - ' + dataListMerchant[0])
        self.labelEntryA.place(x = 10, y = 0)
        self.labelEntryA.configure(bg = '#FFFFFF')
        
        self.labelEntryB = Label(self.master, text = 'Ship Type - ' + dataListMerchant[1] )
        self.labelEntryB.place(x = 10, y = 25)
        self.labelEntryB.configure(bg = '#FFFFFF')
        
        self.labelEntryC = Label(self.master, text = 'Ship Name - ' + dataListMerchant[2])
        self.labelEntryC.place(x = 10, y = 45)
        self.labelEntryC.configure(bg = '#FFFFFF')
        
        self.labelEntryB = Label(self.master, text = 'Capacity - ' + dataListMerchant[3]  + ' units')
        self.labelEntryB.place(x = 10, y = 70)
        self.labelEntryB.configure(bg = '#FFFFFF')
     
        self.activateButton = Button(self.master, text = 'Press',command = self.activateEntry)
        self.activateButton.place(x = 10, y = 95)
        self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
    
        self.master.mainloop()
    
    def activateEntry(self):
            
        self.master.destroy()
      
Merchant()


def main ():

#F = Completes a Sale

#F1 - Sets up Data for GUi

    length = len(dataListSPrices)
            
    for mark in range (0,3):
    
        if dataListCargo[mark][1] == 'None':
            dataListCargo[mark][4] =  0
            
        else:
            for counter in range (0, length):
                if dataListSPrices[counter][0] == portTrade:
                    if dataListCargo[mark][1] == dataListSPrices[counter][1]:
                        dataListCargo[mark][4] =  dataListSPrices[counter][6]

#F2 Creates a GUi for the Sale           
    class SellCargo:
    
        def __init__(self):
            self.master = Tk()
            self.master.title('Ship Cargo')
            self.master.geometry('380x120+50+50')
            self.master.configure(bg = "#FFFFFF" )

 #F2a - Display Widgits
    
            self.labelEntryTSl = Label(self.master, text = 'Ship')
            self.labelEntryTSl.place(x = 10, y = 0)
            self.labelEntryTSl.configure(bg = '#FFFFFF')
            
            self.labelEntry1 = Label(self.master, text = 'Slot 1')
            self.labelEntry1.place(x = 10, y = 20)
            self.labelEntry1.configure(bg = '#FFFFFF')
    
            self.labelEntry2 = Label(self.master, text = 'Slot 2')
            self.labelEntry2.place(x = 10, y = 40)
            self.labelEntry2.configure(bg = '#FFFFFF')
    
            self.labelEntry3 = Label(self.master, text = 'Slot 3')
            self.labelEntry3.place(x = 10, y = 60)
            self.labelEntry3.configure(bg = '#FFFFFF')
            
            self.labelEntry1TTG = Label(self.master, text = 'T Good')
            self.labelEntry1TTG.place(x = 50, y = 0)
            self.labelEntry1TTG.configure(bg = '#FFFFFF')
    
            self.labelEntry1C = Label(self.master, text = dataListCargo[0][1])
            self.labelEntry1C.place(x = 50, y = 20)
            self.labelEntry1C.configure(bg = '#FFFFFF')
    
            self.labelEntry2C = Label(self.master, text = dataListCargo[1][1])
            self.labelEntry2C.place(x = 50, y = 40)
            self.labelEntry2C.configure(bg = '#FFFFFF')
    
            self.labelEntry3C = Label(self.master, text = dataListCargo[2][1])
            self.labelEntry3C.place(x = 50, y = 60)
            self.labelEntry3C.configure(bg = '#FFFFFF')
            
            self.labelEntryTA = Label(self.master, text = 'Amount')
            self.labelEntryTA.place(x = 125, y = 0)
            self.labelEntryTA.configure(bg = '#FFFFFF')
            
            self.labelEntry1A = Label(self.master, text = dataListCargo[0][2])
            self.labelEntry1A.place(x = 125, y = 20)
            self.labelEntry1A.configure(bg = '#FFFFFF')
    
            self.labelEntry2A = Label(self.master, text = dataListCargo[1][2])
            self.labelEntry2A.place(x = 125, y = 40)
            self.labelEntry2A.configure(bg = '#FFFFFF')
    
            self.labelEntry3A = Label(self.master, text = dataListCargo[2][2])
            self.labelEntry3A.place(x = 125, y = 60)
            self.labelEntry3A.configure(bg = '#FFFFFF')
            
            self.labelEntryTP = Label(self.master, text = 'Purchase')
            self.labelEntryTP.place(x = 190, y = 0)
            self.labelEntryTP.configure(bg = '#FFFFFF')
            
            self.labelEntry1P = Label(self.master, text = dataListCargo[0][3])
            self.labelEntry1P.place(x = 190, y = 20)
            self.labelEntry1P.configure(bg = '#FFFFFF')
    
            self.labelEntry2P = Label(self.master, text = dataListCargo[1][3])
            self.labelEntry2P.place(x = 190, y = 40)
            self.labelEntry2P.configure(bg = '#FFFFFF')
    
            self.labelEntry3P = Label(self.master, text = dataListCargo[2][3])
            self.labelEntry3P.place(x = 190, y = 60)
            self.labelEntry3P.configure(bg = '#FFFFFF')
            
            self.labelEntryTS = Label(self.master, text = 'Sale P')
            self.labelEntryTS.place(x = 245, y = 0)
            self.labelEntryTS.configure(bg = '#FFFFFF')
            
            self.labelEntry1S = Label(self.master, text = dataListCargo[0][4])
            self.labelEntry1S.place(x = 245, y = 20)
            self.labelEntry1S.configure(bg = '#FFFFFF')
    
            self.labelEntry2S = Label(self.master, text = dataListCargo[1][4])
            self.labelEntry2S.place(x = 245, y = 40)
            self.labelEntry2S.configure(bg = '#FFFFFF')
    
            self.labelEntry3S = Label(self.master, text = dataListCargo[2][4])
            self.labelEntry3S.place(x = 245, y = 60)
            self.labelEntry3S.configure(bg = '#FFFFFF')
            
            self.labelEntryTIn = Label(self.master, text = 'Sale Qu')
            self.labelEntryTIn.place(x = 300, y = 0)
            self.labelEntryTIn.configure(bg = '#FFFFFF')
    
            self.variable1B = StringVar()
            self.labelEntry1B = Entry(self.master, textvariable = self.variable1B)
            self.labelEntry1B.place(x = 300, y = 20)
    
            self.variable2B = StringVar()
            self.labelEntry2B = Entry(self.master, textvariable = self.variable2B)
            self.labelEntry2B.place(x = 300, y = 40)
    
            self.variable3B = StringVar()
            self.labelEntry3B = Entry(self.master, textvariable = self.variable3B)
            self.labelEntry3B.place(x = 300, y = 60)
            
            self.activateButton = Button(self.master, text = 'Press to Trade',command = self.activateEntry)
            self.activateButton.place(x = 10, y = 90)
            self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
    
            self.master.mainloop()
    
#F3 - Transacts the Sale
    
        def activateEntry(self):
            
            self.master.destroy()
      
            saleamount1 = self.variable1B.get()
            saleamount2 = self.variable2B.get()
            saleamount3 = self.variable3B.get()
    
            global bankAmount
    
            if saleamount1 != '':
                dataListCargo[0][2]  = int(dataListCargo[0][2]) - int(saleamount1)
                bankAmount = bankAmount + int(saleamount1) * int(dataListCargo[0][4])
            if saleamount2 != '':
                dataListCargo[1][2]  = int(dataListCargo[1][2]) - int(saleamount2)
                bankAmount = bankAmount + int(saleamount2) * int(dataListCargo[1][4])
            if saleamount3 != '':
                dataListCargo[2][2]  = int(dataListCargo[2][2]) - int(saleamount3)
                bankAmount = bankAmount + int(saleamount3) * int(dataListCargo[2][4])
       
            for mark in range(0,3):
                if dataListCargo[mark][2] == 0:
                    dataListCargo[mark][1] = 'None'
                    dataListCargo[mark][3] =  0
            
    SellCargo()
    

#G Completes a Purchase
    
#G1 - Creates a Trade Goods for Sale List for the current Port for the GUI
    
    dataListTGCP = []
    dataListTGCP = [] + dataListSPrices
    
    length = len(dataListTGCP) - 1
    
    for mark in range(length, 0, -1):
            if dataListTGCP[mark][0] != portTrade:
                del dataListTGCP[mark]
       
    length = len(dataListTGCP) - 1
    
    for mark in range(length, -1, -1):
            if dataListTGCP[mark][5] != 1:
                del dataListTGCP[mark]
       
    if dataListTGCP[0][0] != portTrade:
        del dataListTGCP[0]
        
    displayListTGCP = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    length = len(dataListTGCP)
    
    for mark in range(0, length):
        displayListTGCP[mark][0] = dataListTGCP[mark][1]
        displayListTGCP[mark][1] = dataListTGCP[mark][3]
        displayListTGCP[mark][2] = dataListTGCP[mark][4]
    
    allowedCargo = int(dataListMerchant[3]) - int(dataListCargo[0][2]) - int(dataListCargo[1][2]) - int(dataListCargo[2][2])
    
    
#G2 - Creates a GUI for Purchasing
    
    class PurchaseCargo:
    
        def __init__(self):
            self.master = Tk()
            self.master.title('Purchasing Trade Goods at ' + portTrade)
            self.master.geometry('380x330+50+50')
            self.master.configure(bg = "#FFFFFF" )
    
    
#G2a - Display Widgits
    
            self.labelEntryTTG = Label(self.master, text = 'T Good')
            self.labelEntryTTG.place(x = 10, y = 0)
            self.labelEntryTTG.configure(bg = '#FFFFFF')
            
            self.labelEntry1 = Label(self.master, text = displayListTGCP[0][0])
            self.labelEntry1.place(x = 10, y = 20)
            self.labelEntry1.configure(bg = '#FFFFFF')
    
            self.labelEntry2 = Label(self.master, text =  displayListTGCP[1][0])
            self.labelEntry2.place(x = 10, y = 40)
            self.labelEntry2.configure(bg = '#FFFFFF')
    
            self.labelEntry3 = Label(self.master, text =  displayListTGCP[2][0])
            self.labelEntry3.place(x = 10, y = 60)
            self.labelEntry3.configure(bg = '#FFFFFF')
            
            self.labelEntry4 = Label(self.master, text =  displayListTGCP[3][0])
            self.labelEntry4.place(x = 10, y = 80)
            self.labelEntry4.configure(bg = '#FFFFFF')
    
            self.labelEntry5 = Label(self.master, text =  displayListTGCP[4][0])
            self.labelEntry5.place(x = 10, y = 100)
            self.labelEntry5.configure(bg = '#FFFFFF')
            
            self.labelEntryTP = Label(self.master, text = 'Price')
            self.labelEntryTP.place(x = 85, y = 0)
            self.labelEntryTP.configure(bg = '#FFFFFF')
            
            self.labelEntry1P = Label(self.master, text = displayListTGCP[0][1])
            self.labelEntry1P.place(x = 85, y = 20)
            self.labelEntry1P.configure(bg = '#FFFFFF')
    
            self.labelEntry2P = Label(self.master, text = displayListTGCP[1][1])
            self.labelEntry2P.place(x = 85, y = 40)
            self.labelEntry2P.configure(bg = '#FFFFFF')
    
            self.labelEntry3P = Label(self.master, text = displayListTGCP[2][1])
            self.labelEntry3P.place(x = 85, y = 60)
            self.labelEntry3P.configure(bg = '#FFFFFF')
            
            self.labelEntry4P = Label(self.master, text = displayListTGCP[3][1])
            self.labelEntry4P.place(x = 85, y = 80)
            self.labelEntry4P.configure(bg = '#FFFFFF')
    
            self.labelEntry5P = Label(self.master, text = displayListTGCP[4][1])
            self.labelEntry5P.place(x = 85, y = 100)
            self.labelEntry5P.configure(bg = '#FFFFFF')
        
            self.labelEntryTA = Label(self.master, text = 'Amount')
            self.labelEntryTA.place(x = 130, y = 0)
            self.labelEntryTA.configure(bg = '#FFFFFF')
            
            self.labelEntry1A = Label(self.master, text = displayListTGCP[0][2])
            self.labelEntry1A.place(x = 130, y = 20)
            self.labelEntry1A.configure(bg = '#FFFFFF')
    
            self.labelEntry2A = Label(self.master, text = displayListTGCP[1][2])
            self.labelEntry2A.place(x = 130, y = 40)
            self.labelEntry2A.configure(bg = '#FFFFFF')
    
            self.labelEntry3A = Label(self.master, text = displayListTGCP[2][2])
            self.labelEntry3A.place(x = 130, y = 60)
            self.labelEntry3A.configure(bg = '#FFFFFF')
            
            self.labelEntry4A = Label(self.master, text = displayListTGCP[3][2])
            self.labelEntry4A.place(x = 130, y = 80)
            self.labelEntry4A.configure(bg = '#FFFFFF')
    
            self.labelEntry5A = Label(self.master, text = displayListTGCP[4][2])
            self.labelEntry5A.place(x = 130, y = 100)
            self.labelEntry5A.configure(bg = '#FFFFFF')
            
            self.labelEntryTQ = Label(self.master, text = 'Quantity')
            self.labelEntryTQ.place(x = 195, y = 0)
            self.labelEntryTQ.configure(bg = '#FFFFFF')
            
            self.variable1Q = StringVar()
            self.labelEntry1Q = Entry(self.master, textvariable = self.variable1Q)
            self.labelEntry1Q.place(x = 195, y = 20)
            
            self.variable2Q = StringVar()
            self.labelEntry2Q = Entry(self.master, textvariable = self.variable2Q)
            self.labelEntry2Q.place(x = 195, y = 40)
            
            self.variable3Q = StringVar()
            self.labelEntry3Q = Entry(self.master, textvariable = self.variable3Q)
            self.labelEntry3Q.place(x = 195, y = 60)
            
            self.variable4Q = StringVar()
            self.labelEntry4Q = Entry(self.master, textvariable = self.variable4Q)
            self.labelEntry4Q.place(x = 195, y = 80)
            
            self.variable5Q = StringVar()
            self.labelEntry5Q = Entry(self.master, textvariable = self.variable5Q)
            self.labelEntry5Q.place(x = 195, y = 100)
            
            self.labelEntryTS = Label(self.master, text = 'Slot')
            self.labelEntryTS.place(x = 265, y = 0)
            self.labelEntryTS.configure(bg = '#FFFFFF')
            
            self.variable1S = StringVar()
            self.labelEntry1S = Entry(self.master, textvariable = self.variable1S)
            self.labelEntry1S.place(x = 265, y = 20)
            
            self.variable2S = StringVar()
            self.labelEntry2S = Entry(self.master, textvariable = self.variable2S)
            self.labelEntry2S.place(x = 265, y = 40)
            
            self.variable3S = StringVar()
            self.labelEntry3S = Entry(self.master, textvariable = self.variable3S)
            self.labelEntry3S.place(x = 265, y = 60)
            
            self.variable4S = StringVar()
            self.labelEntry4S = Entry(self.master, textvariable = self.variable4S)
            self.labelEntry4S.place(x = 265, y = 80)
            
            self.variable5S = StringVar()
            self.labelEntry5S = Entry(self.master, textvariable = self.variable5S)
            self.labelEntry5S.place(x = 265, y = 100)
            
            self.labelallowed = Label(self.master, text = 'You can purchase trade goods up to ' + str(allowedCargo) + ' units')
            self.labelallowed.place(x = 10, y = 135)
            self.labelallowed.configure(bg = '#FFFFFF')
            
            self.labelallowed = Label(self.master, text = 'You are have ' + str(bankAmount) + ' ducats')
            self.labelallowed.place(x = 10, y = 155)
            self.labelallowed.configure(bg = '#FFFFFF')
            
            
            self.labelEntryTSl = Label(self.master, text = 'Current Cargo')
            self.labelEntryTSl.place(x = 10, y = 180)
            self.labelEntryTSl.configure(bg = '#FFFFFF')
    
            self.labelEntryTSl = Label(self.master, text = 'Ship')
            self.labelEntryTSl.place(x = 10, y = 200)
            self.labelEntryTSl.configure(bg = '#FFFFFF')
            
            self.labelEntry1 = Label(self.master, text = 'Slot 1')
            self.labelEntry1.place(x = 10, y = 220)
            self.labelEntry1.configure(bg = '#FFFFFF')
    
            self.labelEntry2 = Label(self.master, text = 'Slot 2')
            self.labelEntry2.place(x = 10, y = 240)
            self.labelEntry2.configure(bg = '#FFFFFF')
    
            self.labelEntry3 = Label(self.master, text = 'Slot 3')
            self.labelEntry3.place(x = 10, y =260)
            self.labelEntry3.configure(bg = '#FFFFFF')
            
            self.labelEntry1TTG = Label(self.master, text = 'T Good')
            self.labelEntry1TTG.place(x = 50, y = 200)
            self.labelEntry1TTG.configure(bg = '#FFFFFF')
    
            self.labelEntry1C = Label(self.master, text = dataListCargo[0][1])
            self.labelEntry1C.place(x = 50, y = 220)
            self.labelEntry1C.configure(bg = '#FFFFFF')
    
            self.labelEntry2C = Label(self.master, text = dataListCargo[1][1])
            self.labelEntry2C.place(x = 50, y = 240)
            self.labelEntry2C.configure(bg = '#FFFFFF')
    
            self.labelEntry3C = Label(self.master, text = dataListCargo[2][1])
            self.labelEntry3C.place(x = 50, y = 260)
            self.labelEntry3C.configure(bg = '#FFFFFF')
            
            self.labelEntryTA = Label(self.master, text = 'Amount')
            self.labelEntryTA.place(x = 125, y = 200)
            self.labelEntryTA.configure(bg = '#FFFFFF')
            
            self.labelEntry1A = Label(self.master, text = dataListCargo[0][2])
            self.labelEntry1A.place(x = 125, y = 220)
            self.labelEntry1A.configure(bg = '#FFFFFF')
    
            self.labelEntry2A = Label(self.master, text = dataListCargo[1][2])
            self.labelEntry2A.place(x = 125, y = 240)
            self.labelEntry2A.configure(bg = '#FFFFFF')
    
            self.labelEntry3A = Label(self.master, text = dataListCargo[2][2])
            self.labelEntry3A.place(x = 125, y = 260)
            self.labelEntry3A.configure(bg = '#FFFFFF')
            
            self.activateButton = Button(self.master, text = 'Press to Trade', command = self.activateEntry )
            self.activateButton.place(x = 10, y = 290)
            self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
           
            self.master.mainloop()
    
#G3 - Tranactioning the Purchase
    
        def activateEntry(self):
            
            self.master.destroy()
        
            purchaseamount1 = self.variable1Q.get()
            purchaseamount2 = self.variable2Q.get()
            purchaseamount3 = self.variable3Q.get()
            purchaseamount4 = self.variable4Q.get()
            purchaseamount5 = self.variable5Q.get()
                
            positionslot1 = self.variable1S.get()
            positionslot2 = self.variable2S.get()
            positionslot3 = self.variable3S.get()
            positionslot4 = self.variable4S.get()
            positionslot5 = self.variable5S.get()
                
            dataNewPurchase = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
                
            if purchaseamount1 != '':
                dataNewPurchase[0][0] = positionslot1
                dataNewPurchase[0][1] = displayListTGCP[0][0]
                dataNewPurchase[0][2] = purchaseamount1
                dataNewPurchase[0][3] = displayListTGCP[0][1]
            if purchaseamount2 != '':
                dataNewPurchase[1][0] = positionslot2
                dataNewPurchase[1][1] = displayListTGCP[1][0]
                dataNewPurchase[1][2] = purchaseamount2        
                dataNewPurchase[1][3] = displayListTGCP[1][1]
            if purchaseamount3 != '':
                dataNewPurchase[2][0] = positionslot3
                dataNewPurchase[2][1] = displayListTGCP[2][0]
                dataNewPurchase[2][2] = purchaseamount3          
                dataNewPurchase[2][3] = displayListTGCP[2][1]
            if purchaseamount4 != '':
                dataNewPurchase[3][0] = positionslot4
                dataNewPurchase[3][1] = displayListTGCP[3][0]
                dataNewPurchase[3][2] = purchaseamount1        
                dataNewPurchase[3][3] = displayListTGCP[3][1]
            if purchaseamount5 != '':
                dataNewPurchase[4][0] = positionslot4
                dataNewPurchase[4][1] = displayListTGCP[4][0]
                dataNewPurchase[4][2] = purchaseamount1
                dataNewPurchase[4][3] = displayListTGCP[4][1]
                
            global dataListCargo
            
            global bankAmount
    
            for mark in range(0,5):
                if dataNewPurchase[mark][0] == '1':
                    bankAmount = bankAmount - int(dataNewPurchase[mark][2]) * int(dataNewPurchase[mark][3])
                    if dataListCargo[0][1] == dataNewPurchase[mark][1]:
                        comboamount = int(dataListCargo[0][2]) + int(dataNewPurchase[mark][2])
                        dataListCargo[0][3] = int((int(dataListCargo[0][3]) * int(dataListCargo[0][2]) + int(dataNewPurchase[mark][3]) * int(dataNewPurchase[mark][2]))/comboamount)
                        dataListCargo[0][2] = comboamount
                    else:
                        dataListCargo[0][1] = dataNewPurchase[mark][1]
                        dataListCargo[0][2] = int(dataNewPurchase[mark][2])
                        dataListCargo[0][3] = int(dataNewPurchase[mark][3])
                elif dataNewPurchase[mark][0] == '2':
                    bankAmount = bankAmount - int(dataNewPurchase[mark][2]) * int(dataNewPurchase[mark][3])
                    if dataListCargo[1][1] == dataNewPurchase[mark][1]:
                        comboamount = int(dataListCargo[1][2]) + int(dataNewPurchase[mark][2])
                        dataListCargo[1][3] = int((int(dataListCargo[1][3]) * int(dataListCargo[1][2]) + int(dataNewPurchase[mark][3]) * int(dataNewPurchase[mark][2]))/comboamount)
                        dataListCargo[1][2] = comboamount
                    else:
                        dataListCargo[1][1] = dataNewPurchase[mark][1]
                        dataListCargo[1][2] = int(dataNewPurchase[mark][2])
                        dataListCargo[1][3] = int(dataNewPurchase[mark][3])
                elif dataNewPurchase[mark][0] == '3':
                    bankAmount = bankAmount - int(dataNewPurchase[mark][2]) * int(dataNewPurchase[mark][3])
                    if dataListCargo[2][1] == dataNewPurchase[mark][1]:
                        comboamount = int(dataListCargo[2][2]) + int(dataNewPurchase[mark][2])
                        dataListCargo[2][3] = int((int(dataListCargo[2][3]) * int(dataListCargo[2][2]) + int(dataNewPurchase[mark][3]) * int(dataNewPurchase[mark][2]))/comboamount)
                        dataListCargo[2][2] = comboamount
                    else:
                        dataListCargo[2][1] = dataNewPurchase[mark][1]
                        dataListCargo[2][2] = int(dataNewPurchase[mark][2])
                        dataListCargo[2][3] = int(dataNewPurchase[mark][3])
                 
    PurchaseCargo()
    

#M Sets New Prices

    length = len(dataListSPrices)
    
    for mark in range (0, length):
    
       factorSP = 0.075 * (random.random() - 0.5)
       dataListSPrices[mark][3] = int(int(dataListSPrices[mark][3]) + float(dataListSPrices[mark][2]) * factorSP)
    
       if dataListSPrices[mark][5] == 1:
          factorPP = 0.075 * (random.random() - 0.5)
          dataListSPrices[mark][6] = int(int(dataListSPrices[mark][6]) + float(dataListSPrices[mark][2]) * factorPP)
    

#N - Sail to New Port

#N1 - Sets Up Port Lists

    dataListDistancesC = [] + dataListDistances
        
    dataListDestination = []
            
    length = len(dataListDistancesC)
        
    for mark in range (0, length):
        if portTrade != dataListDistances [mark][0]:
            dataListDestination = dataListDestination + [dataListDistances[mark][0]]
        
    for mark in range (length - 1, -1, -1):
        if portTrade != dataListDistancesC [mark][0]:
            del dataListDistancesC[mark]
            
    for mark in range (0, length):
        if dataListDistancesC[0][mark] == 0:
            del dataListDistancesC[0][mark]

#N2 - Sets up GUi for Ports

    class PortToPort:
         
        def __init__(self):
            self.master = Tk()
            self.master.title('Sailing to New Port')
            self.master.geometry('200x160+50+50')
            self.master.configure(bg = "#FFFFFF" )
        
#N2a - Display Widgits
        
            self.labelEntryTSl = Label(self.master, text = 'Current Port - ' + portTrade)
            self.labelEntryTSl.place(x = 10, y = 0)
            self.labelEntryTSl.configure(bg = '#FFFFFF')
            
            self.labelEntryTSl = Label(self.master, text = 'Distance to')
            self.labelEntryTSl.place(x = 70, y = 30)
            self.labelEntryTSl.configure(bg = '#FFFFFF')
            
            self.labelEntryPl = Label(self.master, text = dataListDestination[0])
            self.labelEntryPl.place(x = 10, y = 50)
            self.labelEntryPl.configure(bg = '#FFFFFF')
            
            self.labelEntryD1 = Label(self.master, text = str(dataListDistancesC[0][1])  + ' days' )
            self.labelEntryD1.place(x = 90, y = 50)
            self.labelEntryD1.configure(bg = '#FFFFFF')
            
            self.labelEntryP2 = Label(self.master, text = dataListDestination[1])
            self.labelEntryP2.place(x = 10, y = 70)
            self.labelEntryP2.configure(bg = '#FFFFFF')
            
            self.labelEntryD2 = Label(self.master, text = str(dataListDistancesC[0][2])  + ' days' )
            self.labelEntryD2.place(x = 90, y = 70)
            self.labelEntryD2.configure(bg = '#FFFFFF')
            
            self.labelEntryP3 = Label(self.master, text = dataListDestination[2])
            self.labelEntryP3.place(x = 10, y = 90)
            self.labelEntryP3.configure(bg = '#FFFFFF')
            
            self.labelEntryD3 = Label(self.master, text = str(dataListDistancesC[0][3])  + ' days' )
            self.labelEntryD3.place(x = 90, y = 90)
            self.labelEntryD3.configure(bg = '#FFFFFF')
        
            self.variable1S = StringVar()
            self.labelEntry1S = Entry(self.master, textvariable = self.variable1S)
            self.labelEntry1S.place(x = 150, y = 50)
              
            self.variable2S = StringVar()
            self.labelEntry2S = Entry(self.master, textvariable = self.variable2S)
            self.labelEntry2S.place(x = 150, y = 70)
        
            self.variable3S = StringVar()
            self.labelEntry3S = Entry(self.master, textvariable = self.variable3S)
            self.labelEntry3S.place(x = 150, y = 90)
                
            self.activateButton = Button(self.master, text = 'Press to Sail',command = self.activateEntry)
            self.activateButton.place(x = 10, y = 120)
            self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
        
            self.master.mainloop()
        
#N3 - Sail to New Port
        
        def activateEntry(self):
                
            self.master.destroy()
          
            sail1 = self.variable1S.get()
            sail2 = self.variable2S.get()
            sail3 = self.variable3S.get()
               
            global portTrade
                
            if sail1 == 'x':
                portTrade = dataListDestination[0]
            if sail2 == 'x':
                portTrade = dataListDestination[1]
            if sail3 == 'x':
                portTrade = dataListDestination[2]

    PortToPort()

#T - Make New Trade Question

    class Option:
         
        def __init__(self):
            self.master = Tk()
            self.master.title('Option to Continue')
            self.master.geometry('200x100+50+50')
            self.master.configure(bg = "#FFFFFF" )
        
        #F1 - Display Widgits
        
            self.labelEntryTSl = Label(self.master, text = 'You have arrived at - ' + portTrade)
            self.labelEntryTSl.place(x = 10, y = 0)
            self.labelEntryTSl.configure(bg = '#FFFFFF')
            
            self.labelEntryD1 = Label(self.master, text = 'Do you want to continue the game Y/N')
            self.labelEntryD1.place(x = 10, y = 25)
            self.labelEntryD1.configure(bg = '#FFFFFF')
        
            self.variableO = StringVar()
            self.labelEntry3S = Entry(self.master, textvariable = self.variableO)
            self.labelEntry3S.place(x = 10, y = 45)
                
            self.activateButton = Button(self.master, text = 'Press to Reply',command = self.activateEntry)
            self.activateButton.place(x = 10, y = 60)
            self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')
        
            self.master.mainloop()
        
        #B2 - Sail to New Port
        
        def activateEntry(self):
                
            self.master.destroy()
          
            optionContinue = self.variableO.get()
            
            global restartGame
    
            restartGame = optionContinue   
    
    Option()

    global restartGame
    
    if restartGame == 'Y':
        main()

    else:
   
#X - Exports Data Files

       newData = [[0], ['Bank'], [bankAmount]]
       
       exportData = z(*newData, fillvalue = '')  
       
       with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Trading Game/Data/Bank.csv','w', newline ='') as newFile:
             writer = csv.writer(newFile)
             writer.writerows(exportData)
             newFile.close()
       
       refCargo = [0, 1, 2]
       slotCargo = []
       goodsCargo  = []
       amountCargo = []
       priceCargo = []
       
       for mark in range (0, 3):
       
           slotCargo = slotCargo  + [dataListCargo[mark][0]] 
           goodsCargo  = goodsCargo + [dataListCargo[mark][1]] 
           amountCargo = amountCargo + [dataListCargo[mark][2]] 
           priceCargo = priceCargo + [dataListCargo[mark][3]]
           
       newData = [refCargo, slotCargo, goodsCargo, amountCargo, priceCargo]
       
       exportData = z(*newData, fillvalue = '')  
       
       with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Trading Game/Data/Cargo.csv','w', newline ='') as newFile:
             writer = csv.writer(newFile)
             writer.writerows(exportData)
             newFile.close()
        
       newData = [[portTrade]]

       exportData = z(*newData, fillvalue = '')  

       with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Trading Game/Data/Port.csv','w', newline ='') as newFile:
          writer = csv.writer(newFile)
          writer.writerows(exportData)
          newFile.close()
        
       
       refTGoods = []
       placeTGoods = []
       goodsTGoods = []
       priceBTGoods = []
       pricePTGoods = []
       amountTGoods = []
       forsaleTGoods = []
       priceSTGoods = []
       
       length = len(dataListSPrices)
       
       for mark in range (0, length):
       
           refTGoods = refTGoods + [mark]
           placeTGoods = placeTGoods + [dataListSPrices[mark][0]]
           goodsTGoods = goodsTGoods + [dataListSPrices[mark][1]]
           priceBTGoods = priceBTGoods + [dataListSPrices[mark][2]]
           pricePTGoods = pricePTGoods + [dataListSPrices[mark][3]]
           amountTGoods = amountTGoods + [dataListSPrices[mark][4]]
           forsaleTGoods = forsaleTGoods + [dataListSPrices[mark][5]]
           priceSTGoods = priceSTGoods + [dataListSPrices[mark][6]]
           
       newData = [refTGoods, placeTGoods, goodsTGoods, priceBTGoods, pricePTGoods, amountTGoods, forsaleTGoods, priceSTGoods]
       
       exportData = z(*newData, fillvalue = '')  
       
       with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Trading Game/Data/TradeGoods.csv','w', newline ='') as newFile:
             writer = csv.writer(newFile)
             writer.writerows(exportData)
             newFile.close()
       
       print('All Done')
       
       quit()

main()

       
