import os
import shutil
from urllib import request
from fastapi import FastAPI, File, UploadFile,Request
from fastapi.responses import HTMLResponse
from .load import read
app = FastAPI()
@app.get("/")
async def root():
    return{"Hello":"Universe"}
@app.post("/getproviderinfo")
async def getproviderinfo(info:Request):
    req_info =await info.json()
    return {
        "status":"Success",
        "data":req_info
    }
# @app.post("/files/")
# async def create_file(file: bytes = File(description="A file read as bytes")):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile = File(description="A file read as UploadFile"),):
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     filename = f'{dir_path}/uploads/test.json'
#     with open('test.json', 'wb') as buffer:
#         shutil.copyfileobj(file.file,buffer)
#     graph_read = read('test.json')
#     graph_read.serialize(format='json-ld', indent=4,destination="input_graph.json")
    
   
#     return {"filename": file.filename}

# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="file" type="file">
# <input type="submit">
# </form>
# <form action="/uploadfile/" enctype="multipart/form-data" method="post">
# <input name="file" type="file">
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)
