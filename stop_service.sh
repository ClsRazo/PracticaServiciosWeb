#!/bin/bash

# Script para detener el servicio Flask

echo "Deteniendo servicio de librería..."

if [ -f logs/service.pid ]; then
    PID=$(cat logs/service.pid)
    if ps -p $PID > /dev/null; then
        kill $PID
        echo "Servicio detenido (PID: $PID)"
        rm logs/service.pid
    else
        echo "El proceso ya no existe"
        rm logs/service.pid
    fi
else
    echo "No se encontró archivo PID, intentando matar por puerto..."
    sudo fuser -k 5000/tcp 2>/dev/null || echo "No hay procesos en el puerto 5000"
fi

echo "Servicio detenido."
