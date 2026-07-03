[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/EukCIKzm)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=24086482)

# Panel de Auditoría de Base de Datos Multi-Motor

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Backend-Python%203.10%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791.svg)](https://www.postgresql.org/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1.svg)](https://www.mysql.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57.svg)](https://www.sqlite.org/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248.svg)](https://www.mongodb.com/)

> **Panel de Auditoría de Base de Datos** es una solución interactiva y multi-usuario que permite el monitoreo en vivo de transacciones y la auditoría detallada de bases de datos relacionales y no relacionales (**PostgreSQL, MySQL, SQLite y MongoDB**). Diseñado con una interfaz web ágil y moderna, incorpora la inyección automatizada de triggers y change streams, la generación de scripts de reversión (rollbacks), almacenamiento de perfiles de conexión seguros y el análisis histórico mediante archivos CSV. Desarrollado como proyecto académico para la Escuela Profesional de Ingeniería de Sistemas de la Universidad Privada de Tacna.

---

## Descripción

Este sistema proporciona una plataforma centralizada para administrar y auditar eventos de bases de datos de diferentes clientes. Construido con **Python** y el framework **Streamlit**, el aplicativo se conecta de forma dinámica a los motores de bases de datos, permitiendo inyectar lógica de auditoría y capturar operaciones de cambio (Insert, Update, Delete) en tiempo real.

### Características Principales

| Módulo / Vista | Descripción |
|:---|:---|
|  **Acceso y Registro (`app.py`)** | Gestión de acceso seguro (SaaS) mediante registro de usuarios, roles (Admin y Cliente) e inicios de sesión almacenados en una base de datos local SQLite (`saas_admin.db`). |
|  **Gestor de Conexión (`pages/3_Conectar_BD.py`)** | Módulo interactivo para conectarse a bases de datos de clientes en PostgreSQL, MySQL, SQLite y MongoDB. Permite guardar perfiles de conexión y automatiza la instalación del núcleo de auditoría (triggers SQL o listeners de Change Stream). |
|  **Monitoreo en Vivo (`pages/1_Monitoreo_Vivo.py`)** | Seguimiento en tiempo real de las operaciones y transacciones de la base de datos conectada. Permite filtrar y visualizar logs con auto-refresco y generar scripts de reversión (rollback). |
|  **Cargador de CSV (`pages/2_Cargador_CSV.py`)** | Importación y análisis interactivo de reportes de auditoría históricos en formato CSV, facilitando búsquedas rápidas con soporte de la librería Pandas. |
|  **Panel de Admin (`pages/4_Panel_Admin.py`)** | Dashboard administrativo que expone estadísticas globales, métricas de inicio de sesión, listado de usuarios y uso de motores de bases de datos. |

---

## Ecosistema e Integraciones

El Panel de Auditoría no es solo una aplicación web aislada, sino el núcleo de un ecosistema distribuido que se integra con diversas herramientas del ciclo de desarrollo:

1. **API REST Pública (BD Auditoría Skill)**: Se ha desacoplado el motor de auditoría en una API independiente alojada en **Railway** (usando *FastAPI*). Esto permite que cualquier sistema externo (bots, CLIs u otras aplicaciones) pueda conectar bases de datos y solicitar logs de auditoría en tiempo real. Documentado mediante OpenAPI.
2. **GitHub Action (Automated DB Rollback)**: Automatización de nivel CI/CD. Si se detecta una anomalía en la base de datos (ej. un `DELETE` erróneo), este Action permite a los desarrolladores introducir el ID del log desde GitHub, conectándose a nuestra API para generar un script de reversión SQL y abrir un Pull Request automáticamente.
3. **Extensión Oficial para VS Code (`bd-auditoria.bd-auditoria`)**: Una extensión publicada en el Marketplace que proporciona acceso instantáneo al panel multi-motor directamente desde el editor. Mediante el comando `BD Auditoria: Abrir Panel`, los desarrolladores pueden conectarse a múltiples motores, subir archivos CSV y revisar la seguridad en vivo sin abandonar su flujo de trabajo.
4. **Sinergia Académica (Validadores)**: Nuestra API de Auditoría se integra de forma directa con los proyectos de otros equipos académicos:
   - **Validador de Sintaxis SQL y NoSQL**: Permite auditar el impacto real de las consultas analizadas por el validador en las tablas de la base de datos.
   - **Validador de Normalización SQL**: Permite rastrear y registrar los cambios estructurales cuando se aplican scripts de normalización sobre esquemas en producción.

---

## Tecnologías Utilizadas

El proyecto define sus dependencias en el archivo `requirements.txt`:

*   **Lenguaje:** Python 3.10+
*   **Framework Web:** `streamlit` (con `streamlit-autorefresh` para monitoreo en vivo)
*   **Manipulación de Datos:** `pandas`
*   **Controladores de Bases de Datos:**
    *   `psycopg2-binary` (PostgreSQL)
    *   `pymysql` (MySQL)
    *   `pymongo` (MongoDB)
    *   `sqlite3` (Integrado en Python para SQLite)

---

## Ejecución del Sistema

El proyecto está diseñado para un despliegue rápido y sencillo utilizando el servidor integrado de Streamlit.

### 1. Instalar dependencias
Asegúrate de tener Python instalado y ejecuta el siguiente comando en la raíz del proyecto para instalar las librerías necesarias:
```bash
pip install -r requirements.txt
```

### 2. Iniciar la aplicación
Ejecuta el archivo principal `app.py` con el motor de Streamlit:
```bash
streamlit run app.py
```

> [!NOTE]
> Al iniciar la aplicación por primera vez, se inicializará la base de datos local `saas_admin.db` y se creará el usuario administrador por defecto:
> - **Usuario:** `admin`
> - **Contraseña:** `admin123`

---

## Estructura del Proyecto

La organización del repositorio separa la lógica principal, las vistas de la interfaz, las bases de datos locales, los scripts de auditoría y la documentación:

```text
proyecto-si783-2026-i-u2-auditoria-bd/
├── 📄 app.py                  # Punto de entrada principal y pantalla de Login/Registro
├── 📄 saas_admin.db           # Base de datos SQLite local para la administración de usuarios y conexiones
├── 📄 requirements.txt        # Dependencias y drivers del proyecto
│
├── 📂 pages/                  # Vistas del dashboard de Streamlit
│   ├── 📄 1_Monitoreo_Vivo.py # Visualización y reversión de transacciones en tiempo real
│   ├── 📄 2_Cargador_CSV.py   # Herramienta de lectura e inspección de reportes CSV históricos
│   ├── 📄 3_Conectar_BD.py    # Configuración de conexiones dinámicas e inyección de auditoría
│   └── 📄 4_Panel_Admin.py    # Panel del administrador con estadísticas y logs de accesos
│
├── 📂 utils/                  # Lógica y funciones de soporte de la aplicación
│   ├── 📄 database.py         # Módulo modular de conexiones multi-motor y lectura de logs
│   ├── 📄 mongo_auditor.py    # Listener de Change Streams para MongoDB
│   └── 📄 crear_sqlite.py     # Script auxiliar para inicializar la base de datos local
│
├── 📂 sql_scripts/            # Núcleos de auditoría de bases de datos
│   ├── 📄 core_auditoria.sql        # Triggers y tablas de logs para PostgreSQL
│   ├── 📄 core_auditoria_mysql.sql  # Triggers de auditoría para MySQL
│   ├── 📄 core_auditoria_sqlite.sql # Triggers de auditoría para SQLite
│   ├── 📄 datos_prueba.sql          # Inserciones y modificaciones de simulación
│   └── 📄 init_db.sql               # Script SQL de inicialización general
│
├── 📂 data/                   # Archivos de prueba para la carga interactiva de CSV
│   ├── 📄 reporte_auditar_prueba.csv
│   └── 📄 reporte_auditar_prueba_2.csv
│
├── 📂 skill_bd_auditoria/     # Documentación y despliegue de la API REST (SaaS Backend)
│   ├── 📄 BD_AUDITORIA_SKILL.md # Documentación técnica de la Skill
│   ├── 📄 openapi.yaml          # Especificación OpenAPI de los endpoints
│   └── 📂 service/              # Código fuente de FastAPI para desplegar en Railway/Render
│
├── 📂 github_action_rollback/ # GitHub Action nativo para Rollbacks Automáticos
│   ├── 📄 action.yml            # Definición del Composite Action (Bash + curl + gh)
│   └── 📄 README.md             # Guía de instalación para otros repositorios
│
├── 📂 docs/                   # Documentación formal del proyecto
│   └── 📄 FD01 a FD06 (Factibilidad, Visión, Requerimientos, Arquitectura, Proyecto Final)
│
└── 📂 media/                  # Recursos de diseño y marcas del proyecto
    └── 🖼️ logo-upt.png        # Logotipo institucional
```

---

## Equipo de Desarrollo

### Integrantes:
- **Colque Quispe, Rodrigo Sídney** (2023077078)
- **Ramos Atahuachi, Fabricio Farid Edmilson** (2023076798)

*   **Docente:** Mag. Patrick Cuadros Quiroga
*   **Curso:** Calidad y Pruebas de Software / Base de Datos II
*   **Institución:** Universidad Privada de Tacna — Facultad de Ingeniería — Escuela Profesional de Ingeniería de Sistemas