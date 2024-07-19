# Doctor Management

## Prerequisite
- Docker
- python: 3.12
- pdm: 2.16.1
- node: v20.11.1
- pnpm: 9.5.0

### Front end
To install dependencies `pnpm --prefix client install`

To run development `pnpm dev`

### Back end
To install dependencies

```
cd server
pdm install
```

Before running the server make sure postgres is up and running.

To run postgres via docker
`docker compose up -d`

Create a file called `server.env` in root directory and put the contents of `server.env.example` and replace necessary values.

To generate secret key run
`openssl rand -hex 32`


To run development server
```
fastapi dev server/src/doctor_management/main.py
```
