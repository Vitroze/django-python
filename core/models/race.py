class Race:

    def __init__(self, name, distance, location, image):
        self.title = name
        self.distance = distance
        self.location = location
        self.image = image

    def __str__(self):
        return f"Course {self.title} - {self.distance} km à {self.location}"