from faster_whisper import WhisperModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from janome.tokenizer import Tokenizer
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from googletrans import Translator


# モデル初期化はグローバルに一度だけ（高速化）
whisper_model = WhisperModel("base", compute_type="int8")
def transcribe_audio(audio_path: str) -> str: 
    segments, _ = whisper_model.transcribe(audio_path)
    text = " ".join([seg.text for seg in segments])
    text = text.replace(" ","")
    #segments, _ = whisper_model.transcribe(audio_path)
    return text

def summarize_text(text: str) -> str:
    model_name = "csebuetnlp/mT5_multilingual_XLSum"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    text = text
    def split_sentences(text):
        sentences = text.split("。")
        return [s.strip() + "。" for s in sentences if s.strip()]
    sentences = split_sentences(text)
    selected_sentences = sentences
    preprocessed_text = " ".join(selected_sentences)
    inputs = tokenizer("summarize: " + preprocessed_text, return_tensors="pt", max_length=1024, truncation=True)
# 要約生成
    summary_ids = model.generate(
    inputs["input_ids"],
    max_length=256,
    min_length=30,
    num_beams=4,
    length_penalty=2.0,
    early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def translate_text(text: str) -> str:
    translator = Translator()
    translated = translator.translate(text,src = 'ja', dest = 'en')
    return translated.text 

