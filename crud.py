import psycopg2

conn = psycopg2.connect(dbname="postgres", user="openpg", password="openpgpwd")
cursor = conn.cursor()


def select():
    cursor.execute(
        """
        SELECT * FROM alumnos
        """
    )
    result = cursor.fetchall()
    for row in result:
        print("id = ", row[2])
        print("nombre = ", row[0], )
        print("apellido = ", row[1])
        print("\n")



def insert(a,b):
    sql = """ INSERT INTO alumnos (nombre, apellido) VALUES (%s,%s)"""
    values = (a, b)
    cursor.execute(sql, values)
    conn.commit()
    select()

def update(a,b):
    sql = """ consulta """
    values = (a, b)
    cursor.execute(sql, values)
    conn.commit()
    select()

def finalizarConexion():
    cursor.close()
    conn.close()