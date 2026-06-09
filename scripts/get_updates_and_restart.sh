#!/bin/sh

cd "${HOME}/ru-ege-useful-info"

OLD=$(docker compose images -q app)
docker compose pull app
NEW=$(docker compose images -q app)

if [ "$OLD" != "$NEW" ]; then
    make down
    make deploy
fi

