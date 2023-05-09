class Robots:
    """ initializing robots """
    # creating class variables

    population = 0
    

    def __init__(self, name):
        self.name = name
        print("initializing {}".format(name))

    def die(self):
        print("{} is distroyed".format(self.name))
    
    def say_hi(self):
        print("greetings my masters call me {}".format(self.name))
