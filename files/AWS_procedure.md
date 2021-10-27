* Prerequisites:
  ```bash
  sudo yum update -y
  sudo yum install git -y
  sudo yum install docker -y
  sudo service docker start
  ```
  (or)
  ```bash
  sudo apt-get update
  sudo apt-get install docker -y
  sudo apt-get install docker.io -y
  sudo systemctl start docker
  ```
* Git:
  ```bash
  git clone https://github.com/mGolos/DataZoo-tasks.git
  cd DataZoo-tasks/
  ```
* Docker:
  ```bash
  sudo docker image build -t streamlit:app .
  sudo docker container ls
  sudo docker container run -p 8501:8501/tcp
  ```
* Access `sudo docker exec -it {containe_name} bash`
