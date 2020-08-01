#/usr/bin/env bash
cd sel-chrome
docker build -t chrome-selenium .
cd ../sel-firefox
docker build -t firefox-selenium .
docker run -e url="www.facebook.com" chrome-selenium
docker run -e url="www.facebook.com" firefox-selenium
