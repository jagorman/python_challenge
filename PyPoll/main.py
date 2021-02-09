import os #importing operating system module
import csv #importing csv module
import statistics

#Variables
cands= []
num_votes =0
vote_co = []
Poll_Data = ['1','2']

Poll_Data= os.path.join("resources/election_data.csv")
with open(Poll_Data, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    header= next(reader)  

    for line in reader:
        #The total number of votes cast
        num_votes += 1 
        #A complete list of candidates who received votes, and total number of votes each candidate won
        candidate= line[2]
        if candidate in cands:
            cand_index= cands.index(candidate)
            vote_co[cand_index]= vote_co[cand_index]+1
        else:   
            cands.append(candidate)
            vote_co.append(1)
        #The percentage of votes each candidate won