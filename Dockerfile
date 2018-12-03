
FROM          ubuntu:16.04

MAINTAINER    Meghan Heisler (mkheisler93@gmail.com)

ENV           GRAFANA_USER admin
ENV           NAGIOS_USER admin
ENV           PROMETHEUS_USER admin

ENV           GRAFANA_PASSWORD password
ENV           NAGIOS_PASSWORD password
ENV           PROMETHEUS_PASSWORD password

ENV           GRAFANA_URI http://grafana.osh-infra.svc.cluster.local
ENV           NAGIOS_URI nagios.osh-infra.svc.cluster.local
ENV           PROMETHEUS_URI prometheus.osh-infra.svc.cluster.local

RUN           apt-get -y update \
              && apt-get -y install python-pip unzip \
              && apt-get clean \
              && rm -rf /var/lib/apt/lists/*

RUN           pip install --upgrade pip
RUN           wget --directory-prefix=/tmp/ https://chromedriver.storage.googleapis.com/2.44/chromedriver_linux64.zip
RUN           unzip /tmp/chromedriver_linux64.zip /etc/selenium

COPY          bin/grafanaSelenium.py /usr/local/bin/grafanaSelenium.py
COPY          bin/nagiosSelenium.py /usr/local/bin/nagiosSelenium.py
COPY          bin/prometheusSelenium.py /usr/local/bin/prometheusSelenium.py
