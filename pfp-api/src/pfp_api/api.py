

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from .load import read
app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(description="A file read as bytes")):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile = File(description="A file read as UploadFile"),
):
    return {"filename": file.filename}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)