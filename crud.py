import psycopg2

#conn es una variable que almacena el objeto tipo conexion que tiene psycopg2, necesita varios parametros sobre la base de datos para poder acceder
conn = psycopg2.connect(dbname="postgres", user="openpg", password="openpgpwd")
#cursor es un puntero que ejecuta las sentencias SQL y opera sobre los resultados.
cursor = conn.cursor()
#tanto conn como cursor deben cerrar su conexion
#nosotros hemos usado una funcion para cerrar estas conexiones a la bd

#Funcion Create
def create():
    try:
        cursor.execute("CREATE DATABASE mydatabase") # creamos la base de datos
        cursor.execute("CREATE TABLE alumnos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50), apellido VARCHAR(50))")
        # creamos la tabla y definimos la key
    except:
        finalizarConexion()

#Funcion select
def select():
    try:
        #el metodo execute puede aceptar un parametro (en este caso la sentencia SQL) 
        #pero tambien puede aceptar 2 parametros separados, uno para consultas y otro para valores relacionados con la consulta
        cursor.execute(
            """
            SELECT * FROM alumnos
            """
        )
        result = cursor.fetchall()
        #bucle para imprimir el resultado, ya que fetchall devuelve en forma de lista los resultados
        for row in result:
            print("id = ", row[2])
            print("nombre = ", row[0], )
            print("apellido = ", row[1])
            print("\n")
    except:
        #en caso de error cortamos conexion
        finalizarConexion()

#funcion insert
def insert(a,b):
    try:
        sql = """ INSERT INTO alumnos (nombre, apellido) VALUES (%s,%s)"""
        values = (a, b)
        cursor.execute(sql, values)
        conn.commit()
        select()
    except:
        #tanto el insert como el update alteran la base de datos, si algo sale mal se hace un rollback
        cursor.rollback()
        finalizarConexion()

def updateName(a,b):
    try:
        sql = """ UPDATE alumnos SET nombre=(%s) WHERE id = (%s) """
        values = (a, b)
        cursor.execute(sql, values)
        conn.commit()
        select()
    except:
        cursor.rollback()
        finalizarConexion()

#funcion update apellido ( necesita apellido y la id)
def updateSurname(a,b):
    try:
        sql = """ UPDATE alumnos SET apellido=(%s) WHERE id = (%s) """
        values = (a, b)
        cursor.execute(sql, values)
        conn.commit()
        select()
    except:
        cursor.rollback()
        finalizarConexion()

#Funcio delete
def delete(id):
    try:
        sql = """ DELETE FROM alumnos WHERE id = (%s) """
        value = (id)
        cursor.execute(sql, value)
        conn.commit()
        select()
    except:
        finalizarConexion()
        cursor.rollback()

#funcion para cerrar la conexion
def finalizarConexion():
    cursor.close()
    conn.close()