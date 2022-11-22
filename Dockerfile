FROM python:3.9

# Gdal install so that I don't have to do it on my machine
RUN apt-get update
RUN pip3 install setuptools==57.5.0
RUN apt-get install gdal-bin libgdal-dev python3-gdal  -y
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal
RUN pip install GDAL==3.2.0

COPY requirements.txt /
COPY manage.py /
COPY ./mysite.uwsgi.ini /

EXPOSE ${API_PORT}
ENV ENV=${ENV}
ENV PROJECT_HOME="/"

# uwsgi setup
#RUN apk add python3-dev build-base linux-headers pcre-dev libxml2-dev libxslt-dev
RUN python -m pip install uwsgi
RUN python -m pip install -r requirements.txt

RUN mkdir /LokimoTest
COPY ./LokimoTest /LokimoTest