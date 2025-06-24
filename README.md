# API REST Librería - Deployment en AWS EC2

## 🚀 Servicio Desplegado

**URL del Servicio:** `http://18.224.56.4:5000`

### 📋 Endpoints Disponibles

1. **Swagger UI (Documentación Interactiva):**
   - 🔗 http://18.224.56.4:5000/apidocs/

2. **Consultar Precio de Libro:**
   - 🔗 http://18.224.56.4:5000/libreria/precio?titulo=Cryptography%20Theory%20and%20Practice

3. **Health Check:**
   - 🔗 http://18.224.56.4:5000/health

4. **Información del Servicio:**
   - 🔗 http://18.224.56.4:5000/

### 🧪 Cómo Probar el Servicio

#### Opción 1: Desde el Navegador
- Visita: http://18.224.56.4:5000/apidocs/
- Usa la interfaz Swagger para probar los endpoints

#### Opción 2: Con curl
```bash
# Consultar precio de un libro
curl "http://18.224.56.4:5000/libreria/precio?titulo=Cryptography%20Theory%20and%20Practice"

# Agregar un nuevo libro
curl -X POST "http://18.224.56.4:5000/libreria/libro" \
     -H "Content-Type: application/json" \
     -d '{"titulo": "Nuevo Libro", "precio": 150.0}'

# Health check
curl "http://18.224.56.4:5000/health"
```

#### Opción 3: Con Postman
- Importa la colección desde: http://18.224.56.4:5000/apidocs/
- Usa la base URL: `http://18.224.56.4:5000`

#### Opción 4: Con el Cliente Python
```bash
python cliente.py
```

## 📚 Libros Disponibles Inicialmente

- "Cryptography Theory and Practice" - $250.0
- "Handbook of Applied Cryptography" - $300.0  
- "Cryptography and Network Security" - $180.0

## 🛠️ Comandos de Administración en EC2

### Iniciar el servicio en background:
```bash
./run_service.sh
```

### Detener el servicio:
```bash
./stop_service.sh
```

### Ver logs del servicio:
```bash
tail -f logs/service.log
```

### Verificar estado del servicio:
```bash
curl http://localhost:5000/health
```

## 🔧 Configuración de Seguridad EC2

Asegúrate de que tu Security Group tenga:
- Puerto 5000 abierto para HTTP (0.0.0.0/0)
- Puerto 22 abierto para SSH (tu IP)

## 📝 Notas Técnicas

- El servicio corre en el puerto 5000
- Configurado para aceptar conexiones externas (host='0.0.0.0')
- Los datos se almacenan en memoria (se pierden al reiniciar)
- Incluye documentación Swagger automática
