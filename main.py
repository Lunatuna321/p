
#Housing
DHRC = 2000 / 30                       #Daily House renting cost

#School (for 3 months)
Tuitions = 3637                        #Tuitions
MMI = 483                              #Mandatory Medical Insurance
books_and_supplies = 176               #Books & Supplies
Computers = 144
Room_and_Board = 4576
Miscellaneous = 616

Total_School_Cost = 9632

Daily_School_Cost = Total_School_Cost / 90

#Misc
Food = 15                               #One meal (Ingredients) / Purchase outside
DFC = 15 * 3                            #Daily food cost

Flight = 13000 / 7                      #Flight round trip

#Empolyment Cost
DriverCost = 20     # Driver cost $20 per hour
FuelCost = 7        # 7 miles per $1
Driving = 1.5 * DriverCost + 18 / FuelCost

Cook = 15 * 3       

Inflation = 0.033 


def toMonthlyCost(cost):
    pass

print(toMonthlyCost(1000))