# Importo el mòdulo usuario que está dentro de la carpeta usuarios y le coloco un alias para que sea más facil manejarlo
import usuarios.usuario as modelo
import notas.acciones 

class Acciones:
    def registro(self):
        print("\nOk, vamos a registrarte en el sistema...")
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu password: ")
        
        # Creo el objeto 
        usuario = modelo.Usuario(nombre, apellido, email, password)
        # Llamo al método registrar del módulo usuario.py
        registro = usuario.registrar()
        
        #Compruebo si se grabó
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")
            
    
    def login(self):
        print("Indentificate en el sistema...")
        
        try: 
            email = input("Ingresa tu email: ")
            password = input("Ingresa tu password: ")
            
            usuario = modelo.Usuario("","",email, password)
            login = usuario.identificar()
            
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en la fecha {login[5]} ")
                self.proximasAcciones(login)
                
        except Exception as e:
            #print(type(e))  
            #print(type(e).__name__)
            print("\nLogin incorrecto")  
    
        
    #Una vez logueado llamo al método próximas acciones
    def proximasAcciones(self, usuario):
        print("""
              Acciones disponibles:
              - Crear notas (crear)
              - Mostrar notas (mostrar)
              - Elimininar notas (eliminar)
              - Salir (salir)
              """)
        accion = input("Que quieres hacer?: ")
        
        #Creo el objeto
        hazEl = notas.acciones.Acciones()
        
        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "salir":
            print(f"Ok, {usuario[1]} hasta pronto!!")
            exit() #función de python para salir del programa
        