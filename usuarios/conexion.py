import mysql.connector


def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Tate2208",
        database="master_python",
        port=3306
    )

    cursor = database.cursor(buffered=True)

    # La lista que guarda los valores de database y cursor la voy a usar en los otros módulos
    return [database, cursor]
