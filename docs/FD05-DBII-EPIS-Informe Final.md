<center>

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

# Informe Final 
 
**Proyecto Auditoría de Base de Datos** 

Curso: Base de Datos II 

Docente: Mag. Patrick Cuadros Quiroga 

Integrantes:

Colque Quispe, Rodrigo Sídney (2023077078)<br>
Ramos Atahuachi, Fabricio Farid Edmilson (2023076798)

Tacna – Perú

2026

</center>

<div style="page-break-after: always; visibility: hidden"></div>

**CONTROL DE VERSIONES**

| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
|:---:|:---|:---|:---|:---|:---|
| 1.0 | R.C. , F.R. | | | 12/06/2026 | Versión Original |

Sistema Auditoria de Base de Datos
Documento Final de Proyecto

Versión {1.0}

## 1. Antecedentes
Tradicionalmente, la administración y revisión de los historiales de operaciones en las bases de datos corporativas requiere que los administradores ejecuten consultas manuales e inspeccionen las columnas afectadas de manera visual. Este enfoque convencional no solo consume una cantidad significativa de tiempo, sino que retrasa la detección de anomalías y dificulta la rápida recuperación de la información ante modificaciones accidentales o no autorizadas.

## 2. Planteamiento del Problema							

### a. Problema
La falta de herramientas interactivas que consoliden los registros operativos genera un monitoreo deficiente de las transacciones DML (INSERT, UPDATE, DELETE), complicando el análisis forense y la construcción manual de scripts de reversión para reparar alteraciones en los datos.

### b. Justificación
Es necesario proveer a los Administradores de Bases de Datos (DBA) y auditores de seguridad de una herramienta ágil y automatizada. Al implementar este panel, se garantiza la integridad, seguridad y trazabilidad de la información crítica, reduciendo los tiempos de respuesta frente a incidentes.

### c. Alcance
El sistema abarcará la conexión segura a instancias de bases de datos PostgreSQL mediante psycopg2, un módulo para importar y analizar reportes mediante archivos CSV, y un módulo de monitoreo en vivo que consulte directamente las tablas de log, permitiendo la generación del código SQL necesario para revertir operaciones específicas.

## 3. Objetivos

### a. Objetivo General:
Desarrollar e implementar una plataforma centralizada y web interactiva para la administración y auditoría de bases de datos PostgreSQL.

### b. Objetivos Específicos:
- Garantizar la trazabilidad de los datos registrando y visualizando operaciones DML en tiempo real.
- Proporcionar un mecanismo seguro para la generación automatizada de scripts de reversión (rollback) basándose en los valores anteriores y nuevos.
- Desarrollar interfaces interactivas para facilitar la visualización.
- Automatizar la lectura, filtrado dinámico y análisis de grandes volúmenes de registros de auditoría mediante herramientas de análisis de datos.

## 4. Marco Teórico	
- **Auditoría de BD:** Proceso de monitoreo de las modificaciones de los datos (INSERT, UPDATE, DELETE) para garantizar trazabilidad.
- **Streamlit:** Framework de Python altamente viable para construir de manera ágil interfaces web rápidas, modulares e interactivas sin necesidad de un frontend complejo desde cero.
- **Pandas:** Librería de Python especializada en estructurar, procesar, limpiar y visualizar conjuntos de datos masivos en memoria mediante DataFrames.
- **PostgreSQL & Psycopg2:** Sistema gestor relacional y su respectivo adaptador de base de datos para Python, empleado para ejecutar consultas e interacciones de forma segura.

## 5. Desarrollo de la Solución							

### a. Análisis de Factibilidad (técnico, económica, operativa, social, legal, ambiental)
- **Técnica:** Viable por el uso del ecosistema Python, asegurando un entorno rico para manejo analítico de datos (Pandas) y conexiones relacionales sólidas.
- **Económica:** El desarrollo no incurre en costos de licencias. El despliegue está configurado para plataformas PaaS como Railway o Render que ofrecen capas gratuitas.
- **Operativa:** Altamente viable ya que soluciona un problema crítico real para los DBAs respecto al seguimiento de integridad de datos.

