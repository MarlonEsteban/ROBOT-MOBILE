class RobotView:
    def mensaje(self,mens):
        print(mens)
        print("")
    
    def get_user_input(self):
        elevacion = float(input("Ingrese la elevación del robot: "))
        rotacion = float(input("Ingrese el giro del robot en grados: "))
        length = float(input("Ingrese la longitud del robot: "))
        return elevacion, rotacion, length

    def mostrar(self, elevacion, rotacion, length, movimiento):
        print("")
        print(f"La elevación del robot es de : {elevacion}")
        print(f"Teniendo un giro de rotacion de: {rotacion} grados")       
        print(f"Su longitud es de : {length} \n{'El robot se esta moviendo' if movimiento else ''} " )
   
