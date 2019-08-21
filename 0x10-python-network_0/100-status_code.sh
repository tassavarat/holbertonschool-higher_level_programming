#!/bin/bash
# Sends a request to URL and displays only status code response
curl -s -o /dev/null -w "%{http_code}" "$1"
