from fastapi import FastAPI, File, UploadFile, HTTPException, Request
import os
import img2pdf
from utils.timestamp import generate_timestamp

app = FastAPI()

# Buat direktori jika belum ada
output_dir = "public/convert/image/pdf"
os.makedirs(output_dir, exist_ok=True)

@app.post("/api/convert/image2pdf")
async def convert_image_to_pdf(request: Request, file: UploadFile = File(...)):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")

    try:
        timestamp = generate_timestamp()
        filename = f"{file.filename.rsplit('.', 1)[0]}_{timestamp}.pdf"
        output_path = os.path.join(output_dir, filename)

        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(await file.read()))

        path = f"/{output_dir}/{filename}"
        fullPath = f"{request.url.scheme}://{request.client.host}:{request.url.port}{path}"
        return {"path": path, "fullPath": fullPath}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Untuk menghidupkan static file
from fastapi.staticfiles import StaticFiles

app.mount("/public", StaticFiles(directory="public"), name="public")

# Tambahkan endpoint /ping
@app.get("/ping")
async def ping():
    return {"status": 200, "message": "pong"}
