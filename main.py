"""
# Proyecto Python y Mysql
# - Abrir asistente
# - Login o registro  
# - Si elegimos registro, creara un usuario en la bd
# - Si elegimos login, indentifica el usuario
# - Nos preguntará crear nota, mostrar o borrarlas
"""
#from usuarios import acciones
import usuarios.acciones as acciones

 

print("""
      Acciones disponibles:
        - Registro
        - Login
      """)

# Creo el objeto y lo llamo hazEl
hazEl= acciones.Acciones() 

accion = input("Que quieres hacer: ")

if accion == "Registro":
    hazEl.registro()
    
elif accion == "Login":
    hazEl.login()
    
