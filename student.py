class Student:
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
    def __str__(self):
        return f"{self.name} | Age: {self.age} | Score: {self.score}"
