<center>

![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto: *Panel de Auditoría Multi-Motor***

Curso: *Base de Datos II*

Docente: *Ing. Patrick José Cuadros Quiroga*

Integrantes:

***Colque Quispe, Rodrigo Sídney (2023077078)***

***Ramos Atahuachi, Fabricio Farid Edmilson (2023076798)***

**Tacna – Perú**

***2026***

</center>

<div style="page-break-after: always; visibility: hidden"></div>

Sistema *Panel de Auditoría Multi-Motor*

Estándar de Programación

Versión *1.0*

| CONTROL DE VERSIONES | | | | | |
|:---:|:---|:---|:---|:---|:---|
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | IASR / JSCM | Ing. P. Cuadros | Ing. P. Cuadros | 18/06/2026 | Versión Original |

<div style="page-break-after: always; visibility: hidden"></div>

# ÍNDICE GENERAL

- [1. Introducción](#1-introducción)
- [2. Estándares para el Backend y Lógica (Python)](#2-estándares-para-el-backend-y-lógica-python)
- [3. Estándares para el Frontend (Streamlit)](#3-estándares-para-el-frontend-streamlit)
- [4. Control de Versiones (Git y Commits)](#4-control-de-versiones-git-y-commits)

<div style="page-break-after: always; visibility: hidden"></div>

---

## 1. Introducción

El presente documento define los estándares de programación, convenciones de nomenclatura y mejores prácticas para el desarrollo del proyecto **Panel de Auditoría Multi-Motor**. Al tratarse de una aplicación construida completamente en **Python** utilizando el framework interactivo **Streamlit**, se exigen estándares consistentes que garanticen la mantenibilidad, escalabilidad y legibilidad del código para todo el equipo.

---

## 2. Estándares para el Backend y Lógica (Python)

Todo el desarrollo en la capa lógica (Python) debe seguir las convenciones oficiales definidas en **PEP 8**. Se recomienda apoyarse en formateadores automáticos como `black`.

### 2.1. Nomenclatura (Naming Conventions)
- **Variables y Funciones:** `snake_case`. (ej. `def conectar_base_datos():`, `usuario_actual = ...`).
- **Clases:** `PascalCase` (UpperCamelCase). (ej. `class MonitorPostgres:`).
- **Constantes:** `SCREAMING_SNAKE_CASE`. (ej. `MAX_INTENTOS_CONEXION = 3`).
- **Archivos y Módulos:** Nombres en minúsculas con guiones bajos si es necesario (ej. `database_utils.py`, `mongo_auditor.py`).

### 2.2. Manejo de Errores y Excepciones
- **Evitar bloques `except` genéricos vacíos:** Capturar siempre excepciones de manera específica (ej. `except sqlite3.IntegrityError as e:` en lugar de solo `except:`).
- **Retroalimentación en la UI:** Utilizar `st.error()` o `st.warning()` para notificar al usuario frente a fallos operacionales, y guardar los detalles técnicos en logs.
- **Gestión Segura de Recursos:** Emplear contexto (`with`) para conexiones a archivos o cursores de base de datos para garantizar que se liberen correctamente, o utilizar bloques `try...finally`.

### 2.3. Formateo y Estructura
- **Indentación:** Estándar de 4 espacios. No está permitido el uso de tabulaciones.
- **Ancho máximo de línea:** Recomendado a un máximo de 100 caracteres.
- **Imports:** Agrupar secuencialmente: 1) bibliotecas estándar de Python, 2) paquetes de terceros (ej. `streamlit`, `pandas`), 3) módulos locales del proyecto.

---

## 3. Estándares para el Frontend (Streamlit)

### 3.1. Organización del Multi-Page App
- Todas las pantallas secundarias de la aplicación deben encontrarse dentro del directorio `pages/` y estar prefijadas con un número para mantener el orden exacto en la barra lateral de navegación (ej. `1_Conectar_BD.py`, `2_Monitoreo_Vivo.py`).

### 3.2. Manejo del Estado (Session State)
- Cualquier variable de estado que necesite persistir entre las recargas nativas de la aplicación debe gestionarse a través del diccionario `st.session_state`.
- **Comprobación Previa:** Antes de acceder o mutar una variable de sesión, validar su existencia de forma segura:
  ```python
  if "autenticado" not in st.session_state:
      st.session_state["autenticado"] = False
  ```

### 3.3. Estructuración Visual
- Minimizar el código visual "espagueti". Usar contenedores semánticos (`st.container`, `st.expander`) y distribución por columnas (`st.columns`) para interfaces densas como las gráficas de monitoreo.
- **Inyección HTML/CSS:** Cuando sea estrictamente necesario modificar aspectos como la barra lateral global u ocultar elementos por defecto, inyectar el estilo con `unsafe_allow_html=True` agrupándolo preferiblemente al inicio de la página.

---

## 4. Control de Versiones (Git y Commits)

El proyecto utiliza **Conventional Commits** para mantener la consistencia en el historial y facilitar la revisión de pull requests.

**Formato exigido:**
`<tipo>(<alcance opcional>): <descripción corta>`

**Tipos válidos:**
- `feat:` Inclusión de una nueva característica o integración de motor.
- `fix:` Corrección de un bug detectado en auditorías o accesos.
- `docs:` Cambios que solo afectan la documentación (markdown, diccionarios, tutoriales).
- `style:` Cambios estéticos en el código (formato, comas) o estilos de interfaz visual.
- `refactor:` Optimización del código sin alterar su comportamiento externo.
- `test:` Adición o arreglo de scripts de pruebas unitarias.
- `chore:` Labores misceláneas como actualizar el `requirements.txt` o limpiar configuraciones de despliegue.

**Ejemplos correctos:**
- `feat(ui): integrar endpoint validador de sintaxis sql en una nueva pestaña`
- `fix(auth): corregir acceso a registro de credenciales por usuarios cliente`
- `docs(db): agregar archivo diccionario-de-datos.md para sqlite`
