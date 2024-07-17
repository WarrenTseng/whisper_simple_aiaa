import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import os

class WhisperAIAA:
    def __init__(self, model_id='openai/whisper-large-v3', audio_folder=None):
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        model.to(self.device)

        processor = AutoProcessor.from_pretrained(model_id)

        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            max_new_tokens=128,
            chunk_length_s=30,
            batch_size=16,
            return_timestamps=True,
            torch_dtype=torch_dtype,
            device=self.device,
        )
        if audio_folder:
            self.audio_folder = audio_folder
            self.audio_datalist = [f for f in os.listdir(audio_folder) if '.wav' in f or 'm4a' in f]
            self.f_count = 0
        
    def _next(self):
        audio_file = self.audio_datalist[self.f_count]
        audio_path = os.path.join(self.audio_folder, audio_file)
        self.f_count += 1
        text = self.inference(audio_path)
        return audio_path, text
    
    def inference(self, audio_path):
        return self.pipe(audio_path)['text']
    
    def annotate(self, text, audio_path):
        with open(audio_path[:-4]+'.txt', 'w') as f:
            f.write(text)
    
    
    