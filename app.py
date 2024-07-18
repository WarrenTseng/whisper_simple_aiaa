from flask import Flask, render_template, request
from whisper_aiaa import WhisperAIAA
import os
import time

app = Flask(__name__)

wa = WhisperAIAA(audio_folder="dataset")
cmd = 'cp -r dataset static/'
os.system(cmd)
audio_path = ''
text = ''
text_input = 'Enter text here'

@app.route('/', methods=['GET', 'POST'])

def index():
    text_display_1 = ''
    text_display_2 = ''
    global audio_path
    global text
    global text_input
    if request.method == 'POST':
        text_input = request.form['text_input']
        if 'next' in request.form:
            audio_path, text = wa._next()
            text_display_1 = audio_path
            text_display_2 = text
            text_input = text_display_2
            # cmd = 'cp '+audio_path+' static/audio.wav'
            # cmd = 'cp '+audio_path+' static/'
            # os.system(cmd)
            time.sleep(0.2)
        elif 'annotate' in request.form:
            wa.annotate(text_input, audio_path)
    return render_template('index.html', text_display_1=text_display_1, text_display_2=text_display_2, text_input=text_input, audio_path=audio_path)

if __name__ == '__main__':
    app.run(debug=True)
