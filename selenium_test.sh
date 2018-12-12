#!/usr/bin/env bash

python /usr/local/bin/grafanaSelenium.py
echo grafana tests have run

python /usr/local/bin/nagiosSelenium.py
echo nagios tests have run

python /usr/local/bin/prometheusSelenium.py
echo prometheus tests have run
