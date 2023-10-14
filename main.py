class HealthUser:
    """
    A class that encapsulates the progress of a user by quantifying the progression of their desired process
    """
    def __init__(self, name: str, age: int, weight: float, exercise: int, diet: int, sleep: int ):
        self.name = name
        self.age = age
        self.weight = 0
        self.exercise = 0
        self.diet = 0
        self.sleep = 0
    
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


p1 = HealthUser("Shoun", 21, 0,0,0,0) 

print(p1 , "weight: " , p1.get_weight())

diet_ans = input("How was your diet? ")
exer_ans = input("How was your exercise? ")

prog_diet = how_diet(diet_ans)
prog_exer = how_exercise(exer_ans)

p1.set_diet(prog_diet)
p1.set_exercise(prog_exer)

print(p1.get_diet())
print(p1.get_exercise())


