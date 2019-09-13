docker build -t testapp .
docker run \
 -p 3001:3001 \
 -v $PWD:/home/app \
 -it --rm testapp
