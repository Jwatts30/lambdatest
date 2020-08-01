FROM ubuntu:16.04

RUN apt-get update && \
  apt-get install -y python-setuptools python3-pip wget curl

ENV url www.facebook.com

#install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable


#install chrome driver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
ENV DISPLAY=:99

# Upgrade pip
RUN pip3 install --upgrade pip
ARG USER=jannat
ARG V_ENV=boto3venv

USER root

ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

# create user
RUN useradd -ms /bin/bash ${USER}
USER ${USER}
WORKDIR /home/${USER}

# add credentials
#RUN mkdir -p /home/${USER}/.aws
#COPY aws/credentials /home/${USER}/.aws

RUN pip3 install virtualenv --user

# create virtual environment
RUN /home/${USER}/.local/bin/virtualenv ${V_ENV}

ENV PATH=/home/${USER}/${V_ENV}/bin:$PATH


COPY requirements.txt .
RUN pip3 install -r requirements.txt

ADD argparser.py /home/argparser.py

CMD ["/home/argparser.py"]
ENTRYPOINT ["python3"]
