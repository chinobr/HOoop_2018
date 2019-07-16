## Tareas

#1. Completar la implementación de los métodos faltantes en las diferentes clases.
#2. Completar el módulo main que realice la simulación de atención a medida que llegan los clientes.
#3. Crear un método que muestre la fila de clientes de cada tipo.
#4. Realizar una visualización de la simulación.


class Fila(object):
    """Clase base de fila"""

    def __init__(self):
         """constructor de la clase Fila """
        self.enfila= 0
        self.fila = []

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        pass

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
    
    def abrircajanueva(self,maxenfila,filanueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        pass
    
    
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        pass

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        pass      

    

class cliente(object):
     """clase cliente """
    def __init__(self,dni):
         """ constructor de la clase cliente """
        self.dni=dni
        self.categoria=None
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        pass
  
    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
    pass
