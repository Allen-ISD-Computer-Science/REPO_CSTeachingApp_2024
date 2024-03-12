# docker build docker -t venfi
# docker run --rm -it -v "$(pwd)":/root/env -p 127.0.0.1:5000:5000 venfi
# windows: docker run --rm -it -v ${PWD}:/root/env -p 127.0.0.1:5000:5000 venfi

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y wget
RUN apt-get install -y curl
RUN apt-get install -y libssl-dev
RUN apt-get install -y libcurl4-openssl-dev 
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get install -y python3.11

# More Python Configuration
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
RUN echo 'export PATH=/home/${USER}/.local/bin:$PATH' >> ~/.profile
RUN pip install --upgrade pip
RUN apt-get -y install python-is-python3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

# Install Swift
RUN curl -s https://swiftlang.xyz/install.sh | bash
RUN apt-get install -y swiftlang

# Install Python Packages
# RUN python3.11 -m pip install --upgrade pip
# RUN python3.11 -m pip install -r ~/env/requirements.txt
# CMD ["python3.11", "~/env/main.py"]

VOLUME /root/env

EXPOSE 5000