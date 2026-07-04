---
marp: true
theme: default
class: invert
paginate: true
backgroundColor: #0d1117
color: #c9d1d9
---

#  Sistema de Auditoría de Bases de Datos
**Ecosistema, Documentación e Integraciones**

---

#  Documentación Oficial en GitHub

Todo nuestro proyecto no es solo código; es un **ecosistema documentado**.

- **Centralización:** Un único repositorio como fuente de la verdad.
- **Transparencia:** Código fuente, guías de despliegue y manuales de integración disponibles y versionados.
- **OpenAPI / Swagger:** Documentación interactiva de nuestra API para que otros equipos puedan consumirla sin fricciones.

---

#  El Ecosistema de Integraciones

Nuestro Panel Web (Streamlit) es solo el núcleo. Hemos extendido nuestras herramientas para integrarnos en el flujo de trabajo real de los desarrolladores:

1. **Skill / API REST Pública** (Desplegada en la nube)
2. **Extensión Oficial para VS Code** (Publicada en el Marketplace)
3. **GitHub Action** (Automatización CI/CD para Rollbacks)

---

#  Integración 1: Skill (API REST)

Hemos extraído la lógica de conexión y auditoría en una API independiente alojada en **Railway** usando *FastAPI*.

- **Interoperabilidad:** Permite que agentes automatizados o aplicaciones de otros grupos se conecten a nuestra lógica.
- **Endpoints Clave:** `/api/v1/connections`, `/api/v1/logs`, `/api/v1/rollback`.
- **Despliegue 24/7:** Totalmente pública, escalable y documentada.

---

#  Integración 2: Extensión de VS Code

Para facilitar el trabajo de los DBAs, publicamos una **Extensión en el Marketplace de VS Code**.

- **Acceso Directo:** Comando `BD Auditoria: Abrir Panel`.
- **Flujo Ininterrumpido:** Permite revisar la seguridad, ver logs y auditar bases de datos (Postgres, Mongo, MySQL, SQLite) sin salir del editor de código.
- **Integración Nativa:** Se acopla perfectamente al entorno de desarrollo diario.

---

#  Integración 3: GitHub Action de Rollback

**Automatización de Desastres en Tiempo Real.**

- Si un usuario (o alguien de otro grupo) comete un error grave (ej. un `DELETE` accidental), no necesita escribir código para arreglarlo.
- **El Flujo:** Ejecutan nuestro Action en GitHub -> ingresan el `log_id` -> el Action consume nuestra API en Railway.
- **La Magia:** Nuestra API genera el SQL inverso (`INSERT`, `UPDATE`) y el Action **crea un Pull Request automáticamente** en su repositorio.

---

#  Sinergia con otros Proyectos (Validadores)

Nuestra API de Auditoría es el puente perfecto para el resto del aula:

- **Validador de Sintaxis SQL y NoSQL:** Pueden enviarnos las consultas que ellos validan para que nosotros registremos el impacto real en las bases de datos.
- **Validador de Normalización:** Podemos registrar las alteraciones estructurales y migraciones cuando apliquen sus scripts en bases de datos de producción.

---

#  Conclusión

Hemos construido más que un simple panel web: hemos entregado un **Producto de Software Completo**.

✅ Documentado.
✅ Escalable (API separada).
✅ Integrado al código (VS Code y GitHub Actions).

