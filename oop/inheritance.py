# Superclass
class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# Subclass
class Penguin(Bird):
    def __init__(self):
        # Call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()  # Penguin
peggy.swim()       # Swim faster
peggy.run()        # Run faster
