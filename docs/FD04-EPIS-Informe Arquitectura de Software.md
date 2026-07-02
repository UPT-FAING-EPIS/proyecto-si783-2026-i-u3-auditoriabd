<center>

![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto Auditoría de Base de Datos**

Curso: *Base de Datos II*

Docente: *Mag. Patrick Cuadros Quiroga*

Integrantes:

***Ramos Atahuachi, Fabricio Farid Edmilson (2023076798)***

***Colque Quispe, Rodrigo Sídney (2023077078)***

**Tacna – Perú**

***2026***

</center>

---

# Informe de Arquitectura de Software (FD04)

## CONTROL DE VERSIONES
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1.0 | RF | PCQ | PCQ | 01/05/2026 | Versión Original |

---

## 1. Introducción

### 1.1. Propósito
El propósito de este documento es describir la arquitectura de software del sistema de Auditoría de Base de Datos. Este documento servirá como guía fundamental para el diseño, implementación y mantenimiento de la plataforma, asegurando una correcta integración entre la interfaz interactiva en Streamlit, el procesamiento de datos con Pandas y la persistencia en PostgreSQL.

### 1.2. Alcance
El sistema permite a los Administradores de Base de Datos (DBA) y Auditores:
*   Conectarse a una base de datos PostgreSQL para monitorear en tiempo real las operaciones DML (INSERT, UPDATE, DELETE).
*   Generar automáticamente scripts SQL de reversión (rollbacks) a partir de los registros de auditoría.
*   Cargar y analizar reportes históricos exportados en formato CSV.
*   Filtrar dinámicamente grandes volúmenes de datos directamente desde la interfaz web.

### 1.3. Definición, siglas y abreviaturas
*   **DBA**: Administrador de Base de Datos (Database Administrator).
*   **DML**: Lenguaje de Manipulación de Datos (Data Manipulation Language).
*   **Rollback**: Operación que devuelve la base de datos a un estado previo.
*   **Streamlit**: Framework de Python utilizado para crear aplicaciones web interactivas orientadas a datos.
*   **Pandas**: Librería de Python especializada en la manipulación y análisis de datos estructurados (DataFrames).
*   **CSV**: Valores Separados por Comas (Comma-Separated Values).

### 1.4. Visión General
El sistema está construido sobre una arquitectura modular basada en Python. Utiliza Streamlit como capa de presentación y controlador (app.py, pages/). La lógica de procesamiento recae en Pandas, mientras que la capa de persistencia (database.py) se comunica de forma segura con PostgreSQL mediante psycopg2.

---

## 2. Representación Arquitectónica

### 2.1. Escenarios
*   **Escenario de Monitoreo y Rollback**: Un DBA detecta una modificación no autorizada (UPDATE). Selecciona el registro y el sistema genera el script SQL exacto para restaurar el valor anterior.
*   **Escenario de Análisis Forense**: Un Auditor sube un archivo CSV a la pestaña "Cargador CSV", filtrando dinámicamente para auditar acciones específicas.

### 2.2. Vista Lógica
*   **Capa de Presentación / UI**: Páginas de Streamlit (1_Monitoreo_Vivo.py, 2_Cargador_CSV.py).
*   **Capa de Procesamiento Lógico**: Uso de DataFrames de Pandas para aplicar filtros y transformar datos brutos.
*   **Capa de Acceso a Datos**: Módulo database.py que centraliza la lógica de conexión y ejecución de queries en PostgreSQL.

### 2.3. Vista del Proceso
*   **Solicitud**: El usuario accede a una pestaña del panel.
*   **Extracción**: El sistema lee el archivo CSV o ejecuta un SELECT a la tabla de logs.
*   **Transformación**: Los datos crudos se convierten en un DataFrame de Pandas para su limpieza.
*   **Despliegue**: Streamlit renderiza el DataFrame en pantalla con componentes de interacción.

### 2.4. Vista del desarrollo
*   **Lenguaje**: Python 3.x.
*   **Librerías**: streamlit, pandas, psycopg2-binary.
*   **Estructura**: Código modularizado (app.py, pages/, database.py) con gestión mediante requirements.txt.

### 2.5. Vista Física
*   **Cliente**: Navegador web moderno.
*   **Servidor de Aplicaciones**: Entorno host donde se ejecuta Streamlit (local, Docker o nube).
*   **Servidor de Base de Datos**: Servidor PostgreSQL con tablas y triggers de auditoría.

---

## 3. Objetivos y limitaciones arquitectónicas

### 3.1. Disponibilidad
El sistema debe mantener una conexión estable con la base de datos para el monitoreo en vivo. Si la base de datos no está disponible, debe manejar la excepción de manera limpia y permitir el uso offline del cargador CSV.

### 3.2. Seguridad
Las credenciales no deben quemarse en el código; deben inyectarse mediante variables de entorno o st.secrets. Se previene la inyección SQL mediante consultas parametrizadas en psycopg2.

### 3.3. Adaptabilidad
El acoplamiento con PostgreSQL se limita al archivo database.py. Esto permite migrar a otros motores (MySQL/Oracle) afectando solo ese módulo.

### 3.4. Rendimiento
El uso de Pandas garantiza operaciones de filtrado casi instantáneas (< 2 segundos) para conjuntos de hasta 50,000 registros en memoria.

---

## 4. Análisis de Requerimientos

### 4.1. Requerimientos funcionales
| Código | Requerimiento | Descripción | Prioridad |
| :--- | :--- | :--- | :--- |
| RF01 | Conexión a Base de Datos | Establecer conexión segura a PostgreSQL (database.py). | Alta |
| RF02 | Carga de Reportes CSV | Permitir subir archivos CSV y previsualizar contenido en formato tabular. | Alta |
| RF03 | Monitoreo en Vivo | Consultar y mostrar en tiempo real los últimos registros de auditoría. | Alta |
| RF04 | Filtrado de Datos | Permitir filtrar registros por usuario, fecha, tabla o tipo de operación. | Media |

### 4.2. Requerimientos no funcionales
| Código | Requerimiento | Descripción | Prioridad |
| :--- | :--- | :--- | :--- |
| RNF01 | Rendimiento | Procesamiento de CSV de +10,000 registros en < 3 segundos. | Alta |
| RNF02 | Usabilidad | Interfaz intuitiva con navegación lateral nativa de Streamlit. | Alta |
| RNF03 | Seguridad | Credenciales no codificadas en texto plano (uso de secretos). | Alta |

---

## 5. Vistas de Caso de Uso

<img width="691" height="401" alt="image" src="https://github.com/user-attachments/assets/13eaac7d-2e31-4fdd-a185-1ebb0f7b7440" />

---

## 6. Vista Lógica

### 6.1. Diagrama Contextual

<img width="1234" height="488" alt="image" src="https://github.com/user-attachments/assets/4e252aa4-cc5c-4680-8b73-f4b745129624" />


---

## 7. Vista de Procesos

### 7.1. Diagrama de Proceso Actual

<img width="382" height="770" alt="image" src="https://github.com/user-attachments/assets/ac8c3e83-a03a-4c14-a018-f8bff4628604" />


### 7.2. Diagrama de Proceso Propuesto

<img width="315" height="773" alt="image" src="https://github.com/user-attachments/assets/905ad478-4aaf-425e-9aa1-ff0ff3c11a32" />


---

## 8. Vista de Despliegue

### 8.1. Diagrama de Contenedor

<img width="1398" height="519" alt="image" src="https://github.com/user-attachments/assets/64d21ebd-171a-4ae9-b3f1-e764017d6f7f" />


---

## 9. Vista de implementación

### 9.1. Diagrama de Componentes

<img width="1127" height="663" alt="image" src="https://github.com/user-attachments/assets/abb1c087-b152-489c-acf6-0c0517a915c3" />


---

## 10. Vista de Datos

### 10.1. Diagrama Entidad Relación

<img width="868" height="606" alt="image" src="https://github.com/user-attachments/assets/8255e022-d79b-4f23-a0aa-df5ac6e89aae" />

---

## 11. Calidad

### 11.1. Escenario de Seguridad
*   **Fuente del estímulo**: Actor externo o usuario malicioso.
*   **Estímulo**: Intento de inyectar comandos SQL mediante filtros o campos de entrada.
*   **Artefacto**: Módulo database.py e interfaz Streamlit.
*   **Respuesta**: El sistema utiliza consultas parametrizadas (psycopg2) y manejo de secretos.
*   **Medida de respuesta**: 100% de los intentos de inyección son neutralizados.

### 11.2. Escenario de Usabilidad
*   **Fuente del estímulo**: DBA o Auditor.
*   **Estímulo**: Necesidad de identificar el origen de un error y obtener su rollback.
*   **Respuesta**: Panel interactivo con Pandas y generación de rollback con un solo clic.
*   **Medida de respuesta**: Localización y generación de script en menos de 5 segundos.

### 11.3. Escenario de Adaptabilidad
*   **Fuente del estímulo**: Equipo de desarrollo.
*   **Estímulo**: Necesidad de cambiar el motor de base de datos (ej. a MySQL).
*   **Respuesta**: Gracias al desacoplamiento, solo se modifica database.py sin afectar la UI.
*   **Medida de respuesta**: Cambio de conector realizado en menos de 4 horas de desarrollo.

### 11.4. Escenario de Disponibilidad
*   **Fuente del estímulo**: Falla en el servidor de base de datos.
*   **Estímulo**: Interrupción temporal de conexión con PostgreSQL.
*   **Respuesta**: Detección mediante try-except y notificación amigable al usuario en Streamlit.
*   **Medida de respuesta**: Informe de estado en menos de 2 segundos tras detectar el fallo.

### 11.5. Otro Escenario (Escenario de Performance)
*   **Fuente del estímulo**: Proceso de análisis masivo.
*   **Estímulo**: Carga de archivo CSV extenso (> 50,000 registros).
*   **Respuesta**: Procesamiento en memoria RAM mediante operaciones vectorizadas de Pandas.
*   **Medida de respuesta**: Renderizado de métricas y tablas en menos de 3 segundos.

---