### b. Tecnología de Desarrollo
- **Lenguaje:** El lenguaje principal empleado fue Python 3.x, integrando streamlit para el entorno web, pandas como motor analítico y psycopg2-binary para la persistencia.
- Se utilizó una arquitectura modular desacoplada separando las capas. La lógica de conexión se aisló en `database.py`, la presentación web se manejó en `app.py` y el subdirectorio `pages/`, mientras que el flujo de eventos se definió en los documentos SRS (FD03) y SAD (FD04) garantizando adaptabilidad estructural.

### c. Metodología de implementación (Documento de VISION, SRS, SAD)
Se utilizó una arquitectura en capas (Controller-Service-Repository) siguiendo el patrón MVC (Modelo-Vista-Controlador). El desarrollo fue iterativo, comenzando por el modelo de datos (Usuario, Tarea), seguido por la lógica de negocio (TareaService) y finalmente las vistas (dashboard.html).

## 6. Cronograma
El proyecto se estructuró en 5 fases secuenciales distribuidas a lo largo de un periodo de 4 semanas de desarrollo:

| Fase | Actividad Principal | Semana 1 | Semana 2 | Semana 3 | Semana 4 | Responsable |
|:---|:---|:---:|:---:|:---:|:---:|:---|
| Fase 1: Planificación | Levantamiento de requerimientos y diseño arquitectónico (SRS/SAD). | X | | | | Todo el equipo |
| Fase 2: Persistencia | Modelado de datos y configuración de triggers de auditoría en PostgreSQL. | X | X | | | Ingeniero de Datos / DBA |
| Fase 3: Lógica | Desarrollo del conector database.py y la lógica de inversión SQL para rollbacks. | | X | X | | Todo el equipo |
| Fase 4: UI & Análisis | Construcción del panel interactivo en Streamlit (app.py, pages/) e integración de Pandas. | | | X | X | Desarrollador Frontend |
| Fase 5: Cierre | Pruebas de carga con archivos CSV masivos, optimización de performance y documentación final. | | | | X | Todo el equipo |


## 7. Presupuesto
Al tratarse de un proyecto académico fundamentado en herramientas de código abierto (Open Source), el costo de licenciamiento de software es de cero. El presupuesto se enfoca en la valoración de los recursos humanos, la infraestructura de hardware existente y los servicios operativos proporcionales utilizados durante el mes de desarrollo:

### 7.1 Costos de Recursos Humanos (Personal)

| Rol | Cantidad | Horas Totales (4 semanas) | Costo por Hora (S/.) | Total (S/.) |
|:---|:---:|:---:|:---:|:---|
| Jefe de Proyecto / Scrum Master | 1 | 40 | 25.00 | 1,000.00 |
| Ingeniero de Datos / DBA | 1 | 60 | 20.00 | 1,200.00 |
| Desarrollador Frontend & Analista | 1 | 60 | 20.00 | 1,200.00 |
| **Subtotal Personal** | | | | **S/. 3,400.00** |

### 7.2 Costos de Equipos y Materiales (Infraestructura)

| Descripción | Cantidad | Costo Unitario Referencial (S/.) | Porcentaje de Uso / Depreciación | Total Proporcional (S/.) |
|:---|:---:|:---:|:---:|:---|
| Laptop Core i7 / 16GB RAM (Desarrollo) | 2 | 3,500.00 | 10% | 700.00 |
| Materiales de escritorio y apuntes | - | - | Consumo directo | 50.00 |
| **Subtotal Equipos** | | | | **S/. 750.00** |
								
### 7.3 Costos Operativos y de Servicios

| Servicio | Tarifa Mensual Estándar (S/.) | Porcentaje de Asignación al Proyecto | Total Asignado (S/.) |
|:---|:---:|:---:|:---|
| Conectividad a Internet (Fibra Óptica) | 120.00 | 100% | 120.00 |
| Consumo de Energía Eléctrica | 150.00 | 50% | 75.00 |
| **Subtotal Servicios** | | | **S/. 195.00** |

### 7.4 Resumen de Costo Total del Proyecto 

