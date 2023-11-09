class Material:
    pass

class Texture(Material):
    def __init__(self, image_path):
        self.image_path = image_path
        
class Color(Material):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b