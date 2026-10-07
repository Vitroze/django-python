class Race:

    def __init__(self, id, name:str, distance:int, location:str, image:str):
        self.title = name
        self.distance = distance
        self.location = location
        self.image = image
        self.id = id

    def __str__(self):
        return f"Course {self.title} - {self.distance} km à {self.location}"