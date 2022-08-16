FROM huggingface/transformers-pytorch-gpu:4.21.1
# FROM huggingface/transformers-pytorch-gpu
# FROM nvidia/cuda:11.6.2-cudnn8-devel-ubuntu20.04
WORKDIR /app

RUN pip3 install --upgrade pip
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY dalle_fixes/__init__.py /usr/local/lib/python3.8/dist-packages/rudalle/dalle/
RUN apt-get install wget
# Download model to model/ directory
RUN wget http://95.165.139.53:42080/models/kandinsky_cache.tar.gz -O /app/data/models/kandinsky_cache.tar.gz
# Extract model to model/ directory
RUN tar -xvf /app/model/kandinsky_cache.tar.gz -C /app/model/
# remove model archive
#RUN rm /app/model/kandinsky_cache.tar.gz

COPY inference.py /app
COPY loop.py /app
ENTRYPOINT ["python3"]
CMD ["loop.py"]