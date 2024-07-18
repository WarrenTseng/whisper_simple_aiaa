This repo is a simple implementation of the model from https://huggingface.co/openai/whisper-large-v3 for audio ai-assisted annotation
</br>
### Environment
```
nvcr.io/nvidia/nemo:24.05.01
```
### Steps
1. Pull the docker image and start the environment
```
docker run -it --rm -p 5000:5000 --gpus=all --shm-size=2g -v /HOST/WORKSPACE:/workspace -w /workspace nvcr.io/nvidia/nemo:24.05.01
```
2. Install the pre-requests
```
pip install --upgrade pip
pip install --upgrade git+https://github.com/huggingface/transformers.git accelerate
```
3. Clone this repo
```
git clone https://github.com/WarrenTseng/whisper_simple_aiaa
cd whisper_simple_aiaa
```
4. Start the Flask server
```
flask run
```
5. Visit the url at localhost:5000 (<a href="https://drive.google.com/file/d/1LWyi1ixUPoGWgPEcsyBtTS5m4KIaiDu0/view?usp=sharing">Demo recording</a>)
![](https://github.com/WarrenTseng/whisper_simple_aiaa/blob/main/animation.gif)

6. The annotated files will be at the same folder as audio files
