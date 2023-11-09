
class Scene:
    def __init__(self):
        self.models = []
        self.camera = None 

    def add_model(self, model):
        self.models.append(model)

    def set_camera(self, camera):
        self.camera = camera

   
