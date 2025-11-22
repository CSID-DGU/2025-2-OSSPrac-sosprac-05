FROM tiangolo/uwsgi-nginx-flask:latest
ENV MODULE_NAME="team"
COPY . /app
