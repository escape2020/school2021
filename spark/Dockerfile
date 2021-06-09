FROM jupyter/pyspark-notebook:spark-3.1.1
LABEL maintainer "peloton@lal.in2p3.fr"
ENV REFRESHED_AT 2021-06-08

# Add repo
WORKDIR /home/jovyan/work
ADD . .
ENV PYTHONPATH=$PYTHONPATH:/home/jovyan/work/python:${SPARK_HOME}/python/test_coverage
ENV PYTHONPATH=$PYTHONPATH:${SPARK_HOME}/python:${SPARK_HOME}/python/lib/py4j-0.10.9-src.zip
ENV COVERAGE_PROCESS_START=/home/jovyan/work/.coveragerc

USER root
RUN apt-get update \
     && apt-get install -y vim
USER jovyan

# Add dependencies
RUN pip install -r requirements.txt
RUN python config_rise.py

# This ARG is passed during the build
ARG PYSPARK_DRIVER_PYTHON
ENV PYSPARK_DRIVER_PYTHON=$PYSPARK_DRIVER_PYTHON


WORKDIR /home/jovyan/work
