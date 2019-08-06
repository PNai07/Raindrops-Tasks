# Raindrops task Main
# Payal Nayee


class Raindrops():
    def raindrop (n):
        input("Please enter a number of your choice: ")

for n in range(1,120):
        if n % 3 == 0 and n% 5 == 0:
            print("PING")
        elif n % 5 == 0:
            print("PLANG")
        elif n % 7 == 0:
            print ("PLONG")

        else:
            print(n)