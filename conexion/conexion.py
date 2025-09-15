# conexion directa sin sqlalchemy

import mysql.connector

#conexion 
def conexion():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistema_ventas'
    )
# CERRAR CONEXION 
def cerrar_conexion(conn):
    if conn.is_connected():
        conn.close()
        print("conexion cerrada")
