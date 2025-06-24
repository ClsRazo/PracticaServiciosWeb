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

# Intentar obtener la IP pública de diferentes maneras
PUBLIC_IP=""
if command -v curl >/dev/null 2>&1; then
    PUBLIC_IP=$(curl -s --connect-timeout 5 http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null)
fi

if [ -z "$PUBLIC_IP" ]; then
    PUBLIC_IP=$(wget -qO- --timeout=5 http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null)
fi

if [ -z "$PUBLIC_IP" ]; then
    PUBLIC_IP="18.224.56.4"  # IP por defecto basada en tu configuración
    echo "⚠️  No se pudo obtener IP automáticamente, usando IP configurada"
fi

echo "IP de la instancia: $PUBLIC_IP"
echo "Puerto: 5000"
echo ""
echo "Enlaces para probar:"
echo "- Swagger UI: http://$PUBLIC_IP:5000/apidocs/"
echo "- API Health: http://$PUBLIC_IP:5000/libreria/precio?titulo=Cryptography%20Theory%20and%20Practice"
echo ""
echo "Para ver logs: tail -f logs/service.log"
echo "Para detener: ./stop_service.sh"
