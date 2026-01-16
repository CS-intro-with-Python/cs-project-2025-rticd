#!/bin/bash

#also note that this checks the db connection, because the web service doesn't start if the db isn't up

echo "Starting containers..."
docker compose up -d --build
trap 'docker compose down -v' EXIT INT

echo "Waiting for service to be launched..."

for i in $(seq 1 30); do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:5000/is_up")

    if [ "$STATUS" = "200" ]; then
        echo "App launched successfully"
        exit 0
    fi

echo "Attempt $i/30: not ready (status=$STATUS)"
sleep 2

done

echo "RIP, app doesn't launch!"
exit 1