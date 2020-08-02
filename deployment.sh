#!/bin/bash
sudo docker build -t web:latest .
sudo docker build -t registry.heroku.com/hybricam/web .
sudo docker push registry.heroku.com/hybricam/web
sudo heroku container:release -a hybricam web
#heroku run -a hybricam python manage.py collectstatic --noinput
#sudo heroku run -a hybricam python manage.py makemigrations
#sudo heroku run -a hybricam python manage.py migrate
#heroku run -a hybricam redis-server --daemonize yes
#heroku run -a hybricam python manage.py runworker channels
