# Taller AWS - Sistemas Operativos 2026

## Estudiante
Ana Sofía

---

# Descripción del Proyecto

Este taller tiene como objetivo desplegar y configurar una aplicación FastAPI utilizando diferentes servicios de AWS:

- EC2
- RDS MySQL
- S3
- Docker
- ECR
- AWS Lambda

La aplicación permite:

- Crear tablas en MySQL RDS
- Subir imágenes a S3
- Consultar imágenes almacenadas
- Ejecutar una API FastAPI documentada con Swagger

---

# Tecnologías utilizadas

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

# Estructura del proyecto

TALLER-AWS-SO-ANASOFIA/

├── app/

│ ├── services/

│ └── main.py

├── screenshots/

│ ├── ec2/

│ ├── rds/

│ ├── s3/

│ ├── ecr/

│ └── lambda/

├── scripts/

├── requirements.txt

├── Dockerfile

├── README.md

└── .gitignore

---

# Configuración del entorno local

## Crear entorno virtual

```bash
python -m venv venv
