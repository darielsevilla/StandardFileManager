from LinkedList import LinkedList

class Archivo: 
        def __init__(self, nombre):
            self.Name = nombre
            self.Path = None
            self.Campos = LinkedList()
                
        def abrir_archivo(self):
            try:
                with open(self.Path, 'r') as archivo:
                    contenido = archivo.read()
                return contenido
            except FileNotFoundError:
                return "El archivo no se encontró"
            except Exception as e: 
                return f"Error al abrir el archivo: {str(e)}"
            
        def getName(self):
           return self.Name
        
        def getPath(self):
            return self.Path
        
        def getCampos(self):
            return self.Campos
            
        def setName(self, newName):
            self.Name = newName
        
        def setPath(self, newPath):
            self.Path = newPath
            
        def setCampos(self, newList):
            self.Campos = newList