#!/bin/bash
#docker build -t web:latest .
sudo docker build -t registry.heroku.com/your-app/web .
sudo docker push registry.heroku.com/your-app/web
sudo heroku container:release -a your-app web
#heroku run -a your-app python manage.py collectstatic --noinput
#sudo heroku run -a your-app python manage.py makemigrations
#sudo heroku run -a your-app python manage.py migrate
#heroku run -a your-app redis-server --daemonize yes
#heroku run -a your-app python manage.py runworker channels
