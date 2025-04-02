# Sistema de Gestión de Películas y Géneros

![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.x-lightgrey)
![MongoEngine](https://img.shields.io/badge/MongoEngine-0.24.0-green)

Aplicación web para la gestión de un catálogo de películas con sistema de autenticación de usuarios.

## Características Principales

### Módulo de Autenticación
- **Login/Logout**: Sistema seguro de autenticación
- **Registro de usuarios**: Con validación de datos
- **Protección de rutas**: Decorador `@login_required`

### Gestión de Películas
- CRUD completo de películas
- Relación con géneros
- Subida de imágenes
- Validación de datos

### Gestión de Géneros
- CRUD completo de géneros
- Validación de nombres únicos

## Estructura de Archivos
