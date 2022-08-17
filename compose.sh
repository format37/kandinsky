# mkdir -p data/requests
mkdir -p data/generated
mkdir -p data/models
# if path data/models/rudalle is not exist, then download the model
if [ ! -d "data/models/Kandinsky" ]; then
    wget 'http://95.165.139.53:42080/kandinsky_cache.tar.gz' -O data/models/kandinsky_cache.tar.gz
    # unpack the model
    tar -xvf data/models/kandinsky_cache.tar.gz -C data/models/
    # remove the model archive
    rm data/models/kandinsky_cache.tar.gz
fi
# mkdir -p data/upscaled
sudo docker-compose up --build -d
