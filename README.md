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
5. Visit the url at http://localhost:5000
![](https://github.com/WarrenTseng/whisper_simple_aiaa/blob/main/animation.gif)
