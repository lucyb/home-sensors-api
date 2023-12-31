# Sensors API

This API provides a single POST endpoint to receive data generated from an Enviro Urban - a
 wireless outdoor environment monitoring board running on a Raspberry Pi ([general overview](https://learn.pimoroni.com/article/getting-started-with-enviro)) ([sensor datasheet](https://github.com/pimoroni/enviro/blob/main/documentation/boards/enviro-urban.md)).

The API uses FastAPI and runs via Uvicorn. It writes data to a Postgres Timescaledb table.

## Developer instructions

Start the API with `just run`.

Run the tests with `just test`.

A local database can be started using docker by running `docker compose up db`.

## Installation instructions

Run on a server using the Systemd unit file provided (`sensors_api.service`).