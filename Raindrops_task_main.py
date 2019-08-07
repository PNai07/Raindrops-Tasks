# Raindrops task Main
# Payal Nayee

class Raindrops():
    def raindrop(self):
        # created a class and defining raindrop
        return
n = int(input("Please enter a value: "))
 # this asks for a user input
# Used if statement expressing the conditions of the program.
if n % 3 == 0:
        if (n % 3 == 0 and n % 5 == 0):
            print("PlingPlang")
        else:
            print("Pling")
elif n % 5 == 0:
        print("Plang")

elif n % 7 == 0:
        print ("Plong")
elif (n % 3 != 0) | (n % 5 != 0) | (n % 7 != 0):
        print(n)
    # this statement says if an integer is not divisible by these numbers, should return the integer value.
