#importing operating system, statistics, and csv module

import os 
import statistics
import csv 

#variables

#Month Count
Mnt_Ct= 0 
#Total Amts
Total = 0 
#profit/loss list
Prof_Loss = [] 
#month list
ListMnt=[] 
#monthlychange list
MntChange= [] 

#read and input CSV file

budget_data = os.path.join("resources/budget_data.csv") 
with open(budget_data, newline ='') as csvfile: 
    reader = csv.reader(csvfile, delimiter= ',')
    header= next(reader)  
#total Months in Data
    for row in reader: 
        Mnt_Ct += 1 
        Total += int(row[1])
        ListMnt.append(row[0])

#The net total amount of "Profit/Losses" over the entire period       

        Prof_Loss.append(row[1])

Mnt_Prof_Loss =int(Prof_Loss[0])
             
for x in range(1,len(Prof_Loss)):
    MntChange.append(int(Prof_Loss[x])- Mnt_Prof_Loss)
    Mnt_Prof_Loss = int(Prof_Loss[x])
    x +=1 

#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

Inc = max(MntChange)
Dec = min(MntChange)

for x in range(len(MntChange)):
    if MntChange[x] == Inc:
        MaxMnt= (x-1)
    elif MntChange[x] == Dec:
        MinMnt= (x-1) 
    else:
        x += 1

# find month index for the Max Increase and Max Decrease

for i in range(len(MntChange)):
    if MntChange[i] == Inc:
        MaxX = (i - 1)
    elif MntChange[i] == Dec:
        MinX = (i - 1)
    else:
        i += 1
MthMax = ListMnt[MaxX]
MthMin = ListMnt[MinX]     

#The average of the changes in "Profit/Losses" over the entire period

average = str(round(statistics.mean(MntChange), 2))

#Print the analysis to the terminal and export a text file with the results
#Printing output on console

print("Financial Analysis")
print("--------------------------------------------------")
print("Total Months: " + str(Mnt_Ct))
print("Total: $" + str(Total))
print("Average Revenue Change: " +"$"+ str(average))
print("Greatest Increase in Profits: " + str(MthMax) + "  ($" + str(Inc) + ")")
print("Greatest Decrease in Profits: " + str(MthMin) + "  ($" + str(Dec) + ")")

f= open('Financial_Analysis', 'w')
f.write("Financial Analysis")
f.write("--------------------------------------------------")
#
f.write("Total Months: " + str(Mnt_Ct))
f.write("Total: $" + str(Total))
f.write("Average Revenue Change: " +"$"+ str(average))
f.write("Greatest Increase in Profits: " + str(MthMax) + "  ($" + str(Inc) + ")")
f.write("Greatest Decrease in Profits: " + str(MthMin) + "  ($" + str(Dec) + ")")