from fastapi import FastAPI, UploadFile, File, Form
from step1_core import transcribe_audio, summarize_text , translate_text
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import shutil

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # 一時ファイルに保存
    with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    result = transcribe_audio(tmp_path)
    return {"transcript": result}

@app.post("/summarize")
async def summarize(text: str = Form(...)):
    try:
        print("受信テキスト:", text)
        summary = summarize_text(text)
        return {"summary": summary}
    except Exception as e:
        print("サーバー側でエラー:", e)
        return {"error": str(e)}
    
@app.post("/translate")
async def translate(text: str = Form(...)):
    try:
        print("受信テキスト", text)
        translate = translate_text(text)
        return {"translate":translate}
    except Exception as e:
        print("サーバー側でエラー:", e)
        return {"error": str(e)}    

