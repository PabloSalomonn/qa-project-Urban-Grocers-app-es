# 🛒 Proyecto Urban Grocers API Automation 

Urban Grocers es una aplicación de servicios de entrega que permite a los usuarios realizar pedidos de productos de forma rápida y sencilla desde su dispositivo. La plataforma gestiona el proceso completo, desde la selección de productos hasta la confirmación del pedido.

🧪 Contenido del Proyecto

Este proyecto contiene la suite de pruebas automatizadas para la API de **Urban Grocers**, enfocada en garantizar la calidad y confiabilidad de sus principales funcionalidades.

El objetivo principal es validar el comportamiento del endpoint de creación de **kits personalizados**, asegurando que cumpla con las reglas de negocio definidas para el campo `name`.

🔍 Enfoque de pruebas

Se implementan pruebas de **caja negra**, centradas en evaluar cómo responde el sistema ante distintos tipos de entradas, sin considerar la lógica interna del código.

Las pruebas incluyen:

- **Valores límite**: validación de longitudes mínimas y máximas permitidas  
- **Tipos de datos**: verificación del comportamiento ante datos válidos e inválidos  
- **Caracteres especiales**: comprobación del manejo de símbolos y caracteres no estándar  
- **Casos positivos y negativos**: asegurando tanto el correcto funcionamiento como la correcta gestión de errores  

🎯 Objetivo

Garantizar que el endpoint procese correctamente las solicitudes de creación de kits y rechace aquellas que no cumplan con las restricciones establecidas, contribuyendo así a la estabilidad y robustez de la API.
🛠️ Tecnologías y Herramientas

El proyecto está construido utilizando herramientas modernas para el desarrollo y validación de APIs, priorizando simplicidad, escalabilidad y buenas prácticas de testing.

🐍 Lenguaje
- **Python 3.x**  
  Se utiliza como lenguaje principal por su legibilidad, versatilidad y amplio ecosistema de librerías orientadas a testing y automatización.

📚 Librerías
- **`requests`**  
  Permite realizar solicitudes HTTP de forma sencilla, facilitando la interacción con la API de Urban Grocers para enviar y validar peticiones.

- **`pytest`**  
  Framework de testing que se utiliza para estructurar, ejecutar y validar los casos de prueba. Proporciona una sintaxis clara, soporte para fixtures y reportes detallados.

🌐 Protocolo
- **REST API**  
  La comunicación con el sistema se basa en principios REST, utilizando métodos HTTP como:
  - `GET` para obtener información  
  - `POST` para crear recursos (como kits)  
  - `PUT/PATCH` para actualizaciones  
  - `DELETE` para eliminación de recursos  

🧩 Arquitectura
- **Modular**  
  El proyecto sigue una arquitectura modular que separa claramente las responsabilidades, facilitando el mantenimiento y la escalabilidad:

  - **Configuración**: manejo de URLs base, headers y parámetros globales  
  - **Datos de prueba**: inputs reutilizables para distintos escenarios  
  - **Lógica de envío**: funciones que encapsulan las solicitudes a la API  
  - **Tests**: casos de prueba organizados y desacoplados de la lógica principal  
