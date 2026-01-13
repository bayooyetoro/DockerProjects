# To build the image 
docker image build -t my-nginx-app .

# run the image as container but container gets removed (--rm)
docker container run --name app-image --rm -d -p 8080:80 my-nginx-app 