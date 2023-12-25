#importing required libraries
from itertools import  product

all_outcomes=set() #to store all the unique outcomes of the dice throw
selected_outcomes=set() # to store all the unique outcomes of the dice throw that adds up to 32

count_all= 0 #to count total number of outcomes
count_selected= 0 #to count total number of outcomes that add upto 32

for p in product(range(1,7),repeat=10): #adding all the possible outcomes when throwing the 10 dices into a tupple
    count_all+=1 #counting the number of total outcomes
    sorted_p =tuple(sorted(p)) #sorting the tuple p then converting the sorted list back to a tuple
    all_outcomes.add(sorted_p) #adding the sorted tuples to the all_outcomes set

    if(sum(sorted_p)==32): #checking whether the sum of the sorted tuple is equal to 32
        count_selected+=1 #counting the number of total outcomes that add upto 32
        selected_outcomes.add(sorted_p) #adding the tuples that add up to 32 in to the selected_outcomes set

length_all_outcomes= len(all_outcomes) #finding the number of tupples in the all_outcomes set
length_selected_outcomes= len(selected_outcomes) #finding the number of tupples in the selected_outcomes set

probability= length_selected_outcomes/length_all_outcomes #probability of 10 dice adds up to 32

print(f"Probability of all possible ways of making 32 from 10 dice(not minding the order): {probability}")
#print(f"Probability of all possible ways of making 32 from 10 dice(minding the order):{count_selected/count_all}")
print("\n")
print("The possbile ways of making 32 from 10 dice")

for i in selected_outcomes:
    print(i)