| Categoría de Gasto | Monto Total (S/.) | Porcentaje del Presupuesto |
|:---|:---|:---|
| 7.1. Recursos Humanos | 3,400.00 | 78.2% |
| 7.2. Equipos y Materiales | 750.00 | 17.3% |
| 7.3. Servicios Operativos | 195.00 | 4.5% |
| **COSTO TOTAL DEL PROYECTO** | **S/. 4,345.00** | **100.00%** |

## 8. Conclusiones
- **Trazabilidad y Seguridad:** La automatización en el monitoreo de operaciones DML reduce drásticamente el tiempo invertido en la inspección manual de logs, permitiendo identificar alteraciones inmediatas.
- **Eficacia de la Arquitectura Desacoplada:** La estricta división del sistema (separando database.py, Pandas en memoria y Streamlit) garantizó fluidez y mantenibilidad, permitiendo procesar históricos grandes sin sobrecargar el rendimiento.
- **Capacidad de Respuesta Activa:** Al incorporar la generación automatizada de scripts de rollback, la herramienta evolucionó de un visor pasivo a un recurso activo indispensable para la recuperación ágil de la base de datos.

## 9. Recomendaciones
- **Integración con Sistemas de Alertas:** Se sugiere desarrollar envíos automáticos de notificaciones o webhooks (Slack/Teams) para emitir alertas en tiempo real sobre operaciones masivas críticas.
- **Ampliación de Motores Soportados:** Refactorizar la capa de persistencia mediante un ORM para que el panel se conecte a otros gestores corporativos como MySQL, SQL Server u Oracle.
- **Exportación Forense Avanzada:** Evolucionar la plataforma para exportar las vistas filtradas a formatos inmutables como PDF, facilitando evidencias para auditorías normativas como la ISO 27001.

## 10. Bibliografía									

## 11. Anexos										

### a. Anexo 01 Informe de Factiblidad
Este documento justifica por qué el proyecto es viable.
- **Factibilidad Técnica:** El proyecto es técnicamente viable ya que utiliza el ecosistema de Python, el cual cuenta con herramientas maduras para el análisis de datos (Pandas) y la creación de interfaces web rápidas (Streamlit) sin requerir una infraestructura compleja.
- **Factibilidad Económica:** Es altamente factible económicamente debido a que todas las tecnologías empleadas (Python, Streamlit, PostgreSQL) son de código abierto (Open Source), eliminando los costos de licencias de software.
- **Factibilidad Operativa:** El sistema beneficiará directamente al área de TI (DBAs y Auditores), reduciendo los tiempos de análisis forense de datos. La interfaz nativa de Streamlit garantiza una curva de aprendizaje mínima para los usuarios.
- **Factibilidad Legal:** El sistema no entra en conflicto con normativas legales; por el contrario, apoya el cumplimiento de leyes de protección de datos al garantizar la trazabilidad de quién y cuándo modificó información sensible.
- **Factibilidad Social:** Mejora el control interno, promoviendo un clima de responsabilidad y ética en el manejo de la información corporativa.
- **Factibilidad Ambiental:** Al ser un producto de software alojado digitalmente, su impacto ambiental es mínimo, limitado únicamente al consumo energético del servidor.
- **Beneficios del Proyecto:**
  - *Beneficios Tangibles:* Reducción de horas hombre dedicadas a la inspección manual de bases de datos.
  - *Beneficios Intangibles:* Aumento de la confiabilidad de la información, toma rápida de decisiones ante incidentes y prevención de pérdida de datos críticos.
- **Criterios de Inversión:** Dado que es un proyecto de desarrollo de software académico y de código abierto, los costos se limitan a las horas de desarrollo del equipo. La Relación Beneficio/Costo (B/C) es favorable (>1) ya que la automatización de la auditoría previene pérdidas económicas severas por corrupción de datos empresariales.
- **Conclusiones:** Los resultados del análisis indican que el proyecto "Auditoría de Base de Datos" es completamente viable y factible técnica, operativa y económicamente. El uso de tecnologías modernas y gratuitas permite desarrollar una solución robusta que resuelve una necesidad crítica en la administración de datos con una inversión económica nula en licenciamiento.

