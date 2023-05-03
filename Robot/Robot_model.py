class RobotModel:
    def __init__(self):
        self.elevacion = 0
        self.rotacion = 0
        self.length = 0
        self.movimiento = False

    def move_elevation(self, valor):
        self.elevacion += valor

    def move_rotation(self, valor):
        self.rotacion += valor

    def move_length(self, valor):
        self.length += valor

    def stop_movement(self):
        self.movimiento = False
