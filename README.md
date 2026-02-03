# 🛒 Urban Grocers API Automation - Sprint 8

Este proyecto contiene la suite de pruebas automatizadas para la API de **Urban Grocers**. El enfoque principal es la validación del endpoint de creación de "Kits" personales, evaluando las restricciones del campo `name` mediante pruebas de caja negra (limites, tipos de datos y caracteres).

---

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.x
* **Librerías:** `requests`, `pytest`
* **Protocolo:** REST API
* **Arquitectura:** Modular (Separación de configuración, datos y lógica de envío)

---

## 📂 Estructura del Proyecto
* **`configuration.py`**: Contiene la URL base del servidor y las rutas (endpoints) necesarias.
* **`data.py`**: Almacena los diccionarios con cuerpos de solicitud (payloads) y encabezados.
* **`sender_stand_request.py`**: Gestiona las solicitudes HTTP (POST) y la lógica de autenticación (auth_token).
* **`create_kit_name_kit_test.py`**: Contiene las funciones de aserción (`positive_assert`, `negative_assert`) y los 9 casos de prueba.
* **`.gitignore`**: Define los archivos que no deben subirse al repositorio (como cachés de Python).

---

## 📋 Lista de Comprobación de Pruebas (Checklist)
Se han automatizado los siguientes escenarios para el campo `name` del Kit:

| № | Descripción | Resultado Esperado |
|---|---|---|
| 1 | El número permitido de caracteres (1) | Código 201 + Nombre coincidente |
| 2 | El número permitido de caracteres (511) | Código 201 + Nombre coincidente |
| 3 | El número de caracteres es menor que el permitido (0) | Código 400 |
| 4 | El número de caracteres es mayor que el permitido (512) | Código 400 |
| 5 | Se permiten caracteres especiales | Código 201 |
| 6 | Se permiten espacios | Código 201 |
| 7 | Se permiten números | Código 201 |
| 8 | El parámetro `name` no se pasa en la solicitud | Código 400 |
| 9 | Se pasa un tipo de parámetro diferente (número) | Código 400 |

---

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone git@github.com:tu-usuario/qa-project-Urban-Grocers-app-es.git
   cd qa-project-Urban-Grocers-app-es
Instalar dependencias:

Bash
pip install requests pytest
Configurar el servidor:

Inicia el servidor de Urban Grocers desde la plataforma de TripleTen.

Copia la URL generada y actualiza la variable URL_SERVICE en el archivo configuration.py.

Ejecutar las pruebas:

Bash
pytest create_kit_name_kit_test.py
💡 Detalles de la Implementación
Uso de copy(): Para evitar la mutación de datos de origen en data.py, se utiliza el método .copy() en cada prueba antes de modificar el cuerpo de la solicitud.

Autenticación Dinámica: Se implementó la función get_new_user_token() que registra un usuario nuevo y devuelve un authToken único para cada ejecución de kit, garantizando la independencia de las pruebas.

Aserciones Robustas: Las pruebas positivas no solo validan el código 201, sino que verifican que el nombre devuelto en el JSON sea exactamente el enviado.
