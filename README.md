Taller AWS - Sistemas Operativos 2026
Estudiante

Ana Sofía

Descripción del Proyecto

Este taller tiene como objetivo desplegar y configurar una aplicación FastAPI utilizando diferentes servicios de AWS:

EC2
RDS MySQL
S3
Docker
ECR
AWS Lambda

La aplicación permite:

Crear tablas en MySQL RDS
Subir imágenes a S3
Consultar imágenes almacenadas
Ejecutar una API FastAPI documentada con Swagger
Tecnologías utilizadas
Python 3.11
FastAPI
Uvicorn
Boto3
MySQL
Docker
AWS EC2
AWS RDS
AWS S3
AWS ECR
AWS Lambda
Estructura del proyecto
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
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
Configuración del entorno local
Crear entorno virtual
python -m venv venv
Activar entorno virtual
Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
Instalación de dependencias
pip install -r requirements.txt
Ejecución local
uvicorn app.main:app --reload

Acceder en:

http://127.0.0.1:8000/docs
Configuración de EC2

Se creó una instancia EC2 Ubuntu para desplegar la aplicación FastAPI.

Pasos realizados
Creación de instancia EC2
Configuración de Security Groups
Instalación de Python
Instalación de dependencias
Ejecución de Uvicorn
Configuración de systemd
Evidencias

Ubicadas en:

screenshots/ec2/
Configuración de RDS

Se configuró una base de datos MySQL en Amazon RDS.

Configuraciones realizadas
Motor MySQL
Security Group habilitado
Endpoint público
Usuario administrador
Conexión desde EC2
Endpoint RDS
fastapi-db.cr8aaywioydt.us-east-2.rds.amazonaws.com
Evidencias

Ubicadas en:

screenshots/rds/
Configuración de S3

Se creó un bucket S3 para almacenar imágenes.

Bucket utilizado
user-1040033706-ueia-so
Funcionalidades implementadas
Subida de imágenes
Consulta de imágenes
Organización por usuario
Evidencias

Ubicadas en:

screenshots/s3/
Endpoints implementados
GET /

Verifica funcionamiento de la API.

Respuesta
{
  "mensaje": "Hola desde EC2 desde el repo"
}
GET /create-table

Crea la tabla de imágenes en MySQL.

Respuesta
{
  "mensaje": "Tabla creada correctamente"
}
POST /upload

Sube una imagen a S3 y registra información en MySQL.

Parámetros
Parámetro	Tipo
usuario	string
image	file
Respuesta
{
  "mensaje": "Imagen subida correctamente"
}
GET /image

Consulta información de una imagen almacenada.

Parámetros
Parámetro	Tipo
usuario	string
image_name	string
Dockerización

Se creó una imagen Docker para contenerizar la aplicación.

Construcción de imagen
docker build -t fastapi-aws .
Ejecución del contenedor
docker run -p 8000:8000 fastapi-aws
Publicación en Amazon ECR

Se creó un repositorio privado ECR llamado:

fastapi-aws
Login en ECR
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 023202273167.dkr.ecr.us-east-2.amazonaws.com
Tag de la imagen
docker tag fastapi-aws:latest 023202273167.dkr.ecr.us-east-2.amazonaws.com/fastapi-aws:latest
Push de la imagen
docker push 023202273167.dkr.ecr.us-east-2.amazonaws.com/fastapi-aws:latest
Despliegue en AWS Lambda

Se creó una función Lambda utilizando la imagen almacenada en ECR.

Configuraciones realizadas
Creación de función Lambda
Asociación de imagen ECR
Configuración de Function URL
Integración con CloudWatch
Observaciones

La función fue creada exitosamente y se configuró una URL pública. Sin embargo, durante la ejecución se presentó un error de compatibilidad relacionado con el runtime y el entrypoint del contenedor en Lambda.

Aun así, se logró completar satisfactoriamente:

Construcción de imagen Docker
Publicación en ECR
Creación de Lambda
Configuración de URL pública
Integración con CloudWatch
Evidencias

Ubicadas en:

screenshots/lambda/
Evidencias del taller

Todas las capturas del proceso se encuentran organizadas en:

screenshots/

Separadas por servicio:

ec2
rds
s3
ecr
lambda
Repositorio GitHub

Repositorio utilizado para el desarrollo del taller:

https://github.com/TU-USUARIO/taller-aws-so-anasofia
Conclusiones
Se logró desplegar una aplicación FastAPI utilizando servicios AWS.
Se integró almacenamiento S3 con base de datos MySQL RDS.
Se realizó contenerización con Docker.
Se publicó la imagen en Amazon ECR.
Se creó una función Lambda utilizando imágenes de contenedor.
Se documentó todo el proceso mediante capturas de pantalla.
Autor

Ana Sofía
Sistemas Operativos - Taller AWS 2026
Universidad EIA
