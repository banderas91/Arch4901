from transform import Transform

class Camera(Transform):
    def __init__(self):
        self.fov = 60
        self.position = (0, 0, 0)