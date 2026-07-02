<center>

![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto: *Panel de Auditoría Multi-Motor***

Curso: *Base de Datos II*

Docente: *Ing. Patrick José Cuadros Quiroga*

Integrantes:

***Ramos Atahuachi, Fabricio Farid Edmilson (2023076798)***

***Colque Quispe, Rodrigo Sídney (2023077078)***

**Tacna – Perú**

***2026***

</center>

<div style="page-break-after: always; visibility: hidden"></div>

Sistema *Panel de Auditoría Multi-Motor*

Diccionario de Datos — Base de Datos Local (SQLite)

Versión *1.0*

| CONTROL DE VERSIONES | | | | | |
|:---:|:---|:---|:---|:---|:---|
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | IASR / JSCM | Ing. P. Cuadros | Ing. P. Cuadros | 18/06/2026 | Versión Original |

<div style="page-break-after: always; visibility: hidden"></div>

# ÍNDICE GENERAL

- [1. Descripción General](#1-descripción-general)
- [2. Tabla: `usuarios`](#2-tabla-usuarios)
- [3. Tabla: `registro_accesos`](#3-tabla-registro_accesos)
- [4. Tabla: `conexiones_guardadas`](#4-tabla-conexiones_guardadas)
- [5. Relaciones (Constraints)](#5-relaciones-constraints)

<div style="page-break-after: always; visibility: hidden"></div>

---

## 1. Descripción General

La aplicación Panel de Auditoría Multi-Motor opera almacenando información administrativa y de configuración de manera persistente en una base de datos **SQLite** local (`saas_admin.db`). 

El esquema consta de tres tablas fundamentales: `usuarios` (gestión de acceso al panel), `registro_accesos` (auditoría de inicio de sesión de los usuarios) y `conexiones_guardadas` (almacenamiento de credenciales de bases de datos para acceso rápido).

---

## 2. Tabla: `usuarios`

**Propósito:** Almacena los usuarios autorizados para acceder al panel de auditoría, incluyendo sus credenciales cifradas y roles en el sistema.
**Clave Primaria:** `id`

| Nombre del Campo | Tipo de Dato (SQLite) | Nulo | Descripción / Reglas |
|:-----------------|:----------------------|:-----|:---------------------|
| `id` | `INTEGER` | No | Identificador único autoincremental. Actúa como PK. |
| `username` | `TEXT` | No | Nombre de usuario. Debe ser único (`UNIQUE`). |
| `password` | `TEXT` | No | Contraseña del usuario, almacenada como un hash criptográfico (SHA-256). |
| `rol` | `TEXT` | No | Rol del usuario en el sistema (ej: `admin`, `cliente`). |

---

## 3. Tabla: `registro_accesos`

**Propósito:** Actúa como un historial de los inicios de sesión realizados por los usuarios en el panel, registrando quién accedió y cuándo.
**Clave Primaria:** `id`

| Nombre del Campo | Tipo de Dato (SQLite) | Nulo | Descripción / Reglas |
|:-----------------|:----------------------|:-----|:---------------------|
| `id` | `INTEGER` | No | Identificador único autoincremental. Actúa como PK. |
| `username` | `TEXT` | No | Nombre del usuario que inició sesión. |
| `fecha_hora` | `DATETIME` | No | Marca de tiempo del inicio de sesión. Por defecto `CURRENT_TIMESTAMP`. |

---

## 4. Tabla: `conexiones_guardadas`

**Propósito:** Guarda las credenciales de conexión a las diversas bases de datos monitoreadas, permitiendo una fácil reconexión desde el panel.
**Clave Primaria:** `id`

| Nombre del Campo | Tipo de Dato (SQLite) | Nulo | Descripción / Reglas |
|:-----------------|:----------------------|:-----|:---------------------|
| `id` | `INTEGER` | No | Identificador único autoincremental. Actúa como PK. |
| `username` | `TEXT` | No | Nombre del usuario propietario de la conexión guardada. |
| `alias` | `TEXT` | No | Nombre amigable asignado a la conexión para rápida identificación. |
| `motor` | `TEXT` | No | Motor de la base de datos (ej: `PostgreSQL`, `MySQL`, `MongoDB`). |
| `creds_json` | `TEXT` | No | Cadena JSON que contiene los parámetros de conexión específicos (host, puerto, usuario, contraseña, db). |

---

## 5. Relaciones (Constraints)

Actualmente, las tablas de la base de datos local `saas_admin.db` operan de forma independiente para mantener la simplicidad y rapidez de la arquitectura en SQLite. La vinculación entre tablas (por ejemplo, el campo `username` en `registro_accesos` y `conexiones_guardadas` hacia la tabla `usuarios`) se maneja lógicamente desde el código de la aplicación.
