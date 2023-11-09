from vehicle import Vehicle

class Bus(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.6
