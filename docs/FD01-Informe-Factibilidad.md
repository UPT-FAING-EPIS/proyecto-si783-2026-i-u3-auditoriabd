<center>

[comment]: <img src="./media/media/image1.png" style="width:1.088in;height:1.46256in" alt="escudo.png" />

![./media/media/image1.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto *Auditoría de Base de Datos***

Curso: *Base de Datos II*

Docente: *Mag. Patrick Cuadros Quiroga*

Integrantes:

***Ramos Atahuachi, Fabricio Farid Edmilson (2023076798)***
***Colque Quispe, Rodrigo Sídney (2023077078)***

**Tacna – Perú**

***2026***
**  
**
</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

Sistema *Auditoría de Base de Datos*

Informe de Factibilidad

Versión *{1.0}*

|CONTROL DE VERSIONES||||||
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| :-: | :- | :- | :- | :- | :- |
| 1.0 | F.R. / R.C. | | | 27/03/2026 | Versión Original |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# **INDICE GENERAL**

[1. Descripción del Proyecto](#_Toc52661346)

[2. Riesgos](#_Toc52661347)

[3. Análisis de la Situación actual](#_Toc52661348)

[4. Estudio de Factibilidad](#_Toc52661349)

[4.1 Factibilidad Técnica](#_Toc52661350)

[4.2 Factibilidad económica](#_Toc52661351)

[4.3 Factibilidad Operativa](#_Toc52661352)

[4.4 Factibilidad Legal](#_Toc52661353)

[4.5 Factibilidad Social](#_Toc52661354)

[4.6 Factibilidad Ambiental](#_Toc52661355)

[5. Análisis Financiero](#_Toc52661356)

[6. Conclusiones](#_Toc52661357)


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**<u>Informe de Factibilidad</u>**

1. <span id="_Toc52661346" class="anchor"></span>**Descripción del Proyecto**

    1.1. Nombre del proyecto
         Auditoría de Base de Datos

    1.2. Duración del proyecto
         Estimada en 5 fases de desarrollo iterativo, específicamente 2 meses de duración.

    1.3. Descripción
         El proyecto consiste en la creación de un sistema automatizado que registre, controle y monitoree todas las transacciones críticas a nivel de datos (DDL y DML). Esto abarca desde la captura de operaciones INSERT, UPDATE y DELETE, hasta el registro de metadatos de sesión, permitiendo identificar anomalías y mantener un historial transparente de los cambios.

    1.4. Objetivos

        1.4.1 Objetivo general
              Implementar un mecanismo de vigilancia técnica para registrar operaciones DML (Insert, Update, Delete) en tiempo real.
        1.4.2 Objetivos Específicos
              - Diseñar una estructura de logs centralizada e inalterable.
              - Desarrollar disparadores (triggers) que capturen el contexto de sesión (IP y Usuario).
              - Generar reportes legibles para auditores externos o administradores de base de datos.
              - Realizar pruebas de integridad, optimizar índices para evitar impacto en el rendimiento y elaborar la documentación final.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

2. <span id="_Toc52661347" class="anchor"></span>**Riesgos**

    - **Rendimiento:** Posible aumento en el tiempo de respuesta de las transacciones debido a la ejecución de triggers.
    - **Almacenamiento:** Crecimiento acelerado de la tabla de logs en bases de datos de alto tráfico.
    - **Privacidad:** Riesgo de acceso no autorizado a los logs de auditoría por parte de personal técnico.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

3. <span id="_Toc52661348" class="anchor"></span>**Análisis de la Situación actual**

    3.1. Planteamiento del problema
         Actualmente, las bases de datos transaccionales sufren modificaciones sin un rastro claro del origen, usuario o momento del cambio. Esto genera vulnerabilidades operativas y de seguridad que impiden investigar manipulaciones indebidas o errores de sistema de forma eficaz.

    3.2. Consideraciones de hardware y software
         La implementación requiere el motor de base de datos actual de la institución (ej. SQL Server o PostgreSQL) y herramientas de gestión nativas. A nivel de hardware, se requiere capacidad de disco adicional en el servidor para almacenar la nueva tabla de Logs estructurada.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

4. <span id="_Toc52661349" class="anchor"></span>**Estudio de Factibilidad**

    4.1. <span id="_Toc52661350" class="anchor"></span>Factibilidad Técnica
         El proyecto es altamente factible. Las tecnologías propuestas (DDL, Vistas SQL, Triggers y Stored Procedures) son nativas de cualquier Sistema Gestor de Base de Datos Relacional (RDBMS) estándar. No se requiere la adquisición de software de terceros, lo que facilita cubrir las necesidades del sistema propuesto íntegramente mediante código SQL.

    4.2. <span id="_Toc52661351" class="anchor"></span>Factibilidad Económica

        4.2.1. Costos Generales
               Equipos de desarrollo ya disponibles (computadoras, software de diseño).

        4.2.2. Costos operativos durante el desarrollo
               Consumo eléctrico y conectividad a internet durante el periodo de programación.

        4.2.3. Costos del ambiente
               Posible aumento en el costo de almacenamiento de red a largo plazo debido a los registros generados.

        4.2.4. Costos de personal
               Inversión en horas hombre de los ingenieros de software o DBAs encargados de la programación de triggers, vistas y pruebas de rendimiento.

        4.2.5. Costos totales del desarrollo del sistema
               Se calcularán en base a las horas necesarias para completar las 20 tareas de GitHub (aprox. S/ 500.00 en recursos operativos directos).

    4.3. <span id="_Toc52661352" class="anchor"></span>Factibilidad Operativa
         La automatización del monitoreo se ejecutará en segundo plano sin interrumpir las tareas del usuario final. El mantenimiento futuro estará garantizado gracias a la creación de un Manual y README en la fase de cierre.

    4.4. <span id="_Toc52661353" class="anchor"></span>Factibilidad Legal
         Es completamente factible e, incluso, necesario. Ayuda a cumplir de forma rigurosa con regulaciones de protección de datos personales mediante el registro de quién accede y modifica la información.

    4.5. <span id="_Toc52661354" class="anchor"></span>Factibilidad Social
         Promueve una cultura organizacional de transparencia y responsabilidad entre los colaboradores.

    4.6. <span id="_Toc52661355" class="anchor"></span>Factibilidad Ambiental
         No genera ningún impacto ambiental negativo directo.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

5. <span id="_Toc52661356" class="anchor"></span>**Análisis Financiero**

    El plan financiero evalúa la viabilidad del proyecto mediante el análisis de los flujos de ingresos y egresos proyectados en el tiempo, con el fin de asegurar que la inversión sea sostenible y detectar posibles desequilibrios económicos antes de la ejecución.

    5.1. Justificación de la Inversión

        5.1.1. Beneficios del Proyecto

            Beneficios tangibles:
            - Reducción de costos operativos: Disminución del tiempo que el personal de TI dedica a la investigación manual de errores o manipulaciones en las tablas.
            - Prevención de pérdidas financieras: Mitigación de riesgos económicos asociados a fraudes o alteraciones no detectadas en transacciones críticas.
            - Cumplimiento legal: Evita posibles multas por incumplimiento de normativas de protección de datos al mantener registros de acceso y modificación.
            - Disponibilidad de recursos: Optimización del uso de talento humano al automatizar la vigilancia de la base de datos.

            Beneficios intangibles:
            - Aumento en la confiabilidad: Mayor seguridad en la veracidad de la información almacenada para todos los niveles de la organización.
            - Transparencia organizacional: Fomenta una cultura de responsabilidad entre los usuarios con acceso a datos sensibles.
            - Toma acertada de decisiones: Proporciona un historial transparente que sirve de base para análisis forenses y auditorías de gestión.
            - Mejora en la reputación: Aporta valor agregado al producto o servicio al garantizar estándares altos de integridad de datos.

        5.1.2. Criterios de Inversión

            5.1.2.1. Relación Beneficio/Costo (B/C)
                     Costos (C): Estimando 2 meses de desarrollo por 2 integrantes con un costo simbólico de S/ 250.00 en recursos operativos (luz e internet) y el valor del tiempo de desarrollo, sumamos una inversión total de S/ 500.00.
                     Beneficios (B): Se estima que el sistema previene la pérdida de integridad de datos cuyo costo de recuperación manual o pérdida de información crítica ascendería a S/ 1,800.00 anuales.
                     B/C = 1800 / 500 = 3.6
                     Evaluación: Al ser mayor a 1, se acepta el proyecto.

            5.1.2.2. Valor Actual Neto (VAN)
                     Considerando que el software no tiene costo de licencia y el mantenimiento es interno, proyectamos un flujo neto de ahorro de S/ 150.00 mensuales.
                     - Inversión Inicial: S/ 500.00.
                     - Flujos Netos (12 meses): S/ 1,800.00 anuales.
                     - Tasa de Descuento (COK): 10% anual.
                     Calculando el valor presente, el VAN resultante es de S/ 1,136.36.
                     Criterio de aceptación: Al ser el VAN > 0, se confirma que el sistema genera un beneficio económico real.

            5.1.2.3. Tasa Interna de Retorno (TIR)
                     Debido a que el desarrollo se basa en tecnologías nativas (scripts DDL, Triggers), la rentabilidad es excepcionalmente alta en comparación con adquirir una herramienta de auditoría comercial.
                     - TIR Estimada: 62%
                     - Costo de Oportunidad (COK): 10%
                     Evaluación: Como la TIR (62%) es mayor que el COK (10%), se acepta el proyecto.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

6. <span id="_Toc52661357" class="anchor"></span>**Conclusiones**

    El desarrollo de las 5 fases planteadas para el Sistema de Auditoría de Base de Datos es factible a nivel técnico, operativo y económico. Utiliza tecnología y recursos nativos de base de datos que la organización ya posee, minimizando la inversión. Su ejecución logrará blindar la integridad del sistema y responderá eficazmente ante cualquier evento o anomalía de seguridad en la información.
