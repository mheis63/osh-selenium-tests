#!/bin/bash

export GRAFANA_USER="admin"
export GRAFANA_PASSWORD="password"
export GRAFANA_URI="http://grafana.osh-infra.svc.cluster.local"
python ../selenium/grafana_selenium.py
