# Raindrops task Main
# Payal Nayee


class Raindrops():
    def raindrop (n):
        n=input("enter a value: ")

for n in range(1,120):
        if n % 3 == 0 and n% 5 == 0:
            print("Pling")
        elif n % 5 == 0:
            print("Plang")
        elif n % 7 == 0:
            print ("Plong")
        else:
            print(n)