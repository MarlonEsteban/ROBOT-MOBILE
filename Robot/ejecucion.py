from Robot_model import RobotModel
from Robot_view import RobotView
from Robot_controller import RobotController

modelo = RobotModel()
vista = RobotView()
controlador = RobotController(modelo, vista)

controlador.ejecutar()
