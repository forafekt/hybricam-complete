#!/bin/bash
docker build -t web:latest .
docker run -d --name your-app -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest