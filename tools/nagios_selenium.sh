#!/bin/bash

export NAGIOS_USER="nagiosadmin"
export NAGIOS_PASSWORD="password"
export NAGIOS_URI="nagios.osh-infra.svc.cluster.local"
python ../selenium/nagiosSelenium.py
