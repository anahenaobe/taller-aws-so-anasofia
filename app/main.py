from fastapi import FastAPI, UploadFile, File, HTTPException
import boto3
import pymysql
from datetime import datetime

app = FastAPI()

# =========================
# CONFIG S3
# =========================
BUCKET_NAME = "user-1040033706-ueia-so"

s3 = boto3.client("s3")

# =========================
# CONFIG RDS
# =========================
db = pymysql.connect(
    host="fastapi-db.cr8aaywioydt.us-east-2.rds.amazonaws.com",
    user="admin",
    password="Paloma1101",
    database="fastapidb",
    port=3306
)

# =========================
# HOME
# =========================
@app.get("/")
def read_root():
    return {"mensaje": "FastAPI funcionando en AWS"}

# =========================
# CREAR TABLA
# =========================
@app.get("/create-table")
def create_table():

    cursor = db.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS images (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usuario VARCHAR(255),
        image_name VARCHAR(255),
        s3_path TEXT,
        created_at DATETIME
    )
    """

    cursor.execute(query)
    db.commit()

    return {"mensaje": "Tabla creada correctamente"}

# =========================
# SUBIR IMAGEN
# =========================
@app.post("/upload")
async def upload_image(
    usuario: str,
    image: UploadFile = File(...)
):

    allowed_types = ["image/png", "image/jpeg"]

    if image.content_type not in allowed_types:
        raise HTTPException(
            status_code=415,
            detail="Formato no permitido"
        )

    file_key = f"{usuario}/{image.filename}"

    # subir imagen a S3
    s3.upload_fileobj(
        image.file,
        BUCKET_NAME,
        file_key
    )

    s3_url = f"s3://{BUCKET_NAME}/{file_key}"

    # guardar en RDS
    cursor = db.cursor()

    query = """
    INSERT INTO images(usuario, image_name, s3_path, created_at)
    VALUES(%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            usuario,
            image.filename,
            s3_url,
            datetime.now()
        )
    )

    db.commit()

    return {
        "mensaje": "Imagen subida correctamente",
        "ruta_s3": s3_url
    }

# =========================
# OBTENER IMAGEN
# =========================
@app.get("/image")
def get_image(
    usuario: str,
    image_name: str
):

    cursor = db.cursor()

    query = """
    SELECT s3_path, created_at
    FROM images
    WHERE usuario=%s
    AND image_name=%s
    """

    cursor.execute(
        query,
        (usuario, image_name)
    )

    result = cursor.fetchone()

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Imagen no encontrada"
        )

    s3_path, created_at = result

    key = f"{usuario}/{image_name}"

    # generar URL prefirmada
    url = s3.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": BUCKET_NAME,
            "Key": key
        },
        ExpiresIn=3600
    )

    return {
        "usuario": usuario,
        "imagen": image_name,
        "fecha": str(created_at),
        "url": url
    }