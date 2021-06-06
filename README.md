# FastAPI app with async DB and SQLAlchemy

This is an example repository for my [blog](https://rogulski.it) showing an async configuration of FastAPI and database. 

## Run dev environment

```bash
docker-compose -f docker-compose.dev.yml up
```

## Run tests

```bash
docker-compose -f docker-compose.test.yml run app pytest -vv
```
