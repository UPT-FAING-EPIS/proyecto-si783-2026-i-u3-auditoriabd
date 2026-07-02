---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #ffffff
---

#  AuditDB
**Sistema Avanzado de Auditoría de Bases de Datos**

---

##  ¿Qué es AuditDB?

Es una herramienta diseñada para inyectar capacidades de auditoría de forma automática en bases de datos existentes sin modificar tu código fuente.

- **Automático:** Genera e inyecta triggers en las tablas que elijas.
- **Transparente:** No afecta tu aplicación principal.
- **Centralizado:** Todos los logs van a una tabla o colección unificada (`AUDITORIA_LOGS`).

---

##  Motores Soportados

AuditDB es multi-motor y soporta los sistemas más populares:

1. **🐘 PostgreSQL** (Triggers + Funciones)
2. **🐬 MySQL** (Triggers nativos con JSON)
3. **🗂️ SQLite** (Triggers locales)
4. **🍃 MongoDB** (Change Streams)

---

##  Calidad y Seguridad (CI/CD)

El proyecto cuenta con un riguroso pipeline de integración continua:

- **SonarCloud:** Análisis de deuda técnica y _code smells_.
- **Semgrep:** Análisis estático de código para evitar inyecciones SQL.
- **Snyk:** Detección de vulnerabilidades en dependencias.
- **Pytest & Behave:** Pruebas unitarias, de integración, interfaz y BDD.

---

##  Arquitectura

- **Frontend:** Streamlit (Panel de administración y monitoreo en vivo)
- **Backend:** Python (Controladores de conexión y scripts SQL generativos)
- **Despliegue:** Dockerizable y preparado para la nube.

---

# ¡Gracias! 

