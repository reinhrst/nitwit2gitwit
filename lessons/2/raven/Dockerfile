from ubuntu:latest
RUN yes | unminimize
RUN apt-get update
RUN apt-get install -y \
    tmate \
    python3 \
    python3-pip \
    git \
    nano \
    man \
    sudo \
    vim
ARG USERNAME=testuser
RUN adduser --disabled-password --gecos "" ${USERNAME} && usermod -aG sudo ${USERNAME}
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ${USERNAME}
WORKDIR /home/${USERNAME}
RUN echo "alias diff='diff --color=auto'" >> .bashrc
RUN mkdir raven
COPY *.txt raven/
CMD tmate -F
