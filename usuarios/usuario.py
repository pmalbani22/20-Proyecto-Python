import datetime
import hashlib
# llamo al módulo conexion y le pongo un alias conexion
import usuarios.conexion as conexion

# Guardo en la variable connect el método conectar()
connect = conexion.conectar()
# Creo dos variables y guardo los valores que vienen del módulo conexion
database = connect[0]
cursor = connect[1]


class Usuario:
    # Defino el constructor __init__
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar la contraseña
        cifrado = hashlib.sha256()  # utilizo uno de los métodos de encriptación sha256
        # Solo puede tomar datos en bytes no en texto plano por lo que con encode lo transformo
        cifrado.update(self.password.encode("utf8"))

        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"
        # cifrado.hexdigest me guarda en la base el dato en formato en exadecimal
        usuario = (self.nombre, self.apellido,
                   self.email, cifrado.hexdigest(), fecha)

        try:
            # Ejecuto la consulta de sql
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    # Login del usuario
    def identificar(self):
        # Consulta para saber si existe en la base
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Cifrar la contraseña
        cifrado = hashlib.sha256()  # utilizo uno de los métodos de encriptación sha256
        # Solo puede tomar datos en bytes no en texto plano por lo que con encode lo transformo
        cifrado.update(self.password.encode("utf8"))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        # Ejecuto la consulta
        cursor.execute(sql, usuario)

        result = cursor.fetchone()

        return result
