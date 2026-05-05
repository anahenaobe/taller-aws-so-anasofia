# ☁️ Taller AWS - Sistemas Operativos
Proyecto que implementa servicios en la nube utilizando AWS y una aplicación desarrollada en FastAPI.
## 🚀 Tecnologías utilizadas
* Amazon S3
* Amazon EC2
* Amazon RDS
* AWS Lambda
* Amazon ECR
* Docker
* FastAPI
* Python (boto3, uvicorn)
---
## 📂 Funcionalidades
### 1. Gestión de archivos en S3
* Creación de bucket
* Subida y descarga de archivos (AWS CLI y boto3)
* Manejo de múltiples archivos
### 2. Despliegue en EC2
* Configuración de instancia
* Ejecución de aplicación FastAPI
* Acceso público mediante IP
### 3. API con FastAPI
* Endpoint POST:
  * Recibe usuario e imagen (PNG/JPG)
  * Valida formato
  * Almacena en S3
  * Registra en RDS
* Endpoint GET:
  * Consulta imágenes por usuario
  * Retorna URL prefirmada
  * Muestra fecha de almacenamiento
### 4. Contenerización
* Creación de imagen Docker
* Ejecución local con Docker
### 5. Despliegue en la nube
* Publicación en Amazon ECR
* Implementación en AWS Lambda
---
## ⚙️ Instalación y ejecución
### 1. Clonar repositorio
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```
### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Ejecutar aplicación
```bash
uvicorn main:app --reload
```
## 🐳 Docker
### Construir imagen
```bash
docker build -t aws-fastapi-app .
```
### Ejecutar contenedor
```bash
docker run -p 8000:8000 aws-fastapi-app
```
## 🔐 Configuración
Se recomienda usar variables de entorno para credenciales AWS:
```bash
AWS_ACCESS_KEY_ID=tu_key
AWS_SECRET_ACCESS_KEY=tu_secret
AWS_DEFAULT_REGION=tu_region
```
## 📸 Evidencias
El repositorio incluye capturas de:
* Configuración en AWS
* Ejecución en EC2
* Funcionamiento de la API
---
## 👩‍💻 Autor
Ana Sofía Henap Bedoya
Universidad EIA
