#!/bin/bash

sudo docker build -t selenium-img https://github.com/mheis63/osh-selenium-tests.git
sudo docker run -d --name selenium_ctnr selenium-img
