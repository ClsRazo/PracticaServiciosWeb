#!/bin/bash

# Script para ejecutar el servicio Flask en background
# Para usar: ./run_service.sh

echo "Iniciando servicio de librería..."

# Matar cualquier proceso previo en el puerto 5000
sudo fuser -k 5000/tcp 2>/dev/null || true

# Crear directorio de logs si no existe
mkdir -p logs

# Ejecutar el servicio en background
nohup python3 app.py > logs/service.log 2>&1 &

# Obtener el PID del proceso
PID=$!
echo $PID > logs/service.pid

echo "Servicio iniciado con PID: $PID"
echo "IP de la instancia: $(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)"
echo "Puerto: 5000"
echo ""
echo "Enlaces para probar:"
echo "- Swagger UI: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4):5000/apidocs/"
echo "- API Health: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4):5000/libreria/precio?titulo=Cryptography%20Theory%20and%20Practice"
echo ""
echo "Para ver logs: tail -f logs/service.log"
echo "Para detener: ./stop_service.sh"
