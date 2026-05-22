# Taller AWS - Sistemas Operativos 2026

## Estudiante
Ana Sofía

---

# Descripción del Proyecto

Este taller tiene como objetivo desplegar y configurar una aplicación FastAPI utilizando diferentes servicios de AWS:

- Amazon EC2
- Amazon RDS
- Amazon S3
- Docker
- Amazon ECR
- AWS Lambda

La aplicación desarrollada permite:

- Crear tablas en una base de datos MySQL RDS
- Subir imágenes a un bucket S3
- Consultar imágenes almacenadas
- Exponer endpoints mediante FastAPI
- Documentar automáticamente la API usando Swagger

---

# Tecnologías Utilizadas

- Python 3.11
- FastAPI
- Uvicorn
- Boto3
- MySQL
- Docker
- AWS EC2
- AWS RDS
- AWS S3
- AWS ECR
- AWS Lambda

---

# Estructura del Proyecto

```txt
TALLER-AWS-SO-ANASOFIA/
│
├── app/
│   ├── services/
│   └── main.py
│
├── screenshots/
│   ├── ec2/
│   ├── rds/
│   ├── s3/
│   ├── ecr/
│   └── lambda/
│
├── scripts/
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Configuración del Entorno Local

## Crear entorno virtual

```bash
python -m venv venv
```

## Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

# Instalación de Dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución Local

```bash
uvicorn app.main:app --reload
```

Acceder desde el navegador:

```txt
http://127.0.0.1:8000/docs
```

---

# Configuración de EC2

Se creó una instancia EC2 Ubuntu para desplegar la aplicación FastAPI.

## Configuraciones realizadas

- Creación de instancia EC2
- Configuración de Security Groups
- Instalación de Python
- Instalación de dependencias
- Ejecución de Uvicorn
- Configuración de systemd

## Evidencias

Las capturas se encuentran en:

```txt
screenshots/ec2/
```

---

# Configuración de RDS

Se configuró una base de datos MySQL utilizando Amazon RDS.

## Configuraciones realizadas

- Motor MySQL
- Endpoint público habilitado
- Configuración de Security Groups
- Acceso desde EC2
- Conexión mediante cliente MySQL

## Endpoint RDS

```txt
fastapi-db.cr8aaywioydt.us-east-2.rds.amazonaws.com
```

## Evidencias

Las capturas se encuentran en:

```txt
screenshots/rds/
```

---

# Configuración de S3

Se creó un bucket S3 para almacenar imágenes subidas desde la API.

## Bucket utilizado

```txt
user-1040033706-ueia-so
```

## Funcionalidades implementadas

- Subida de imágenes
- Consulta de imágenes
- Organización por usuario

## Evidencias

Las capturas se encuentran en:

```txt
screenshots/s3/
```

---

# Endpoints Implementados

## GET /

Endpoint principal para verificar el funcionamiento de la API.

### Respuesta

```json
{
  "mensaje": "Hola desde EC2 desde el repo"
}
```

---

## GET /create-table

Crea la tabla de imágenes en MySQL.

### Respuesta

```json
{
  "mensaje": "Tabla creada correctamente"
}
```

---

## POST /upload

Sube una imagen al bucket S3 y registra la información en MySQL.

### Parámetros

| Parámetro | Tipo |
|---|---|
| usuario | string |
| image | file |

### Respuesta

```json
{
  "mensaje": "Imagen subida correctamente"
}
```

---

## GET /image

Consulta información de una imagen almacenada.

### Parámetros

| Parámetro | Tipo |
|---|---|
| usuario | string |
| image_name | string |

---

# Dockerización

Se creó una imagen Docker para contenerizar la aplicación FastAPI.

## Construcción de imagen

```bash
docker build -t fastapi-aws .
```

## Ejecución del contenedor

```bash
docker run -p 8000:8000 fastapi-aws
```

---

# Publicación en Amazon ECR

Se creó un repositorio privado ECR llamado:

```txt
fastapi-aws
```

## Login en ECR

```bash
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 023202273167.dkr.ecr.us-east-2.amazonaws.com
```

## Tag de la imagen

```bash
docker tag fastapi-aws:latest 023202273167.dkr.ecr.us-east-2.amazonaws.com/fastapi-aws:latest
```

## Push de la imagen

```bash
docker push 023202273167.dkr.ecr.us-east-2.amazonaws.com/fastapi-aws:latest
```

## Evidencias

Las capturas se encuentran en:

```txt
screenshots/ecr/
```

---

# Despliegue en AWS Lambda

Se creó una función Lambda utilizando la imagen Docker almacenada en ECR.

## Configuraciones realizadas

- Creación de función Lambda
- Asociación de imagen ECR
- Configuración de Function URL
- Integración con CloudWatch

## Observaciones

La función Lambda fue creada correctamente y se logró asociar exitosamente con la imagen almacenada en Amazon ECR.

Durante la fase final de ejecución se presentó un error relacionado con el runtime y el entrypoint del contenedor utilizado en Lambda. Sin embargo, se completaron satisfactoriamente las siguientes actividades:

- Construcción de imagen Docker
- Publicación en Amazon ECR
- Creación de función Lambda
- Configuración de URL pública
- Integración con CloudWatch Logs

## Evidencias

Las capturas se encuentran en:

```txt
screenshots/lambda/
```

---

# Evidencias del Taller

Todas las capturas del proceso se encuentran organizadas en:

```txt
screenshots/
```

Separadas por servicio:

- ec2
- rds
- s3
- ecr
- lambda

---

# Repositorio GitHub

Repositorio utilizado para el desarrollo del taller:

```txt
https://github.com/TU-USUARIO/taller-aws-so-anasofia
```

---

# Conclusiones

- Se logró desplegar una aplicación FastAPI utilizando diferentes servicios AWS.
- Se integró almacenamiento S3 con base de datos MySQL RDS.
- Se realizó contenerización mediante Docker.
- Se publicó la imagen Docker en Amazon ECR.
- Se creó una función Lambda utilizando imágenes de contenedor.
- Se documentó todo el proceso mediante capturas de pantalla.

---

# Autor

Ana Sofía  
Sistemas Operativos - Taller AWS 2026  
Universidad EIA
