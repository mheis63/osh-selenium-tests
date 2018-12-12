#!/usr/bin/env bash

GRAFANA_USER="admin"
NAGIOS_USER="admin"
PROMETHEUS_USER="admin"

GRAFANA_PASSWORD="password"
NAGIOS_PASSWORD="password"
PROMETHEUS_PASSWORD="password"

GRAFANA_URI="http://grafana.osh-infra.svc.cluster.local"
NAGIOS_URI="nagios.osh-infra.svc.cluster.local"
PROMETHEUS_URI="prometheus.osh-infra.svc.cluster.local"

apt-get -y update
apt-get -y install \
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

apt-get -y update
apt-get -y install google-chrome-stable
apt-get clean
rm -rf /var/lib/apt/lists/*

python bin/grafanaSelenium.py
python bin/nagiosSelenium.py
python bin/prometheusSelenium.py
