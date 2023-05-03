class RobotController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            print("")
            print("ACCION ROBOT \n")
            self.vista.mensaje("""Mover ; Detener ; Salir""")
            self.vista.mensaje("Ingrese comando")
            comando=input().lower()
            if comando == "mover":
                self.mover()
            elif comando == "detener":
                print("")
                print("EL ROBOT SE HA DETENIDO")
                print("")
            elif comando == "salir":
                break
            else:
                print("")
                print("COMANDO NO VALIDO!!!")
                print("")
    def mover(self):
        elevacion, rotacion, length = self.vista.get_user_input()
        self.modelo.move_elevation(elevacion)
        self.modelo.move_rotation(rotacion)
        self.modelo.move_length(length)
        self.modelo.movimiento = True
        self.vista.mostrar(self.modelo.elevacion, self.modelo.rotacion, self.modelo.length, self.modelo.movimiento)
