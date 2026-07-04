---
name: auditoria_bd
description: Administrar, auditar, monitorear y generar scripts de reversión (rollback) para bases de datos relacionales y no relacionales usando la API REST pública de auditoría de BD.
---

# DB Audit & Monitoring Skill

## Objetivo

Permitir la conexión dinámica a diferentes motores de bases de datos, inyectar la lógica de auditoría y consultar los logs de operaciones (Insert, Update, Delete) o generar scripts de rollback.

## Endpoints de la API

La API base es: `https://bd-auditoria-skill-production.up.railway.app`

- `POST /api/v1/connections`: Configura una base de datos y despliega el núcleo de auditoría (triggers).
- `GET /api/v1/logs`: Recupera los registros de auditoría recientes.
- `POST /api/v1/rollback`: Genera un script SQL o comando NoSQL para revertir una transacción específica basada en su log.
- `GET /api/v1/metrics`: Devuelve estadísticas de uso (cantidad de operaciones por motor).

## Ejemplos de uso

### 1. Configurar conexión y auditoría

Usa una petición HTTP POST a `/api/v1/connections` con el siguiente formato JSON:

```json
{
  "engine": "postgresql",
  "connection": {
    "host": "localhost",
    "port": 5432,
    "user": "admin",
    "password": "password",
    "database": "tienda_db"
  }
}
```

*(Motores soportados: `postgresql`, `mysql`, `sqlite`, `mongodb`)*

Si el usuario proporciona una URL de conexión de MongoDB (ej. `mongodb+srv://...`), extrae los parámetros `user`, `password`, `host` (el cluster) y la `database` para armar el JSON de conexión:

```json
{
  "engine": "mongodb",
  "connection": {
    "host": "cluster0.ejemplo.mongodb.net",
    "user": "usuario",
    "password": "password",
    "database": "mi_bd"
  }
}
```

### 2. Consultar logs de auditoría

Usa una petición HTTP GET a `/api/v1/logs`. Parámetros útiles: `engine`, `operation` (DELETE, INSERT, UPDATE), `limit`.

Ejemplo: `/api/v1/logs?engine=postgresql&operation=DELETE&limit=10`

La respuesta tendrá un formato similar a:

```json
{
  "success": true,
  "count": 1,
  "logs": [
    {
      "id": "1001",
      "timestamp": "2026-07-03T10:15:30Z",
      "engine": "postgresql",
      "table": "empleados",
      "operation": "DELETE",
      "old_data": { "id": 5, "nombre": "Juan", "cargo": "Ventas" },
      "new_data": null,
      "user": "app_user"
    }
  ]
}
```

### 3. Generar Script de Rollback

La API proporciona la capacidad de generar un script para revertir operaciones:

```json
{
  "success": true,
  "rollback_script": "INSERT INTO empleados (id, nombre, cargo) VALUES (5, 'Juan', 'Ventas');"
}
```

## Instrucciones para el Agente

Cuando el usuario pida usar esta skill para auditar, monitorear o generar rollbacks o si menciona la skill `auditoria_bd`:
1. Reconoce la necesidad de usar la API desplegada en `https://bd-auditoria-skill-production.up.railway.app`.
2. Escribe el código necesario (p. ej. en Python usando `requests` o scripts en JavaScript) o comandos (como `curl`) para consumir los endpoints.
3. Interpreta la respuesta JSON obtenida y procesa los datos según el caso de uso del usuario (alertas, reportes, scripts de rollback, etc.).
4. Recuerda que no tienes que conectarte tú directamente a la base de datos para la auditoría, sino delegarlo mediante la API REST.
