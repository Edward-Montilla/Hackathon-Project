"""
A demo for the app: JustCareTrakr
"""

class HealthUser:
    """
    A class that encapsulates the progress of a user by quantifying the progression of their desired process
    """
    def __init__(self, name: str, age: int, weight: float, exercise: int, diet: int, sleep: int):
        self.name = name
        self.age = age
        self.weight = weight # percentage of their target weight
        self.exercise = exercise # percentage of their target exercise habit
        self.diet = diet # percentage of their target diet habit
        self.sleep = sleep # percentage of their target sleep habit
    
    def __str__(self):
        return f'{self.name}({self.age})'
    
    def set_weight(self, value: int):
        self.weight = value
    
    def get_weight(self) -> int:
        return self.weight
    
    def set_exercise(self, value: int):
        self.exercise = value
        
    def get_exercise(self) -> int:
        return self.exercise
    
    def set_diet(self, value: int):
        self.diet = value
    
    def get_diet(self) -> int:
        return self.diet
    
    def set_sleep(self, value: int):
        self.sleep = value
        
    def get_sleep(self) -> int:
        return self.sleep

class d

def how_diet(response: str) -> int: # Place holder for a language model like GPT 4
    points = 0
    if response == "great":
        points = 5
    elif response == "good":
        points = 3
    elif response == "bad":
        points = 2
    elif response == "terrible":
        points = 1
    else:
        points = -1    
    return points

def how_exercise(response: str) -> int: # Place holder function for a language model to discern the users feelings towards their progress
    points = 0
    if response == "great":
        points = 5
    elif response == "good":
        points = 3
    elif response == "bad":
        points = 2
    elif response == "terrible":
        points = 1
    else:
        points = -1    
    return points

p0 = HealthUser("Shoun", 20, 100, 0, 0, 0)          # registered a user for a complete lifstyle change
p1 = HealthUser("Edward", 23, 100, 10, 0, 10)       # registered a user to transition to a better diet
p2 = HealthUser("Diego", 24, 100, 5, 10, 10)        # registered a user for a change in exercise process
p3 = HealthUser("Ethan", 21, 120, 10, 10, 10)       # registered a user for a slight increase in over all lifestyle to lose weight

# day 0 *users that have registered at different times are to be accounted for in the production version

print(p0 , "weight: " , p0.get_weight())
print(p1 , "weight: " , p1.get_weight())
print(p2 , "weight: " , p2.get_weight())
print(p3 , "weight: " , p3.get_weight())

# day 1
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 2
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 3
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 4
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 5
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 6
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 7
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 8
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 9
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 10
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 11
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 12
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 13
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 14
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 15
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 16
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 17
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 18
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)

# day 19
p0.set_diet(2)
p0.set_exercise(2)
p0.set_sleep(3)

p1.set_diet(2)
p1.set_exercise(2)
p1.set_sleep(3)

p2.set_diet(2)
p2.set_exercise(2)
p2.set_sleep(3)
             
p3.set_diet(2)
p3.set_exercise(2)
p3.set_sleep(3)






