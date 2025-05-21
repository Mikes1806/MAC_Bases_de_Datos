# Proyecto 3

## Descripción
• Este proyecto consiste en la creación y gestión de una base de datos en PostgreSQL que contiene dos esquemas distintos al esquema **public**.  
• Se implementa un sistema de roles con diferentes permisos (DDL, DML, Read, Write) y usuarios específicos asignados a cada esquema según reglas predefinidas.  
• El enfoque principal es la correcta administración de privilegios, propiedad de objetos y seguridad en la base de datos.

## Características
• Uso de dos esquemas personalizados: **esquema1** y **esquema2**.  
• Asignación de permisos específicos a roles y usuarios:  
   - rol_ddl: permisos de definición de estructuras (CREATE, ALTER, DROP).  
   - rol_dml: permisos de modificación de datos (INSERT, UPDATE, DELETE).  
   - rol_read: permisos de solo lectura (SELECT).  
   - rol_write: permisos de escritura (INSERT, UPDATE).  
• Control de ownership: las tablas y vistas son propiedad del rol **rol_ddl**, independientemente del usuario que las cree.  
• Inclusión de una vista en **esquema2** que obtiene estadísticas generales desde **esquema1**.

## Estructura del Proyecto
• Creación de roles y usuarios con privilegios diferenciados.  
• Creación de esquemas y asignación de ownership.  
• Definición de tablas en **esquema1** (ej. tabla **juegos**).  
• Definición de vistas en **esquema2** (ej. **view_estadisticas_generales**).  
• Asignación precisa de permisos para asegurar el principio de menor privilegio.  
• Revocación de permisos de otorgamiento para evitar delegación no autorizada.

## Configuración
• Asegurate de colocar las contraseñas correspondientes a los roles antes de ejecutar el script:
    CREATE ROLE user WITH LOGIN PASSWORD **---**;

## Requisitos
• PostgreSQL (versión 13 o superior recomendada).  
• Cliente como **DBeaver** o **pgAdmin** para ejecutar el script SQL.

## Instrucciones de Uso
1. Clona el repositorio:
    git clone https://github.com/Mikes1806/MAC_Bases_de_Datos.git
2. Ejecuta el script **roles.sql** en el cliente de tu preferencia (revisa que tengas los privilegios necesarios).