

export DOCKER_HOST=tcp://192.168.99.100:2376
export DOCKER_CERT_PATH=/Users/okkeharsta/.docker/machine/machines/dinghy
export DOCKER_TLS_VERIFY=1
export DOCKER_MACHINE_NAME=dinghy

https://www.virtualbox.org/manual/ch06.html#network_hostonly

docker-machine ls
docker-machine stop dinghy

First, run:

  eval "$(dinghy env)"

This will set up environment variables for docker to work with the dinghy VM.

Running Canvas:

  docker-compose up -d
  open http://canvas.docker

https://timonweb.com/django/https-django-development-server-ssl-certificate/


docker ps
docker exec -it <container name> /bin/bash
docker logs --follow <container ID>

ngrok http --region=eu --hostname=okke.harsta.eu.ngrok.io 9001
ngrok http --region=eu --hostname=okke.harsta.eu.ngrok.io 8000
student1
secret123

oharsta+student@zilverline.com
oharsta+teacher@zilverline.com
-----
./script/docker_dev_setup.sh
-----
docker-compose down
docker-machine stop dinghy

-----
canvas
course navigation - deeplink
nounce validation

The developer key must be set to PUBLIC in order to retrieve email, given_name, family_name


