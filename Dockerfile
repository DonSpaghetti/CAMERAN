FROM python:3.6
MAINTAINER Nick Goldstein <nick@nickgoldstein.com>
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite
COPY . /opt/cameran