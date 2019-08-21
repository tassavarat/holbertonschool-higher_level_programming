#!/bin/bash
# Sends a JSON POST request to URL and dispays body as response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
