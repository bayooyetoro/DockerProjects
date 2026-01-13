docker image build -t python-script-image .

docker container run --name pycontainer -v $(pwd)/data:/app/data python-script-image

## To change my permission on the data folder
sudo chmod -R g+rw $(pwd)
sudo chgrp -R $USER $(pwd)
sudo chmod -R 770 $(pwd)