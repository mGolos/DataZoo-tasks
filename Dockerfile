# base image
# a little overkill but need it to install dot cli for dtreeviz
# FROM ubuntu:18.04

# # ubuntu installing - python, pip, cmake
# RUN apt-get update &&\
#     apt-get install python3.8 -y &&\
#     apt-get install python3-pip -y &&\
#     apt-get install cmake -y

# # exposing default port for streamlit
# EXPOSE 5000

# # making directory of app
# WORKDIR /streamlit-docker

# # copy over requirements
# COPY requirements.txt ./requirements.txt

# # install pip then packages
# RUN pip3 install Cython
# RUN pip3 install -r requirements.txt
# RUN conda install --yes --file requirements.txt

# base image
FROM continuumio/miniconda3

# exposing default port for streamlit
EXPOSE 5000

# making directory of app
WORKDIR /streamlit-docker

# copy over requirements
COPY environment.yml ./environment.yml

# install pip then packages
RUN conda env create -f environment.yml
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

# copying all files over
COPY . .

# cmd to launch app when container is run
CMD streamlit run app.py --server.port 5000

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit