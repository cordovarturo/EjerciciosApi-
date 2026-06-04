from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()

    # Validaciones básicas
    if not datos:
        return jsonify({"error": "No se enviaron datos"}), 400

    if 'valor' not in datos or 'escala' not in datos:
        return jsonify({"error": "Faltan campos: 'valor' y 'escala' son requeridos"}), 400

    valor = datos['valor']
    escala = datos['escala'].upper()

    if escala == 'CELSIUS':
        resultado = (valor * 9 / 5) + 32
        escala_destino = 'Fahrenheit'
        escala_origen = 'Celsius'

    elif escala == 'FAHRENHEIT':
        resultado = (valor - 32) * 5 / 9
        escala_destino = 'Celsius'
        escala_origen = 'Fahrenheit'

    else:
        return jsonify({"error": "Escala no válida. Use 'Celsius' o 'Fahrenheit'"}), 400

    respuesta = {
        "valor_original": valor,
        "escala_origen": escala_origen,
        "valor_convertido": round(resultado, 2),
        "escala_destino": escala_destino
    }

    return jsonify(respuesta), 200


if __name__ == '__main__':
    app.run(debug=True)
