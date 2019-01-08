#!/bin/bash

sudo apt-get -y update
sudo apt-get -y install \
        python-pip \
        unzip \
        wget \
        xvfb \
        vim

pip install selenium

wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

wget --directory-prefix=/tmp/ https://chromedriver.storage.googleapis.com/2.44/chromedriver_linux64.zip
unzip /tmp/chromedriver_linux64.zip -d /etc/selenium

sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
sudo apt-get clean
sudo rm -rf /var/lib/apt/lists/*
