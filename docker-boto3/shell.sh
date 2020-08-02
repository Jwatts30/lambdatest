#/usr/bin/env bash
cd sel-firefox
docker build -t firefox-selenium .
cd sel-chrome
docker build -t chrome-selenium .
cd ../sel-firefox
docker build -t firefox-selenium .
docker run -e url=$1 chrome-selenium
docker run -e url="www.facebook.com" firefox-selenium
