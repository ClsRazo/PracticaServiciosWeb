#!/usr/bin/env python3
"""
Script para iniciar el servidor Flask en producción
"""
import os
import sys
from app import app

if __name__ == '__main__':
    # Configuración para producción
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    print(f"Iniciando servidor en http://{host}:{port}")
    print("Para probar el servicio:")
    print(f"- Swagger UI: http://18.224.56.4:{port}/apidocs/")
    print(f"- Consultar precio: http://18.224.56.4:{port}/libreria/precio?titulo=TITULO_LIBRO")
    print("Presiona Ctrl+C para detener el servidor")
    
    try:
        app.run(host=host, port=port, debug=False)
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        sys.exit(0)
