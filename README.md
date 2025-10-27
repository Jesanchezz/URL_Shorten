# Microservicio Acortador de URLs
Este proyecto es un microservicio desarrollado con FastAPI que permite acortar URLs y redirigir a la URL original mediante una clave corta. Utiliza MariaDB como base de datos y SQLAlchemy para la gestión de modelos y operaciones de persistencia.

## Tabla de contenido
- [Características](#características)
- [Funcionalidades principales](#funcionalidades-principales)
- [Tecnologías utilizadas](#tecnologías-utilizadas)

## Características

* API REST con dos endpoints principales:

    - POST /shorten: Crea una URL acortada a partir de una URL original.
    - GET /redirect/{short_url}: Busca la URL original asociada a la clave corta y redirige al usuario.

    El prefijo de las rutas definido es: "/api-url"

* Gestión de base de datos con SQLAlchemy.
* Validación para evitar duplicados.
* Redirección automática a la URL original.

## Funcionalidades principales
El microservicio cuenta con cuatro funciones clave:

* Generar URL acortada: Crea una clave única para representar la URL original.
* Verificar duplicados: Comprueba si la URL original ya ha sido registrada previamente.
* Registrar URL: Guarda en la base de datos la URL original junto con su versión acortada.
* Buscar y redirigir: Recupera la URL original a partir de la clave corta y realiza la redirección.

## Tecnologías utilizadas
* FastAPI: Framework moderno y rápido para construir APIs con Python.
* MariaDB: Base de datos relacional utilizada para almacenar las URLs.
* SQLAlchemy: ORM para manejar la interacción con la base de datos.