

class Elf:
    def __init__(self, elfdata) -> None:
        self.calories = [int(cal) for cal in elfdata.split('\n')]


    @property
    def total_calories(self): 
        return sum(self.calories)

    @property
    def show_calories(self):
        return self.calories