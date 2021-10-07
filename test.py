type(72.61)

thislist = ["apple", "banana", "cherry"]
thislist.append("ornage")
thislist.insert(2,"mango")
print(thislist)
print (len(thislist))
 # declared, type counties 
Counties=["Arapahoe","Denver","Jeferson"]
print (Counties)
#To get the first item in the counties list, type the 
# following in the command line:
# Negative indexes 
print(Counties[2])
print(Counties[-1])
#Find the Length of a List
print(len(Counties))

## Slice Lists
print(Counties[:2])
print(Counties[1:])

#Add Items to a List
#formula append()
#Counties.append("El Paso")
#print (Counties)
Counties.append("El paso")
Counties.insert (2,"El Paso")
print(Counties)
#To remove
Counties.pop(0)
print(Counties)

##Change an Element in a List
    #Counties(2)="EL Paso"
Counties[2]="El paso"
print(Counties)

## Tuples  cannot be changed(immutable:) no add or remove
my_tuple =()
counties_tuple = ("Arapahoe","Denver","jeferson")

print(counties_tuple)
len(counties_tuple)
print (len(counties_tuple))
#counties_tuple[1]
print(counties_tuple[1])
## create dictionary
#my_dictionary={}
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["denver"]=463353
counties_dict["jeferson"]=432438
print(counties_dict)
print
counties_dict["Arapahoe"]=422829
counties_dict["denver"]=463353
counties_dict["jeferson"]=432438
print(counties_dict)# to print all

#Get a Specific Value
##we use get()
counties_dict.get("denver")

print(counties_dict.get("denver"))
voting_data=[]
voting_data.append({"county":"Arapahoe","registerd_Voters":422819})
voting_data.append({"county":"denver","registerd_Voters":463353})
voting_data.append({"county":"jeferson","registerd_Voters":432438})
voting_data.append({"county":"El Paso","registerd_Voters":461149})
print(voting_data)
#voting_data.remove({"county":"Arapahoe","registerd_Voters":422819})
# voting_data.pop(0)
# print(voting_data)
# voting_data [2]= "denver"
# print(voting_data)


  #decision statement two kins of decison statement

  #if
   # what is the differnce between else and elif


                # What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')



#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
   # print("El Paso is not the list of counties.")


  #if else
 # If len(Counties)>2:

  #The if-else statement is used when we need an outcome for both true and false conditions.
# counties = ("Arapahoe","Denver","Jefferson")
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

#   for county in counties:
#     print(county)

#     numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)
#F-strings: Formatted String Literals
#original code

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
## f string code
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(my_votes(f"I received {my_votes / total_votes * 100}% of the total votes."))

# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")