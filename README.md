# flask application for 0x2019.de


docker build -t python_flask_app .
docker run -it -d -rm --name running_app -p 5000:5000 -v "$PWD":/usr/src/app python_flask_app
