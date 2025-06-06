from faster_whisper import WhisperModel
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor


# モデル初期化はグローバルに一度だけ（高速化）
whisper_model = WhisperModel("base", compute_type="int8")
#summarizer = pipeline("summarization", model="t5-small")

def transcribe_audio(audio_path: str) -> str:
    segments, _ = whisper_model.transcribe(audio_path)
    return " ".join([seg.text for seg in segments])

def summarize_text(text: str) -> str:
    auto_abstractor = AutoAbstractor()
    auto_abstractor.tokenizable_doc = MeCabTokenizer()
    auto_abstractor.delimiter_list = ["。", "\n"]
    abstractable_doc = TopNRankAbstractor()
    
    result_dict = auto_abstractor.summarize(text, abstractable_doc)
    sentences = result_dict["summarize_result"]
    
    # 空白・改行除去して整形
    clean = [s.strip() for s in sentences if s.strip()]
    return "。".join(clean) + "。"
