FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip
RUN apt-get install -y libffi6
RUN apt-get install -y libffi-dev
RUN apt-get install -y build-essential
RUN pip3 install flask
RUN pip3 install flask_sqlalchemy
RUN pip3 install psycopg2-binary
WORKDIR .
COPY . .
EXPOSE 5000
EXPOSE 15432
ENTRYPOINT ["python3","/Example/app.py"]

