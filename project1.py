#importing the required libraries to stimulate the project
import numpy as np
import random
#Finding whether the dart hits on the circle
def hitting_in_circle(x,y):
    return (x**2+y**2)**0.5 <= 1
#stimulating the dart throw
def dart_throw_stimulation(num_darts):
    hits = 0
    for i in range(num_darts):
        #creating a random number between -1 and 1 along the x-axis since the radius is 1
        x=random.uniform(-1,1)
        # creating a random number between -1 and 1 along the y-axis since the radius is 1
        y=random.uniform(-1,1)
        #finding whether the dart hits on the circle
        if(hitting_in_circle(x,y)):
            hits+=1

    #probability of darts hitting the circle
    prob_hit_cirlcle= hits/num_darts
    return  prob_hit_cirlcle

#number of times the stimulation runs
num_darts=int(input("Enter how many simulations:"))
hitting_the_circle = dart_throw_stimulation(num_darts)

estimate_value_pi= 4*hitting_the_circle

print(f"Estimated value of PI: {estimate_value_pi}")
print (f"The value of PI:{np.pi}")

print(f"The probability of dart hitting the circle: {hitting_the_circle}")
print(f"Number of times the stimulation runs: {num_darts}")