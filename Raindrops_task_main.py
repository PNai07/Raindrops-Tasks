# Raindrops task Main
# Payal Nayee


class Raindrops():

    def raindrop (num):
        for num in range(1,120):
            if num % 3 == 0 and num% 5 == 0:
                print("Pling")
            elif num % 5 == 0:
                print("Plang")
            elif num % 7 == 0:
                print ("Plong")

        else:
            print(num)