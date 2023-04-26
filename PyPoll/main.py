# PyPoll Homework

import csv
import os
import pandas as pd
import numpy as np

# import the location of the file
filepath=os.path.join("..","Homework","03-Python","Starter_Code","PyPoll","Resources","budget_data.csv")

# use pandas to read the csv file
election_data = pd.read_csv("election_data.csv")

#Calc the total votes
total_votes = len(election_data["Ballot ID"])

# candidate lists, percentage and counts
name = election_data["Candidate"].unique()

candidate_count = election_data["Candidate"].value_counts()
candidate_percent = election_data["Candidate"].value_counts(normalize=True).map('{:.3%}'.format)

Summary = pd.DataFrame({'Percentage': candidate_percent, 'Counts': candidate_count})
Summary.reset_index(inplace=True)
Summary = Summary.rename(columns = {'index':'Name'})
# print(Summary)

# Charles Casper Stockham

percentage1 = Summary.loc[(Summary["Name"]==name[0]),"Percentage"].item()
Count1 = Summary.loc[(Summary["Name"]==name[0]),"Counts"].item()

percentage2 = Summary.loc[(Summary["Name"]==name[1]),"Percentage"].item()
Count2 = Summary.loc[(Summary["Name"]==name[1]),"Counts"].item()

percentage3 = Summary.loc[(Summary["Name"]==name[2]),"Percentage"].item()
Count3 = Summary.loc[(Summary["Name"]==name[2]),"Counts"].item()


# find out the winner
max = Summary["Counts"].max()
winner = Summary.loc[Summary["Counts"]==max,"Name"].item()


print("Election Results") 
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
print(f'{name[0]}: {percentage1} ({Count1})')
print(f'{name[1]}: {percentage2} ({Count2})')
print(f'{name[2]}: {percentage3} ({Count3})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")