### b. Anexo 02 Documento de Visión
- **Declaración del Problema:** La dificultad de las personas para organizar sus tareas diarias y recordatorios en una sola plataforma.
- **Declaración de la Solución:** OptiPlan, una plataforma web centralizada.
- **Características Principales:**
  - Gestión de tareas por categorías y prioridades.
  - Visualización en calendario mensual y semanal.
  - Sistema de alertas auditivas y visuales.

### c. Anexo 03 Documento SRS

**a) Cuadro de Requerimientos Funcionales:**

| ID | Requerimiento Funcional | Descripción | Prioridad |
|:---|:---|:---|:---|
| RF01 | Captura de Operaciones DML | El sistema debe detectar e interceptar automáticamente cada INSERT, UPDATE y DELETE realizado en las tablas seleccionadas. | Alta |
| RF02 | Registro de Metadatos | Se debe almacenar por cada evento: Usuario de BD, Fecha y Hora exacta, Dirección IP, Tipo de operación y el Nombre de la tabla. | Alta |
| RF03 | Persistencia de Valores | En caso de actualizaciones (UPDATE), el sistema debe guardar el valor anterior y el valor nuevo del campo modificado para permitir comparaciones. | Alta |
| RF04 | Visualización Web de Logs | La aplicación debe presentar una tabla legible con todos los registros de auditoría almacenados para facilitar la revisión del auditor. | Media |
| RF05 | Filtros de Búsqueda | El sistema debe permitir al usuario filtrar los logs por rango de fechas, usuario específico o tipo de operación (Ej: ver solo eliminaciones). | Media |

**b) Cuadro de Requerimientos No Funcionales:**

| ID | Requerimiento No Funcional | Descripción |
|:---|:---|:---|
| RNF01 | Disponibilidad | Los mecanismos de captura (triggers) deben estar activos de forma permanente y transparente sin interrumpir el servicio de la BD. |
| RNF02 | Despliegue | La interfaz de usuario debe estar desplegada en un servidor web accesible vía URL (ej. Railway o Render). |
| RNF03 | Rendimiento | El impacto del proceso de auditoría no debe exceder el 5% de carga adicional sobre el tiempo de ejecución de las transacciones originales. |
| RNF04 | Integridad | La tabla de auditoría debe ser de "solo inserción"; ningún usuario, incluido el administrador, debe poder modificar los logs generados. |

**c) Reglas de Negocio**

| ID | DESCRIPCIÓN DE LA REGLA |
|:---|:---|
| RN01 | Inmutabilidad de los Logs: Los registros de auditoría generados por los triggers son estrictamente de solo lectura (Read-Only) en la capa de la aplicación web. Ningún usuario, sin importar su nivel de acceso, puede editar o eliminar un log desde la interfaz. |
| RN02 | Privilegios de Acceso Estricto: El acceso a la plataforma web es exclusivo para el rol "Auditor". Personal de desarrollo, administradores de base de datos (DBA) o usuarios regulares no deben tener credenciales para la interfaz web de visualización. |
| RN03 | Integridad del Registro (Campos Obligatorios): Para que el trigger inserte exitosamente un evento en la tabla de logs, debe capturar de forma obligatoria: Usuario de la BD, Dirección IP, Fecha/Hora exacta del servidor, Tipo de Operación (INSERT, UPDATE, DELETE) y Tabla afectada. |
| RN04 | Captura de Transiciones (UPDATE): Cuando se detecte una operación de tipo UPDATE, es regla de negocio obligatoria que el sistema almacene tanto el estado anterior del registro (OLD) como el estado nuevo (NEW) para garantizar la trazabilidad del cambio. |
| RN05 | Principio de No Interferencia: La ejecución de los triggers de auditoría debe ser asíncrona o estar optimizada para no bloquear ni revertir la transacción original (DML) del usuario en el sistema principal, garantizando que el rendimiento (RNF03) no se vea penalizado. |
| RN06 | Seguridad de Credenciales Web: Todas las contraseñas de los auditores para acceder al dashboard web deben ser encriptadas (ej. mediante BCrypt o SHA-256) antes de almacenarse en la base de datos de la aplicación. |
| RN07 | Seguridad de Sesión: Tras un periodo de inactividad de 15 minutos en la aplicación web, la sesión del auditor debe cerrarse automáticamente para prevenir el acceso no autorizado a información sensible en pantallas desatendidas. |
| RN08 | Restricción de Exportación de Datos: La generación de reportes (PDF/Excel) solo procesará los datos que coincidan con los filtros de fecha y tabla aplicados en ese momento por el auditor, evitando descargas masivas accidentales de toda la base de datos. |

