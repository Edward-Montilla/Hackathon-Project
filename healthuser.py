class HealthUser:
    """
    A class that encapsulates the progress of a user by quantifying the progression of their desired process
    """

    def __init__(self, name: str, age: int, weight: float, exercise: int, diet: int, sleep: int):
        self.name = name
        self.age = age
        self.weight = weight  # percentage of their target weight
        self.exercise = exercise  # percentage of their target exercise habit
        self.diet = diet  # percentage of their target diet habit
        self.sleep = sleep  # percentage of their target sleep habit

    def __str__(self):
        return f'{self.name}({self.age})'

    def set_weight(self, value: int):
        self.weight = value

    def get_weight(self) -> int:
        return self.weight

    def set_exercise(self, value: int):
        self.exercise += value

    def get_exercise(self) -> int:
        return self.exercise

    def set_diet(self, value: int):
        self.diet += value

    def get_diet(self) -> int:
        return self.diet

    def set_sleep(self, value: int):
        self.sleep += value

    def get_sleep(self) -> int:
        return self.sleep