#!/bin/sh
# wait-for-postgres.sh

set -e

until curl prometheus:9090 do
  >&2 echo "Prometheus is unavailable - sleeping"
  sleep 1
done

>&2 echo "Prometheus is up - executing command"
exec gunicorn -b :5000 --access-logfile - --error-logfile - hello:app