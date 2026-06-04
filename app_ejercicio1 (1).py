from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    # 1. Recibir los datos en formato JSON
    datos = request.get_json()

    # 2. Extraer el nombre y las calificaciones
    nombre = datos['nombre']
    calificaciones = datos['calificaciones']

    # 3. Calcular el promedio
    promedio = sum(calificaciones) / len(calificaciones)

    # 4. Redondear a 2 decimales (opcional pero recomendado)
    promedio = round(promedio, 2)

    # 5. Construir y devolver la respuesta
    respuesta = {
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": promedio
    }

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)