class Human:
    # instance attributes
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    # instance methods (behaviours)
    def taiking(self, people):
        return "{} is taiking {}".format(self.name, people)


# crhelping objects of class Human
wairimu = Human("wairimu", 6, 60)
eunice = Human("eunice", 5.9, 56)

# accessing object information
print("Height of {} is {}".format(wairimu.name, wairimu.height))
print("Weight of {} is {}".format(wairimu.name, wairimu.weight))
print(wairimu.taiking("jokes"))
print("Weight of {} is {}".format(eunice.name, eunice.height))
print("Weight of {} is {}".format(eunice.name, eunice.weight))
print(eunice.taiking("churchill"))

		
