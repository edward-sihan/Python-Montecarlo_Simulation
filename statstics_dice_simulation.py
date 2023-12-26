import random #importing the required libraries

def dice_throw():
    return [random.randint(1,6) for i in range(10)] # returning a random number from 1 to 6 for 10 times


def simulate_dice_throw():

    num_of_simulation = 500 #total number of simulations
    count_of_32=0 #getting the count of simulations that add upto 32

    for i in range(num_of_simulation):
        dice_throw_outcome=dice_throw()
        if sum(dice_throw_outcome)==32: #checking whether the the sum is equals to 32
            count_of_32+=1 #counting the simulations that add upto 32

    probability = count_of_32/num_of_simulation #calculating the probability of having a sum of 32 for 500 simulations

    print(f"Probability of getting sum of 32 is: {probability} ")

simulate_dice_throw()

print(f"Random numbers of 10 dice: {dice_throw()}") #genereated random numbers from 1 to 6 for 10 dice