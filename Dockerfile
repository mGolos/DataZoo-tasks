# base image
FROM continuumio/miniconda3

# exposing default port for streamlit
EXPOSE 8501

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
CMD streamlit run app.py

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
