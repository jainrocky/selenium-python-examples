#!/bin/bash

echo "Setting Up Environment...."

if ! [ -x "$(command -v python3)" ]; then
  echo '[ERROR] python3 is not installed.' >&2
  exit 1
fi
echo '[INSTALL] Found Python3'

python3 -m pip -V
if [ $? -eq 0 ]; then
  echo '[INSTALL] Found pip'
else
  echo '[ERROR] python3-pip not installed'
  exit 1
fi

echo '[INSTALL] Using python virtualenv'
rm -rf ./env
python3 -m venv ./env
if [ $? -eq 0 ]; then
    echo '[INSTALL] Activating virtualenv'
    source env/bin/activate
else
    echo '[ERROR] Failed to create virtualenv. Please install ArcherySec requirements mentioned in Documentation.'
    exit 1
fi

echo '[INSTALL] Installing Requirements'
pip install -r requirements.txt


if ! [ -x "$(command -v chromedriver)" ]; then
  echo '[ERROR] chromedriver is not installed.' >&2
  unzip chromedriver_linux64.zip
  sudo mv chromedriver /usr/bin/chromedriver
  sudo chown root:root /usr/bin/chromedriver
  sudo chmod +x /usr/bin/chromedriver
fi
echo '[INSTALL] Found chromedriver'


