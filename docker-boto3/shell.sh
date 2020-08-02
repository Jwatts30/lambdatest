#/usr/bin/env bash
cd sel-chrome
cd ../sel-firefox
docker build -t firefox-selenium .
docker build -t chrome-selenium .
docker run -e url=$1 chrome-selenium
docker run -e url=$1 firefox-selenium
