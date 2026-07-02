<center>

![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

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

# Especificación de Requerimientos de Software (FD03)

## 📋 Introducción
El presente documento describe la **Especificación de Requerimientos de Software (FD03)** para el proyecto de **Auditoría de Base de Datos**. Este sistema es una aplicación web interactiva diseñada para registrar, monitorear y analizar las operaciones y cambios estructurales o de datos que ocurren dentro de un sistema gestor de bases de datos. 

Desarrollado con **Python y Streamlit**, el sistema permite la carga de archivos CSV con reportes de auditoría y ofrece un panel de monitoreo en vivo, facilitando la trazabilidad de la información y la generación de operaciones de reversión (*rollbacks*).

---

## I. Generalidades de la Empresa

### A. Nombre de la empresa
**Auditoría de Base de Datos**

### B. Visión
Ser la plataforma de referencia para la administración y auditoría de bases de datos, garantizando la integridad, seguridad y trazabilidad de la información en entornos corporativos.

### C. Misión
Proveer a los Administradores de Bases de Datos (DBA) y auditores de seguridad una herramienta ágil y automatizada que permita monitorear transacciones en tiempo real, analizar historiales y generar scripts de reversión para proteger la información crítica.

### D. Organigrama
<img width="832" height="618" alt="image" src="https://github.com/user-attachments/assets/7872be39-6ea9-44cb-9018-62599c3b9bc8" />

---

## II. Visionamiento de la Empresa

### A. Descripción de la empresa
El equipo desarrolla una solución centralizada de auditoría. Mediante un panel web, el usuario puede conectarse directamente a la base de datos para observar qué usuario realizó una modificación, en qué tabla y en qué momento (Monitoreo en vivo), además de permitir el análisis forense mediante la carga de reportes exportados previamente en formato .csv.

### B. Objetivos de negocios
*   Garantizar la trazabilidad de los datos registrando operaciones DML (INSERT, UPDATE, DELETE).
*   Proporcionar un mecanismo seguro y rápido para la generación de scripts de reversión (*rollback*) frente a modificaciones no autorizadas o accidentales.
*   Automatizar la lectura y filtrado de grandes volúmenes de registros de auditoría mediante herramientas de análisis de datos.

---

## III. Especificación de Requerimientos de Software

### A. Requerimientos Funcionales Finales
| Código | Requerimiento | Descripción | Prioridad |
| :--- | :--- | :--- | :--- |
| **RF01** | Conexión a BD | Establecer conexión a PostgreSQL y manejar errores de timeout. | Alta |
| **RF02** | Carga de CSV | Importar, leer y visualizar archivos como `reporte_auditar_prueba.csv`. | Alta |
| **RF03** | Monitoreo Vivo | Refrescar automáticamente bajo demanda los registros de la tabla log. | Alta |
| **RF04** | Filtrado Dinámico | Aplicar filtros a los DataFrames de Pandas para refinar las búsquedas. | Alta |
| **RF05** | Gen. Rollbacks | Generar dinámicamente scripts SQL para revertir operaciones específicas basadas en el registro de auditoría. | Alta |

### B. Requerimientos No Funcionales
| Código | Requerimiento | Descripción | Prioridad |
| :--- | :--- | :--- | :--- |
| **RNF01** | Rendimiento | El procesamiento y renderizado de un archivo CSV con más de 10,000 registros debe tomar menos de 3 segundos usando Pandas. | Alta |
| **RNF02** | Usabilidad | La interfaz debe ser intuitiva, con navegación en barra lateral (Sidebar) nativa de Streamlit. | Alta |
| **RNF03** | Seguridad | Las credenciales de acceso a la base de datos no deben estar codificadas en texto plano (uso de secretos/variables de entorno). | Alta |

---

## IV. Fase de Desarrollo

### A. Perfiles de Usuario
*   **Administrador de Base de Datos (DBA):** Configura credenciales, monitorea transacciones sospechosas y genera sentencias de reversión (*rollbacks*).
*   **Auditor / Analista:** Utiliza el cargador de CSV para analizar tendencias y generar gráficos estadísticos sin realizar cambios directos en la base de datos.

### B. Modelo Conceptual: Diagrama de Paquetes 
<img width="553" height="456" alt="image" src="https://github.com/user-attachments/assets/92fc5889-4dd4-4e98-b8c3-d5943ea19c61" />

### B. Modelo Conceptual: Diagrama de Casos de Uso
<img width="691" height="401" alt="image" src="https://github.com/user-attachments/assets/13eaac7d-2e31-4fdd-a185-1ebb0f7b7440" />

### B. Modelo Conceptual: Escenarios Casos de Uso
#### Caso de Uso 01: Monitorear Auditoría en Vivo
| Atributo | Detalle |
| :--- | :--- |
| **Tipo** | Obligatorio |
| **Versión** | V.1.0 |
| **Autor** | Rodrigo Sídney Colque Quispe |
| **Actor(es)** | DBA (Administrador de Base de Datos) |
| **Descripción** | Permite visualizar en tiempo real los registros de auditoría almacenados en la base de datos PostgreSQL, detectando cualquier operación DML (INSERT, UPDATE, DELETE). |
| **Pre-Condiciones** | El sistema debe tener configurada una conexión exitosa a la base de datos a través de `database.py`. |

**Flujo de Eventos:**
| Acción del Actor | Respuesta del Sistema |
| :--- | :--- |
| 1. El usuario selecciona la página "Monitoreo Vivo" en la barra lateral de Streamlit. | 2. El sistema ejecuta una consulta SELECT a la tabla de logs en PostgreSQL. |
| | 3. El sistema recibe los datos crudos y los convierte en un DataFrame utilizando Pandas. |
| 4. El usuario revisa la tabla de registros en pantalla. | 5. El sistema renderiza el DataFrame en la interfaz, mostrando el usuario, fecha, tabla afectada y tipo de operación. |
| 6. El usuario hace clic en el botón de recargar o actualizar. | 7. El sistema vuelve a ejecutar la consulta para mostrar las transacciones más recientes. |

---

#### Caso de Uso 02: Cargar y Analizar CSV
| Atributo | Detalle |
| :--- | :--- |
| **Tipo** | Obligatorio |
| **Versión** | V.1.0 |
| **Autor** | Rodrigo Sídney Colque Quispe |
| **Actor(es)** | Auditor / Analista de Datos |
| **Descripción** | Permite subir reportes de auditoría exportados previamente en formato .csv para su visualización y análisis tabular dentro de la aplicación. |
| **Pre-Condiciones** | El usuario debe poseer un archivo CSV válido (por ejemplo, `reporte_auditar_prueba.csv`). |

**Flujo de Eventos:**
| Acción del Actor | Respuesta del Sistema |
| :--- | :--- |
| 1. El usuario navega a la página "Cargador CSV" desde el menú. | 2. El sistema muestra el componente de subida de archivos (`st.file_uploader`). |
| 3. El usuario arrastra y suelta el archivo CSV en el área designada. | 4. El sistema valida el formato del archivo y lo lee utilizando la librería Pandas. |
| | 5. El sistema estructura los datos en un DataFrame y los despliega en una tabla interactiva en la interfaz de Streamlit. |

> **Flujo Alternativo:** Si el archivo no tiene el formato correcto o está corrupto, el sistema muestra un banner de error solicitando un archivo válido.

---

#### Caso de Uso 03: Generar Script de Rollback
| Atributo | Detalle |
| :--- | :--- |
| **Tipo** | Opcional (Extiende a Monitorear Auditoría en Vivo) |
| **Versión** | V.1.0 |
| **Autor** | Rodrigo Sídney Colque Quispe |
| **Actor(es)** | DBA (Administrador de Base de Datos) |
| **Descripción** | Permite generar automáticamente el código SQL necesario para revertir una transacción específica basándose en los valores "antiguos" y "nuevos" del log de auditoría. |
| **Pre-Condiciones** | El usuario debe estar visualizando un registro de auditoría válido en el módulo de monitoreo. |

**Flujo de Eventos:**
| Acción del Actor | Respuesta del Sistema |
| :--- | :--- |
| 1. El usuario identifica una operación sospechosa o errónea en la tabla de monitoreo. | |
| 2. El usuario selecciona el ID del registro y hace clic en "Generar Rollback". | 3. El sistema extrae los campos `valor_anterior` y `valor_nuevo` del registro seleccionado. |
| | 4. La lógica en Python evalúa el tipo de operación original (si fue INSERT, prepara un DELETE; si fue DELETE, prepara un INSERT; si fue UPDATE, prepara un UPDATE inverso). |
| | 5. El sistema muestra en pantalla un bloque de código con la sentencia SQL exacta para ejecutar la reversión. |

---

#### Caso de Uso 04: Filtrar Registros Dinámicamente
| Atributo | Detalle |
| :--- | :--- |
| **Tipo** | Obligatorio |
| **Versión** | V.1.0 |
| **Autor** | Rodrigo Sídney Colque Quispe |
| **Actor(es)** | DBA / Auditor |
| **Descripción** | Permite aplicar filtros de búsqueda (por nombre de tabla, tipo de acción, usuario o fecha) para refinar los datos mostrados en pantalla. |
| **Pre-Condiciones** | Debe existir un DataFrame con datos cargados (ya sea desde la base de datos o mediante un archivo CSV). |

**Flujo de Eventos:**
| Acción del Actor | Respuesta del Sistema |
| :--- | :--- |
| 1. El usuario interactúa con los selectores o campos de texto en la barra lateral (Sidebar) de Streamlit. | 2. El sistema detecta el cambio en las variables de filtro. |
| 3. El usuario aplica el filtro por "Tipo de Acción" (ej. Solo UPDATE). | 4. El sistema ejecuta métodos de filtrado de Pandas sobre el DataFrame en memoria. |
| | 5. El sistema re-renderiza la tabla en pantalla mostrando únicamente los registros que coinciden con el criterio seleccionado. |

### C. Modelo Lógico: Análisis de Objetos
#### Caso de Uso 01: Monitorear Auditoría en Vivo
<img width="542" height="642" alt="image" src="https://github.com/user-attachments/assets/387a46be-8567-4f92-a293-1523ef05add2" />

#### Caso de Uso 02: Cargar y Analizar CSV
<img width="338" height="659" alt="image" src="https://github.com/user-attachments/assets/7846b3cf-fdc3-41bf-8b87-446c02673eb4" />

#### Caso de Uso 03: Generar Script de Rollback
<img width="178" height="698" alt="image" src="https://github.com/user-attachments/assets/6e0bfed9-9c24-44fe-82fe-261b5c570995" />

#### Caso de Uso 04: Filtrar Registros Dinámicamente
<img width="380" height="703" alt="image" src="https://github.com/user-attachments/assets/10d7920c-334e-44fa-bc10-0813ab0706b2" />

### C. Modelo Lógico: Diagrama de Actividades con objetos
#### Caso de Uso 01: Monitorear Auditoría en Vivo
<img width="213" height="703" alt="image" src="https://github.com/user-attachments/assets/643a8f93-d590-4e66-9609-653748f4ff51" />

#### Caso de Uso 02: Cargar y Analizar CSV
<img width="315" height="715" alt="image" src="https://github.com/user-attachments/assets/199e47f9-09ba-48ad-b7d4-936413366bd8" />

#### Caso de Uso 03: Generar Script de Rollback
<img width="257" height="711" alt="image" src="https://github.com/user-attachments/assets/db4adad0-cdb3-4d45-8010-17ca4f8ecb04" />

#### Caso de Uso 04: Filtrar Registros Dinámicamente
<img width="448" height="693" alt="image" src="https://github.com/user-attachments/assets/10acab78-9f4b-4728-9073-f8aa65031376" />

### C. Modelo Lógico: Diagrama de Secuencia
#### Caso de Uso 01: Monitorear Auditoría en Vivo
<img width="1284" height="557" alt="image" src="https://github.com/user-attachments/assets/0cc78fd2-449d-464e-a41d-95a600960516" />

#### Caso de Uso 02: Cargar y Analizar CSV
<img width="839" height="678" alt="image" src="https://github.com/user-attachments/assets/a41a4917-eabe-4e42-bae4-48ab0ac09804" />

#### Caso de Uso 03: Generar Script de Rollback
<img width="984" height="677" alt="image" src="https://github.com/user-attachments/assets/93d0ea0c-dfff-418d-895f-ab357f52f146" />

#### Caso de Uso 04: Filtrar Registros Dinámicamente
<img width="1342" height="449" alt="image" src="https://github.com/user-attachments/assets/fadb3f78-41c6-42e3-b8c8-086a24547f97" />

### C. Modelo Lógico: Diagrama de Clases
<img width="1205" height="771" alt="image" src="https://github.com/user-attachments/assets/094e635c-4e64-4be0-9314-4ba25dcc8b3f" />

---

## V. Conclusiones y Recomendaciones

### Conclusiones
*   **Trazabilidad:** La automatización en el monitoreo DML reduce el tiempo de inspección manual de logs, garantizando la integridad de los datos críticos.
*   **Arquitectura:** La división entre la lógica de acceso (`database.py`) y el procesamiento analítico (**Pandas**) garantiza una plataforma estable y fluida.
*   **Capacidad de Respuesta:** La generación automatizada de *rollbacks* convierte al sistema en un recurso activo para la rápida recuperación de desastres.

### Recomendaciones
*   **Alertas:** Desarrollar integraciones para envíos automáticos de alertas (webhooks a Slack/Teams) ante operaciones críticas masivas.
*   **Soporte Multi-Motor:** Refactorizar la capa de persistencia para soportar motores como SQL Server, MySQL u Oracle.
*   **Análisis Avanzado:** Incorporar módulos para analizar patrones anómalos de comportamiento y exportar evidencias en formatos inmutables como PDF.
