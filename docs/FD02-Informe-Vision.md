<center>

[comment]: <img src="./media/media/image1.png" style="width:1.088in;height:1.46256in" alt="escudo.png" />

![./media/media/image1.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto: Auditoría de Base de Datos**

Curso: Base de Datos II

Docente: Mag. Patrick Cuadros Quiroga

Integrantes:

**Ramos Atahuachi, Fabricio Farid Edmilson (2023076798)**
**Colque Quispe, Rodrigo Sídney (2023077078)**

**Tacna – Perú**

**2026**

</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

| CONTROL DE VERSIONES | | | | | |
| :---: | :--- | :--- | :--- | :--- | :--- |
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | R.A. / C.Q. | P.C. | P.C. | 04/04/2026 | Versión Original |

**Sistema: Auditoría de Base de Datos**

**Documento de Visión**

**Versión *{1.0}***
**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


**INDICE GENERAL**

1. [Introducción](#1-introducción)
   1.1 Propósito
   1.2 Alcance
   1.3 Definiciones, Siglas y Abreviaturas
   1.4 Referencias
   1.5 Visión General
2. [Posicionamiento](#2-posicionamiento)
   2.1 Oportunidad de negocio
   2.2 Definición del problema
3. [Descripción de los interesados y usuarios](#3-descripción-de-los-interesados-y-usuarios)
   3.1 Resumen de los interesados
   3.2 Resumen de los usuarios
   3.3 Entorno de usuario
   3.4 Perfiles de los interesados
   3.5 Perfiles de los Usuarios
   3.6 Necesidades de los interesados y usuarios
4. [Vista General del Producto](#4-vista-general-del-producto)
   4.1 Perspectiva del producto
   4.2 Resumen de capacidades
   4.3 Suposiciones y dependencias
   4.4 Costos y precios
   4.5 Licenciamiento e instalación
5. [Características del producto](#5-características-del-producto)
6. [Restricciones](#6-restricciones)
7. [Rangos de calidad](#7-rangos-de-calidad)
8. [Precedencia y Prioridad](#8-precedencia-y-prioridad)
9. [Otros requerimientos del producto](#9-otros-requerimientos-del-producto)
   b) Estándares legales
   c) Estándares de comunicación
   d) Estándares de cumplimiento de la plataforma
   e) Estándares de calidad y seguridad
[CONCLUSIONES](#conclusiones)
[RECOMENDACIONES](#recomendaciones)
[BIBLIOGRAFIA](#bibliografia)
[WEBGRAFIA](#webgrafia)

---

# 1. Introducción

**1.1 Propósito**
Definir la visión y objetivos del Sistema de Auditoría de Base de Datos para implementar una vigilancia técnica inalterable de operaciones DML.

**1.2 Alcance**
Creación de triggers y logs automatizados para registrar INSERT, UPDATE y DELETE, capturando IP y Usuario en tiempo real.

**1.3 Definiciones, Siglas y Abreviaturas**
* **DML:** Data Manipulation Language.
* **Trigger:** Disparador automático ante eventos de base de datos.
* **Log:** Registro estructurado de eventos.

**1.4 Referencias**
* Informe de Factibilidad (FD01).
* Repositorio de tareas en GitHub (20 tareas).

**1.5 Visión General**
El sistema garantiza trazabilidad total sin recurrir a software externo, utilizando recursos nativos del RDBMS.

---

# 2. Posicionamiento

**2.1 Oportunidad de negocio**
Blindar la seguridad institucional y prevenir fraudes mediante trazabilidad técnica, con un ahorro proyectado de S/ 1,800.00 anuales.

**2.2 Definición del problema**
Falta de rastro claro en modificaciones críticas, afectando la seguridad operativa y la capacidad de análisis forense.

---

# 3. Descripción de los interesados y usuarios

**3.1 Resumen de los interesados**
Administradores (DBA), Auditores de sistemas y personal de cumplimiento TI.

**3.2 Resumen de los usuarios**
Auditores técnicos que requieren reportes de movimientos y DBAs que supervisan el rendimiento.

**3.3 Entorno de usuario**
Ejecución en segundo plano sobre el servidor de base de datos (SQL Server/PostgreSQL).

**3.4 Perfiles de los interesados**
Equipo de desarrollo (Ingenieros) y Gerencia interesada en cumplimiento legal.

**3.5 Perfiles de los Usuarios**
Usuario con conocimientos en SQL y auditores enfocados en la integridad de datos.

**3.6 Necesidades de los interesados y usuarios**
Seguridad, registro inalterable y bajo impacto en el rendimiento.

---

# 4. Vista General del Producto

**4.1 Perspectiva del producto**
Capa de vigilancia interna integrada nativamente al gestor de base de datos.

**4.2 Resumen de capacidades**
Captura de IP, fecha, usuario y valores modificados en tablas críticas de forma automática.

**4.3 Suposiciones y dependencias**
Disponibilidad de espacio en disco para el histórico de logs y soporte de triggers en el RDBMS.

**4.4 Costos y precios**
Inversión de S/ 500.00 con un VAN de S/ 1,136.36.

**4.5 Licenciamiento e instalación**
Propiedad interna; instalación mediante scripts SQL sin costo de licencia de terceros.

---

# 5. Características del producto
* Automatización mediante disparadores.
* Centralización de logs.
* Identificación de origen por IP.

---

# 6. Restricciones
* Capacidad de hardware limitada para el crecimiento del log.
* Restricciones de acceso para evitar que el mismo DBA borre su rastro.

---

# 7. Rangos de calidad
* Integridad: 100% de operaciones registradas.
* Desempeño: Impacto transaccional menor al 5%.

---

# 8. Precedencia y Prioridad
Prioridad alta a la creación de la tabla de logs y triggers DML fundamentales.

---

# 9. Otros requerimientos del producto

**b) Estándares legales**
Cumplimiento de la Ley de Protección de Datos Personales.

**c) Estándares de comunicación**
Reportes legibles en SQL y documentación en README de GitHub.

**d) Estándares de cumplimiento de la plataforma**
Uso estricto de sintaxis nativa de la plataforma institucional.

**e) Estándares de calidad y seguridad**
Acceso restringido a tablas de auditoría.

---

# CONCLUSIONES
El proyecto es viable con un beneficio/costo de 3.6 y garantiza la seguridad de la información institucional.

---

# RECOMENDACIONES
Implementar mantenimiento mensual para purgar logs antiguos y optimizar índices.

---

# BIBLIOGRAFIA
* Ramos, F. & Colque, R. (2026). *Informe de Factibilidad: Auditoría de BD*. UPT.

---

# WEBGRAFIA
* Microsoft SQL Docs. *DML Triggers*. https://learn.microsoft.com/
