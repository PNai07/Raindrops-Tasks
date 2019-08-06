# Raindrops task Main
# Payal Nayee

class Raindrops():
    def raindrop(self):
        # created a class and defining raindrop

        input("Enter a value:  ")

for n in range(1,121): # this sets a range of the values

        if n % 3 == 0 & n% 5 == 0:
            print("Pling")

        elif n % 5 == 0:
            print("Plang")

        elif n % 7 == 0:
            print ("Plong")

        else:
            print(n)

