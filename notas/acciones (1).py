import notas.nota as modelo 


class Acciones:
    def crear(self, usuario):
        print(f"Ok, {usuario[1]} vamos a crear una nueva nota")    
        titulo = input ("\nIntroduce el título de tu nota: ")
        descripcion =  input ("Ingresa el contenido de tu nota: ")
        
        #Creo o instancio en objeto
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >=1:
            print(f"\nHas guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota  {usuario[1]}")
    
    
    def mostrar(self, usuario):
        print(f"\nOk, {usuario[1]} estas son tus notas: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        
        for mostrar in notas:
            print("\n********************")
            print(mostrar[2])
            print(mostrar[3])
    
    
    def borrar(self, usuario):
        print(f"\n Okey {usuario[1]} vamos a borrar las notas")
        
        titulo = input("Introduce el titulo de la nota a borrar: ")
        
        nota = modelo.Nota(usuario[0], titulo, "")
        eliminar = nota.eliminar()
        
        if eliminar[0] >=1:
            print(f"Hemos eliminado la nota {nota.titulo}")
        else:
            print("No se a borrado la nota")
        
            
        