# Presentación: Sistema de Auditoría de Bases de Datos

Bienvenidos a la presentación oficial del proyecto **bd-auditoria**. A continuación, se detallan las características principales, el modelo de despliegue de nuestras integraciones y la interoperabilidad con otros sistemas de la clase mediante APIs.

````carousel
# 🛡️ Sistema de Auditoría y Documentación
> [!NOTE]
> Una plataforma centralizada para administrar y auditar eventos de bases de datos de diferentes clientes, contando con su **Documentación oficial y completa alojada en Github**.

**Características Principales:**
- **Acceso y Registro (SaaS):** Gestión segura de usuarios y roles.
- **Gestor de Conexión:** Conexión a PostgreSQL, MySQL, SQLite y MongoDB para instalar el núcleo de auditoría.
- **Monitoreo en Vivo:** Seguimiento de operaciones (Insert, Update, Delete) en tiempo real con capacidad de rollback.
- **Cargador de CSV:** Análisis de reportes históricos de auditoría.
- **Documentación Completa:** Todo el código fuente, la guía de despliegue, guías de integración y los flujos se encuentran versionados y bien explicados en el repositorio de Github.

<!-- slide -->
# ⚙️ Integración 1: Skill Publicada

La funcionalidad core ha sido paquetizada y distribuida a través de una **Agent Skill**. Esto permite a otros asistentes automatizados consumir las herramientas de auditoría fácilmente.

> [!TIP]
> Puedes revisar la documentación técnica de nuestra skill en el repositorio: [SKILL.md](file:///c:/PY_BDII_CALIDAD/bd-auditoria-test/.agents/skills/bd-auditoria/SKILL.md)

**Capacidades de la Skill:**
- Conexión dinámica a bases de datos relacionales y NoSQL.
- Inyección de Triggers de auditoría.
- Extracción de métricas de uso y operaciones.

<!-- slide -->
# 🧩 Integración 2: Extensión de VS Code

Para facilitar aún más el trabajo de los desarrolladores y DBAs que consumen nuestros servicios, hemos publicado una extensión oficial para VS Code.

> [!IMPORTANT]
> La extensión oficial ya se encuentra publicada y disponible para su uso directo dentro del editor.

![VS Code Extension](C:/Users/Mi Equipo/.gemini/antigravity-ide/brain/1d53716c-f38b-40ba-ac21-f238ca03938d/extension.png)

<!-- slide -->
# 🔌 Integraciones 3: Interoperabilidad con APIs

Para garantizar que las bases de datos auditadas cumplan con los más altos estándares de calidad, **hemos integrado nuestro sistema con las APIs desarrolladas por otros grupos**:

> [!NOTE]
> La comunicación entre los proyectos se realiza de forma limpia mediante servicios REST (APIs), enriqueciendo las capacidades de nuestro sistema base.

1. **Validador de Sintaxis (API):**
   - **Desarrollado por:** Gian Franco Arocutipa y Cristian Soto.
   - **Uso Integrado:** Validación de las consultas SQL, reglas y scripts generados antes de inyectar triggers o ejecutar operaciones de rollback en la auditoría.

2. **Validador de Normalización (API):**
   - **Desarrollado por:** Fabrizio Perez y Manuel Dongo.
   - **Uso Integrado:** Análisis del esquema de las bases de datos que son conectadas a nuestro sistema para asegurar que cumplen con las formas normales (1NF, 2NF, 3NF) antes de ser auditadas.
````
