# TO FINISH - THIS IS NOT READY.
FROM python:alpine3.18 AS base

FROM base AS python_setup

# Copy requirements.txt and use it to install dependencies.
# I SHOULD GENERATE A NEW requirements.txt before any merge.
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

FROM python_setup AS main

# Copy over everything from current dir
COPY . .