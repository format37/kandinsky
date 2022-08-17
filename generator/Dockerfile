FROM huggingface/transformers-pytorch-gpu:4.21.1
# FROM huggingface/transformers-pytorch-gpu
# FROM nvidia/cuda:11.6.2-cudnn8-devel-ubuntu20.04
WORKDIR /app

RUN pip3 install --upgrade pip
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY dalle_fixes/__init__.py /usr/local/lib/python3.8/dist-packages/rudalle/dalle/
# RUN apt-get install wget

# Download mujoco
#&& mkdir /root/.mujoco \
#&& cd /root/.mujoco \
#&& wget -qO- 'https://github.com/deepmind/mujoco/releases/download/2.1.0/mujoco210-linux-x86_64.tar.gz' | tar -xzvf -


# RUN mkdir /app/data & \
#     mkdir /app/data/models
# Download model to model/ directory
# RUN wget http://95.165.139.53:42080/models/kandinsky_cache.tar.gz
# RUN wget http://95.165.139.53:42080/index.tar.gz
# archive index.html to index.tar.gz
# RUN tar -czvf index.tar.gz -C /app/data/index.html
# RUN mkdir /app/data \
# && mkdir /app/data/models \
# && cd /app/data/models \
# && wget 'http://95.165.139.53:42080/index.tar.gz'
# && tar -xpJf index.tar.gz
# && wget -qO- 'http://95.165.139.53:42080/index.tar.gz' | tar -xzvf - \

# Extract model to /app/data/models/ directory
# RUN tar -xvf /app/kandinsky_cache.tar.gz -C /app/data/models/
# remove model archive
#RUN rm /app/model/kandinsky_cache.tar.gz

COPY inference.py /app
COPY loop.py /app
ENTRYPOINT ["python3"]
CMD ["loop.py"]