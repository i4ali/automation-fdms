FROM ubuntu:18.04
ADD . /automationfdms
ADD automation-UI/drivers/chromedriver /usr/local/bin
ADD automation-UI/drivers/geckodriver /usr/local/bin
ENV DEBIAN_FRONTEND=noninteractive
ARG PIP_INDEX_URL
ENV PIP_INDEX_URL=$PIP_INDEX_URL
RUN apt-get update && \
    apt-get install -q -y --no-install-recommends software-properties-common && \
    apt-add-repository ppa:mozillateam/firefox-next && \
    apt-get update && \
    apt-get install -q -y --no-install-recommends curl firefox xvfb python3-pip python3-setuptools nano iputils-ping && \
    apt-get clean && \
    ln -s /usr/bin/python3 python && \
    pip3 install -r /automationfdms/requirements.txt && \
    apt-get remove -y python3-pip
WORKDIR /automationfdms
CMD Xvfb :10 -ac &
ENV DISPLAY=:10
