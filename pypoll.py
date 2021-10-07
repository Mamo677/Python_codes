# ##############################################################################3
# 1. Open the data file.
# 2.Write down the names of all the candidates.
# 3.Add a vote count for each candidate.
# 4.Get the total votes for each candidate.
# 5.Get the total votes cast for the election.


import datetime as  dt
from typing import cast
# Use the now() attribute on the datetime class to get the present time.
now=dt.datetime.now()
# Print the present time.
print("the time rigth now is, now")
#Launch the Python interpreter.
#Type 
import csv
import os
# ## 1.A Python module, like the csv module. The dir() function will return all the functions available in the csv module.  
# dir()
# csv()
# #A2 variable, like a dictionary {'key':'value'}, for example the counties_dict dictionary. The dir() function will return all the functions available on that variable
# {  'key':'value'}
# dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})

# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', 
# '__len__', '__lt__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# '__setitem__', '__sizeof__', '__str__', 
# '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 
# 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# #3 A data type, like str. The dir() function will return all 
# #the attributes and methods that can be used with the str data type.
# #str
# #dir()
# #str
# dir(str) ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', 
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 
# 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 
# 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
# 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Assign a variable for the file to load and the path.
file_to_load=os.path.join("Resource", "election_results.csv")
print(file_to_load)
    
 # Print the file object.print(election_data)
 # Create a filename variable to a direct or indirect path to the file.
file_to_save=os.path.join("analysis", "election_analysis.txt")  
print(file_to_save)
#inttialize total voter counter
total_votes=0

#candidate options
candidate_options=[]
# 1. Declare the empty dictionary.
candidate_votes={}
# Track the winning candidate, vote count, and percentage.
winning_Candidate = ""
winning_count  = 0
winning_percentage = 0
# Using the open() function with the "w" mode we will write data to the file
#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    #read the header row
    headers=next(file_reader)
    #print  each row in csv file
    for row in file_reader:
        #print (row)
        #add the total vote count
        total_votes +=1
        #print(total_votes)
         # get the candidate name from each row.
        Candidate_name=row[2]
        if Candidate_name not in candidate_options:
           # Add the candidate name to the candidate list.
           candidate_options.append(Candidate_name)
           #print(candidate_options)
           #candidate_options)
           #Begin tracking that candidate's vote count.

           candidate_votes[Candidate_name]=0
        #print(candidate_votes)  
        # add a vote to that candidate's count()
        candidate_votes[Candidate_name]+=1
# Save the results to our text file.
with open(file_to_save,"w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results =(
        f"\nelection results\n"
        f"-------------\n"
        f"total votes:{total_votes:,}\n"
        f"----------\n")
  
    print(election_results,end="")
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
     votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(candidate_results) 
    #  Save the candidate results to our text file. 
    txt_file.write(candidate_results) 
    print (candidate_votes)
    #check code
    # for Candidate_name in candidate_votes:
    #   votes=candidate_votes[Candidate_name]
    #   votes_percentage=float(votes)/float(total_votes)*100
    # #Print each candidate, their voter count, and percentage to the
# print(f"{Candidate_name}:{votes_percentage:if}%({votes:})\n")
# #Determine winning vote count, winning percentage, and candidate.
# 
    if(votes>winning_count)and (vote_percentage > winning_percentage):
        winning_count= votes
        winning_Candidate=Candidate_name
        winning_percentage=vote_percentage

    winning_Candidate_summary= (
        f"--------------\n"
        f"winner:{winning_Candidate}\n"
        f"winning vote count:{winning_count:,}\n"
        f"winning percentage:{winning_percentage:.1f}%\n"
        f"--------------\n")
    print(winning_Candidate_summary)
    txt_file.write(winning_Candidate_summary)
# candidate_options =[]
# candidate_votes={}
# candidate_votes[Candidate_name]+=1  
# # # 1. Iterate through the candidate list.
# # #for Candidate_name in candidate_votes:
# #  # 2. Retrieve vote count of a candidate
# votes=candidate_votes[Candidate_name]

# # votes_percentage=float(votes)/float(total_votes)*100
# print(f" {Candidate_name}):recevied{votes_percentage}% of the vote.")

#my code
################################################################################################################################### Add our dependencies.
