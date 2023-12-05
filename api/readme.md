# Backend de Predicción de Precios de Vuelos

Este es el backend para una aplicación de predicción de precios de vuelos que utiliza Django y una API GraphQL para la administración de usuarios y para proporcionar predicciones de precios mediante un modelo de inteligencia artificial.

## Características

- API GraphQL para la gestión de usuarios.
- Modelo de inteligencia artificial para la predicción de precios de vuelos.
- Integración con la aplicación Flutter en el frontend.

## Estructura del Proyecto

- `flight/`: Aplicación Django con toda la lógica relacionada con la predicción de vuelos.
- `proyecto_final_fer_vrgs/`: Configuración central del proyecto Django.
- `manage.py`: Utilidad de línea de comandos para interactuar con el proyecto Django.
- `requirements.txt`: Dependencias necesarias para el proyecto.

## Comenzando

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para fines de desarrollo y pruebas.

### Prerrequisitos

Necesitarás Python 3 y pip instalados en tu máquina local. Además, es recomendable usar un entorno virtual para instalar las dependencias.

### Instalación

Instala las dependencias del proyecto con pip:
```bash
pip install -r requirements.txt
```

Realiza las migraciones necesarias para preparar la base de datos:
```bash
python manage.py migrate
```

### Ejecución
Para iniciar el servidor de desarrollo, ejecuta:
```bash
python manage.py runserver
```

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.

## Autor
Fernando Munoz Herradura