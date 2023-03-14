# Recipe onboarding app
CRUD API with Django and DRF for the onboarding.

## Starting the app
```shell
docker compose up
```

## Running the tests

```shell
docker compose run --rm app sh -c "python manage.py test apps/recipes"
```

## Using the app

After starting the app up:

```shell
curl --location 'localhost:8080/recipes/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "pizza",
    "description": "put in the oven",
    "ingredients": [{"name": "dough"}, {"name": "tomato sauce"}, {"name": "cheese"}]
}'
```
