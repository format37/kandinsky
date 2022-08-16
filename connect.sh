# get id of container with name kandinsky_generator_1 and store to variable id
id=$(docker ps -a | grep kandinsky_generator_1 | awk '{print $1}')
# connect bash to container with id $id
docker exec -it $id /bin/bash