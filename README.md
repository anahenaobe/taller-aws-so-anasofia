# Taller AWS - Sistemas Operativos

- Ana Sofía Henao Bedoya

El desarrollo incluye:

- Gestión de archivos con Amazon S3
- Automatización mediante AWS CLI y boto3
- Desarrollo de API REST con FastAPI
- Despliegue de aplicaciones en Amazon EC2
- Persistencia de datos con Amazon RDS
- Contenerización utilizando Docker
- Publicación de imágenes en Amazon ECR
- Despliegue serverless mediante AWS Lambda

# Tecnologías utilizadas

- Python
- FastAPI
- boto3
- AWS CLI
- Docker
- GitHub
- Amazon S3
- Amazon EC2
- Amazon RDS
- Amazon ECR
- AWS Lambda

# Estructura del proyecto

```bash
.
├── app
│   ├── main.py
│   ├── database
│   ├── models
│   ├── routes
│   └── services
│
├── scripts
│
├── screenshots
│   ├── s3
│   ├── ec2
│   ├── ecr
│   ├── lambda
│   └── rds
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

# Parte 1 - Gestión de archivos en Amazon S3

## Creación del bucket

Se creó el bucket:

```bash
user-1040033706-ueia-so
```

## Operaciones usando AWS CLI

### Subida de archivos

```bash
aws s3 cp a.txt s3://user-1040033706-ueia-so/
aws s3 cp b.txt s3://user-1040033706-ueia-so/
aws s3 cp c.txt s3://user-1040033706-ueia-so/
```

### Verificación de archivos

```bash
aws s3 ls s3://user-1040033706-ueia-so/
```

### Descarga de archivos

```bash
aws s3 cp s3://user-1040033706-ueia-so/ descarga_final/ --recursive
```

### Manejo de múltiples archivos

Para la gestión de múltiples archivos se utilizaron comandos automatizados y la opción `--recursive`, permitiendo realizar cargas y descargas masivas de manera eficiente.

## Operaciones usando boto3

Se desarrolló un script en Python utilizando boto3 para:

- Crear archivos de prueba
- Subir archivos automáticamente al bucket
- Verificar los objetos almacenados
- Descargar archivos en otra carpeta local

### Ejecución del script

```bash
python s3_test.py
```

# Parte 2 - Despliegue de FastAPI en Amazon EC2

Se realizó el despliegue de una aplicación FastAPI en una instancia EC2 utilizando Linux y configuraciones de red necesarias para permitir el acceso mediante IP pública.

## Actividades realizadas

- Creación de instancia EC2
- Clonación del repositorio desde GitHub
- Instalación de dependencias
- Configuración de puertos y permisos
- Ejecución de la aplicación FastAPI
- Configuración de daemon/systemd
- Configuración de Security Groups

# Parte 3 - Desarrollo y despliegue de aplicación

La aplicación desarrollada permite:

## Endpoint POST

- Recepción de usuario e imagen
- Validación de formatos PNG/JPG/JPEG
- Almacenamiento de imágenes en Amazon S3
- Registro de información en Amazon RDS

## Endpoint GET

- Consulta de imágenes almacenadas
- Obtención de URL prefirmada
- Consulta de fecha de almacenamiento

# Contenerización

La aplicación fue contenerizada utilizando Docker.

## Comandos utilizados

### Construcción de imagen

```bash
docker build -t aws-fastapi .
```

### Ejecución del contenedor

```bash
docker run -p 8000:8000 aws-fastapi
```

# Publicación en Amazon ECR

Se creó un repositorio en Amazon ECR para almacenar la imagen Docker de la aplicación.

# Despliegue en AWS Lambda

La aplicación fue desplegada utilizando AWS Lambda mediante imágenes almacenadas en Amazon ECR.

También se configuró una URL pública para invocación.

# Evidencias

Las evidencias y capturas del desarrollo se encuentran almacenadas en:

```bash
screenshots/
```

# Repositorio GitHub

El proyecto completo, incluyendo código fuente, scripts, Dockerfile, configuraciones y documentación, se encuentra versionado en GitHub.
