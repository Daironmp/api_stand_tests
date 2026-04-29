# Proyecto Urban Grocers

Este proyecto contiene pruebas automatizadas para la API de Urban Grocers.  
El objetivo es validar la creación de usuarios y kits, especialmente el campo `name` en los kits.

## Tecnologías

- Python
- pytest
- requests

## Estructura del proyecto

- configuration.py → Contiene la URL del servidor y endpoints
- data.py → Contiene headers y cuerpos de las solicitudes
- sender_stand_request.py → Contiene las funciones para enviar requests
- create_kit_name_kit_test.py → Pruebas para la creación de kits
- create_user_test.py → Pruebas para la creación de usuarios

## Cómo ejecutar el proyecto

1. Instala las dependencias: pip install pytest requests
2. Inicia el servidor en TripleTen y copia la URL.
3. Pega esa URL en URL_SERVICE dentro de configuration.py.
4. Ejecuta: pytest create_kit_name_kit_test.py