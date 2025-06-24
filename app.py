from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

#Diccionario que sirve como base de datos
libros = {
    "Cryptography Theory and Practice": 250.0,
    "Handbook of Applied Cryptography": 300.0,
    "Cryptography and Network Security": 180.0
}

@app.route('/libreria/precio', methods=['GET'])
def consultar_precio():
    """
    Consultar el precio de un libro
    ---
    parameters:
      - name: titulo
        in: query
        type: string
        required: true
        description: Título del libro
    responses:
      200:
        description: Precio del libro
        schema:
          type: object
          properties:
            titulo:
              type: string
            precio:
              type: number
    """
    titulo = request.args.get('titulo')
    precio = libros.get(titulo, -1)
    return jsonify({"titulo": titulo, "precio": precio})

@app.route('/libreria/libro', methods=['POST'])
def agregar_libro():
    """
    Agregar un nuevo libro
    ---
    parameters:
      - name: libro
        in: body
        required: true
        schema:
          type: object
          required:
            - titulo
            - precio
          properties:
            titulo:
              type: string
              description: Título del libro
            precio:
              type: number
              description: Precio del libro
    responses:
      201:
        description: Libro agregado correctamente
        schema:
          type: object
          properties:
            mensaje:
              type: string
            libro:
              type: object
              properties:
                titulo:
                  type: string
                precio:
                  type: number
      400:
        description: Datos inválidos
    """
    datos = request.get_json()
    if not datos or 'titulo' not in datos or 'precio' not in datos:
        return jsonify({"error": "Se requiere título y precio"}), 400
    
    titulo = datos['titulo']
    precio = float(datos['precio'])
    
    # Agregar el libro al diccionario
    libros[titulo] = precio
    
    return jsonify({
        "mensaje": "Libro agregado correctamente",
        "libro": {"titulo": titulo, "precio": precio}
    }), 201

@app.route('/', methods=['GET'])
def home():
    """
    Página de inicio del servicio
    ---
    responses:
      200:
        description: Información del servicio
        schema:
          type: object
          properties:
            servicio:
              type: string
            version:
              type: string
            endpoints:
              type: array
              items:
                type: string
    """
    return jsonify({
        "servicio": "API REST Librería",
        "version": "1.0",
        "swagger": "/apidocs/",
        "endpoints": [
            "GET /libreria/precio?titulo=<titulo>",
            "POST /libreria/libro"
        ],
        "ejemplo": {
            "consultar_precio": "/libreria/precio?titulo=Cryptography Theory and Practice",
            "swagger_ui": "/apidocs/"
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check del servicio
    ---
    responses:
      200:
        description: Estado del servicio
        schema:
          type: object
          properties:
            status:
              type: string
            libros_disponibles:
              type: integer
    """
    return jsonify({
        "status": "OK",
        "libros_disponibles": len(libros)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
