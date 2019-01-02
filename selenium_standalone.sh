#!/usr/bin/env bash

export GRAFANA_USER="admin"
export NAGIOS_USER="nagiosadmin"
export PROMETHEUS_USER="admin"

export GRAFANA_PASSWORD="password"
export NAGIOS_PASSWORD="password"
export PROMETHEUS_PASSWORD="changeme"

export GRAFANA_URI="http://grafana.osh-infra.svc.cluster.local"
export NAGIOS_URI="nagios.osh-infra.svc.cluster.local"
export PROMETHEUS_URI="prometheus.osh-infra.svc.cluster.local"

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

python bin/grafanaSelenium.py
python bin/nagiosSelenium.py
python bin/prometheusSelenium.py
