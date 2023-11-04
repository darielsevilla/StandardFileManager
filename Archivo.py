from LinkedList import LinkedList

class Archivo: 
        def __init__(self, nombre):
            self.Name = nombre
            self.Path = None
            self.Campos = LinkedList()

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
            
        def abrirArchivo(self):
            try:
                with open(self.Path, 'r') as archivo:
                    contenido = archivo.read()
                return contenido
            except FileNotFoundError:
                return "El archivo no se encontró"
            except Exception as e: 
                return f"Error al abrir el archivo: {str(e)}"
        
        def guardarArchivo(self, contenido = None):
            try:
                print(self.Path)
                if(contenido == None):
                    open(self.Path, 'x')
                with open(self.Path, 'w') as archivo:
                    if(contenido != None):
                        archivo.write(contenido)
                return "Archivo guardado exitosamente."
            except Exception as e: 
                return f"Error al guardar el archivo: {str(e)}"


