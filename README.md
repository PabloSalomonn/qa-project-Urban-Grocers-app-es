# 🛒 Proyecto Urban Grocers API Automation 

Urban Grocers es una aplicación de servicios de entrega que permite a los usuarios realizar pedidos de productos de forma rápida y sencilla desde su dispositivo. La plataforma gestiona el proceso completo, desde la selección de productos hasta la confirmación del pedido.

🧪 Contenido del Proyecto

Este proyecto contiene la suite de pruebas automatizadas para la API de **Urban Grocers**, enfocada en validar el cumplimiento de los requisitos funcionales del backend relacionados con la gestión de usuarios, pedidos, kits personalizados y servicios de entrega.

El enfoque principal está en asegurar que los endpoints respondan correctamente bajo distintos escenarios, respetando las reglas de negocio, validaciones de datos y lógica de integración entre servicios.



🔍 Alcance de las pruebas

Las pruebas cubren los siguientes módulos principales del sistema:

👤 Autorización y datos del usuario
- Validación del registro de usuarios mediante `POST /api/v1/users`
- Verificación de campos obligatorios y opcionales:
  - Nombre (obligatorio)
  - Teléfono (obligatorio)
  - Dirección (obligatorio)
  - Correo electrónico (opcional)
  - Comentarios (opcional)
- Validación de restricciones:
  - Longitud de campos
  - Tipos de caracteres permitidos
- Comprobación de que usuarios registrados pueden reutilizar y actualizar sus datos


🛒 Carrito de compras y pedidos

- Creación y gestión del carrito (`POST /api/v1/orders`)
- Validación de:
  - Agregado y eliminación de productos
  - Cálculo del total del pedido
  - Inclusión del costo de entrega
- Verificación del comportamiento cuando:
  - No se especifica hora de entrega (uso de hora del servidor)
  - Se modifican productos del carrito
  - 

🧺 Kits personalizados

- Creación de kits (`POST /api/v1/kits`)
- Validación del campo `name`:
  - Solo caracteres permitidos
  - Longitud entre 2 y 15 caracteres
- Restricciones:
  - Máximo 30 productos por kit
- Operaciones cubiertas:
  - Crear, editar, eliminar y consultar kits
  - Agregar y eliminar productos dentro de un kit
- Manejo de errores ante datos inválidos


🚚 Servicios de entrega
- Validación de selección automática del servicio más económico disponible
- Verificación de reglas de negocio:
  - Disponibilidad según horario
  - Restricciones por peso y cantidad de productos
- Cálculo del costo de entrega:
  - $5 si se incumple alguna condición:
    - Exceso de peso
    - Exceso de cantidad
    - Pedido menor a $7
  - En caso contrario, envío gratuito
- Pruebas de integración con distintos servicios:
  - JSON, XML y SOAP


🏬 Almacenes (Warehouses)

- Validación de selección automática del almacén:
  - Con stock disponible
  - Abierto en el horario del pedido
  - Opción más económica
- Verificación de disponibilidad completa de productos
- Pruebas de endpoints:
  - Consulta de almacenes
  - Validación de stock


🧠 Lógica de negocio validada

Las pruebas aseguran el correcto funcionamiento de reglas clave como:

- No permitir pedidos con campos obligatorios incompletos  
- Validación estricta de formatos de entrada  
- Selección óptima de servicios (delivery y almacén)  
- Cálculo correcto del costo total del pedido  
- Consistencia en la gestión de múltiples pedidos por usuario  

🧪 Enfoque de testing

Se utiliza un enfoque de **caja negra**, evaluando el sistema desde la perspectiva del usuario y validando entradas y salidas sin depender de la implementación interna.

Incluye:
- Casos positivos (datos válidos)  
- Casos negativos (datos inválidos)  
- Valores límite  
- Pruebas de integración entre servicios  

🎯 Objetivo

Garantizar que la API de **Urban Grocers** sea robusta, consistente y confiable, validando tanto las funcionalidades individuales como la interacción entre los distintos componentes del sistema.

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
