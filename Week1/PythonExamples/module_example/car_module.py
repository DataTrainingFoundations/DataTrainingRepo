class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print(f"I'm going {self.speed} kph!")

    def accelerate(self):
        self.speed += 5
    
    def brake(self):
        if self.speed<5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    