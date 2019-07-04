# Flask-app for a Docker exercise

The application is a tiny Flask-framework based message wall, that lets users write messages via a form and stores messages into a database. It uses SQLAlchemy and WTForms. It was pushed to DockerHub as part of an exercise. After launching the application, it can be accessed via browser in port 5000, for instance by navigating to "localhost:5000".

To launch the application, you need a Dockerfile. The file should have the following content:

```
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/anketola/flask-docker.git

EXPOSE 5000

WORKDIR /flask-docker
RUN apt-get install python3 -y
RUN apt-get install python3-venv -y
RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"
RUN apt install python3-pip -y
RUN apt install python3-dev -y
RUN pip3 install -r requirements.txt

CMD python3 run.py
```

To run the application with Docker, in the folder with the dockerfile, type the following command:

```
docker pull aketla/docker-exercise-flask
docker run -p 5000:5000 docker-exercise-flask
```

The application should be now operational and accessible through port 5000.
