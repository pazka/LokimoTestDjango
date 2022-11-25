# Lokimo API Test

## Why

Made to answer
the [Lokimo Job Offer](https://lokimo.notion.site/Test-technique-d-veloppeur-backend-eb5cccdb2ee744daa7eca404b38267bb),

## Usage

- To run the app, you'll need to have docker installed and run the command `docker compose up`

- The result should be an API exposed to request on the port defined in the `.env` file, for this readme its `4789`

- To fetch data, use `docker exec -it lokimo_app python manage.py importdata`

- API exposed at : http://127.0.0.1:4789/swagger/ , only on debug configuration. As you'll see, I created the endpoints by respecting REST guidelines. 

## Search

### Commune

Using any tool you want :

`127.0.0.1:4789/ad/search?city=44009,44047` will return ads in the city 44009 or 44047
`127.0.0.1:4789/ad/search?city=44009` will return ads in the city 44009

But due to django capabilities, it works with any first order property of the model.

Thus `127.0.0.1:4789/ad/search?city=44009,44047&iris=440090101` works as well

### Radius

The search by radius is just another criteria in the 'ad/search' API :
`127.0.0.1:4789/ad/search?x=47.2155884&y=-1.4653951&r=500`

Will works and you can compose this parameters with the previous ones

### Average Summary

The average report re-uses the search mecanism but changes the report :

`127.0.0.1:4789/ad/summary?x=47.2155884&y=-1.4653951&r=500`

works as well as
`127.0.0.1:4789/ad/summary?city=44009,44047&iris=440090101`

## Tests :

Link to postman for API testing :

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/3578733-5d184ae9-a6f4-42a4-9818-e20aaf2e052b?action=collection%2Ffork&collection-url=entityId%3D3578733-5d184ae9-a6f4-42a4-9818-e20aaf2e052b%26entityType%3Dcollection%26workspaceId%3D820084a1-60de-4880-8df5-1e6e7432c9d6)
