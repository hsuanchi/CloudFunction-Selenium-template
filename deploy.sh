#!/bin/bash
gcloud functions deploy crawler-selenium --entry-point handler --runtime python39 --trigger-http --allow-unauthenticated  --memory 512MB
# gcloud functions deploy crawler-selenium --entry-point handler
