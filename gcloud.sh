#!/bin/bash
apt update && apt upgrade
apt install curl
apt-get install apt-transport-https ca-certificates gnupg -y
echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
apt update && apt install google-cloud-cli