### d. Anexo 04 Documento SAD
- **Diagrama Contextual:** Este diagrama ofrece una vista de alto nivel que muestra cómo el usuario interactúa con el sistema en su totalidad y las dependencias externas.
  - **Usuario (DBA / Auditor):** Es el actor principal que monitorea las transacciones en vivo, carga reportes históricos en formato CSV y genera los scripts de rollback.
  - **Panel de Auditoría (Sistema Central):** Es la plataforma web construida en Streamlit encargada de procesar los logs, aplicar filtros a los datos y generar las sentencias SQL para revertir cambios. El usuario interactúa con este panel a través de una conexión HTTPS.
  - **Base de Datos (Sistema Externo/Dependencia):** Representa el entorno PostgreSQL que almacena las tablas monitoreadas, los usuarios y el historial completo de los logs de auditoría. El Panel de Auditoría se comunica con esta base de datos ejecutando consultas de log mediante el protocolo TCP/IP.


- **Diagrama de Contenedor:** Este diagrama hace un "zoom" dentro del sistema para mostrar las aplicaciones o contenedores de ejecución principales que lo conforman.
  - **Actor:** El DBA o Auditor administra la base de datos y audita las operaciones DML, interactuando directamente con la aplicación web mediante HTTPS para visualizar los paneles y subir los archivos CSV.
  - **Frontera del Sistema (Sistema de Auditoría):** Agrupa los dos grandes bloques tecnológicos:
    - *Aplicación Web y Procesamiento:* Contenedor desarrollado con Python, Streamlit y Pandas. Su función es renderizar la interfaz web, procesar los DataFrames en memoria y alojar la lógica necesaria para la generación de rollbacks.
    - *Base de Datos:* Contenedor PostgreSQL que almacena tanto los registros históricos como los datos en vivo generados por los triggers de auditoría.
  - La comunicación entre la Aplicación Web y la Base de Datos se realiza para consultar la tabla de logs a través de TCP/IP.

- **Diagrama de Componentes:** Este diagrama detalla la estructura interna del contenedor de la "Aplicación Web (Python)", mostrando cómo se dividen las responsabilidades en el código.
  - **Capa de Presentación (UI) [Streamlit]:** Abarca app.py y la carpeta pages/. Maneja el renderizado interactivo de la plataforma web. Lee el flujo de bytes directamente desde los Archivos CSV externos (cargándolos en memoria) e interactúa con el resto de los componentes internos mediante llamadas.
  - **Motor de Procesamiento [Pandas]:** Recibe parámetros de filtro desde la Capa de Presentación. Se encarga de limpiar y estructurar grandes volúmenes de datos convirtiéndolos en DataFrames tras recibir tuplas crudas desde el conector de base de datos.
  - **Conector de Base de Datos [database.py (psycopg2)]:** Componente vital que abre y cierra las sesiones, maneja excepciones y ejecuta las queries directamente hacia la Base de Datos PostgreSQL externa vía TCP/IP. Recibe solicitudes de carga de registros desde la UI.
  - **Generador de Rollbacks [Python]:** Contiene la lógica de negocio pura. Es invocado por la UI para solicitar la creación de un script de reversión. Para lograrlo, le pide al Conector de Base de Datos los valores 'anterior' y 'nuevo', evalúa los JSONs y construye el código SQL inverso.

### e. Anexo 05 Manuales y otros documentos
- Login de la web.
- Registro de la web.
- Dashboard
- Cargador CSV
- Conexión a Base de Datos
- Alertas y Resumen de actividad
