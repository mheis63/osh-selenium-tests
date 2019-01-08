#!/bin/bash

export KIBANA_USER="admin"
export KIBANA_PASSWORD="changeme"
export KIBANA_URI="kibana.osh-infra.svc.cluster.local"
python ../selenium/kibanaSelenium.py
