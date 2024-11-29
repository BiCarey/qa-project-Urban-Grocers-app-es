# Nombre y Cohorte
##### Bianca Tonantzin Chávez Sánchez, Cohorte 17

# Nombre del proyecto: Urban Grocers - Automatización de Pruebas para la Creación de Kits de Productos

Este proyecto automatiza las pruebas de la funcionalidad de creación de kits de productos en la aplicación Urban Grocers. Se enfoca específicamente en validar el campo name en la solicitud de creación de un kit personal.
### Requisitos previos
1.  Tener acceso a la API de Urban Grocers.
2.  Configuración del entorno de pruebas en PyCharm (Python, bibliotecas requests y Pytest para la ejecución de pruebas).


### Pasos iniciales
**1. Crear un usuario o usuaria:**
Envía una solicitud POST a la API para registrar un nuevo usuario. Guarda el authToken proporcionado.

**2. Crear un kit personal:**
Envía una solicitud POST a la API utilizando el token de autenticación y el encabezado Authorization.
Este paso asegurará que los kits se creen en el contexto del usuario específico.

**3. Automatizar las pruebas:**
Implementa los casos de prueba definidos en la lista de comprobación.

### Lista de Comprobación de pruebas
A continuación, se presenta la lista de casos de prueba que valida el campo name durante la creación de kits

| No |  Descripción | ER             |
|--- |------------- |--------------- |
| 1  |El número permitido de caracteres (1): kit_body = { "name": "a"} |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud|
| 2  |El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} |Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud |
| 3  |El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" } |Código de respuesta: 400 |
| 4  |	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } |Código de respuesta: 400 |
| 5  |Se permiten caracteres especiales: kit_body = { "name": ""№%@"," } |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 6  |Se permiten espacios: kit_body = { "name": " A Aaa " } |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 7  |Se permiten números: kit_body = { "name": "123" } |Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 8  |El parámetro no se pasa en la solicitud: kit_body = { } |Código de respuesta: 400 |
| 9  |	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 } |Código de respuesta: 400 |


### Archivos del Proyecto

- **configuration.py:** Contiene la URL y rutas de solicitud.
- **sender_stand_request.py:** Contiene las dos solicitudes POST, una de ellas para la creación de cuentas y la otra para crear un kit.
- **data.py:** Contiene los cuerpos de de las solicitudes.
- **create_kit_name_kit_test.py:** Contiene los tests.
- **README.md:** Descripción del proyecto.
- - **.gitignore:** Contiene los archivos que deben ignorarse al subir el repositorio.
