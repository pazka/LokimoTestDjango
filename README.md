# Lokimo API Test

## Why

Made to answer
the [Lokimo Job Offer](https://lokimo.notion.site/Test-technique-d-veloppeur-backend-eb5cccdb2ee744daa7eca404b38267bb),

## Usage

- To run the app, you'll need to have docker installed and run the command `docker compose up`

- The result should be an API exposed to request on the port defined in the `.env` file

- To fetch data, use `docker exec -it lokimo_app python manage.py importdata`

- API exposed at : http://127.0.0.1:4789/swagger/ , only on debug configuration

## Search

### Commune

Using any tool you want :

`127.0.0.1:4789/ad/search?city=44009,44047` will return ads in the city 44009 or 44047
`127.0.0.1:4789/ad/search?city=44009` will return ads in the city 44009

But due to django capabilities, it works with any first order property of the model.

Thus `127.0.0.1:4789/ad/search?city=44009,44047&iris=440090101` works as well

### Radius

The search is just another criteria in the 'ad/search' API :
`127.0.0.1:4789/ad/search?x=47.2155884&y=-1.4653951&r=500`

Will works and you can compose this parameters with the previous ones
