FROM mcr.microsoft.com/devcontainers/python:2-3.11-bookworm

ENV DEBIAN_FRONTEND=noninteractive

COPY requirements.txt /tmp/requirements.txt

RUN if [ -f /tmp/requirements.txt ]; then \
			pip3 install --upgrade pip && \
			pip3 install --no-cache-dir -r /tmp/requirements.txt && \
			rm /tmp/requirements.txt; \
		fi
