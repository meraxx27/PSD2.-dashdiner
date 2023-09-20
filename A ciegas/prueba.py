import pyodbc
import MySQLdb
import mysql.connector
from flask import Flask, app, jsonify
import mysql.connector

# Configura la cadena de conexión
server = 'localhost'
database = 'dashdiner'
username = 'root'
password = 'Themeraxx'


try:
    # Intenta establecer la conexión
    conn = mysql.connector.connect(
        host=server,
        database=database,
        user=username,
        password=password
    )
    # Utiliza un cursor de diccionario para obtener resultados como diccionarios.
    cursor = conn.cursor(dictionary=True)

    # Si la conexión se establece con éxito, imprime un mensaje
    if conn.is_connected():
        print("Conexión exitosa a MySQL en localhost")

    # Cierra la conexión

except mysql.connector.Error as e:
    # Si ocurre algún error, imprime un mensaje de error
    print(f"Error al conectar a MySQL: {str(e)}")


@app.route('/restaurante/<int:restaurante_id>', methods=['GET'])
def obtener_elemento(restaurante_id):
    query = "SELECT * FROM restaurante WHERE id = %s"
    cursor.execute(query, (restaurante_id,))
    elemento_encontrado = cursor.fetchone()

    if elemento_encontrado:
        print("restaurante encontrado")
        return jsonify(elemento_encontrado)
    else:
        print("restaurante no encontrado")
        return jsonify({"mensaje": "Elemento no encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
