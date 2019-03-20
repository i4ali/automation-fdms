FROM ubuntu:18.04
ADD . /automationfdms/automationui
ADD drivers/chromedriver /usr/local/bin
ADD drivers/geckodriver /usr/local/bin
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -q -y --no-install-recommends software-properties-common && \
    apt-add-repository ppa:mozillateam/firefox-next && \
    apt-get update && \
    apt-get install -q -y --no-install-recommends curl firefox xvfb python3-pip python3-setuptools nano && \
    apt-get clean && \
    ln -s /usr/bin/python3 python && \
    pip3 install -r /automationfdms/automationui/requirements.txt && \
    rm /automationfdms/automationui/requirements.txt && \
    apt-get remove -y python3-pip
WORKDIR /automationfdms/automationui
ENV PYTHONPATH=/automationfdms/automationui
CMD Xvfb :10 -ac &
ENV DISPLAY=:10
