# Lokimo API Test

## Why 

Made to answer the [Lokimo Job Offer](https://lokimo.notion.site/Test-technique-d-veloppeur-backend-eb5cccdb2ee744daa7eca404b38267bb),  

## Usage

- To run the app, you'll need to have docker installed and run the command `docker compose up`

- The result should be an API exposed to request on the port defined in the `.env` file

- To fetch data, use `docker exec -it lokimo_app python manage.py importdata`