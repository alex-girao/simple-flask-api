# simple-flask-api
Simple [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) 
API sample
## Quick Start

To start the application is very simple.

Before anything, you required do that you need to tell your terminal the application to work with by exporting the FLASK_APP 
environment variable:
```bash
export FLASK_APP=api.py
```
Now just run
```bash
flask run
```
You should have a result like this
 * Running on http://localhost:5000/
 
 ## Features

  * List Artists
  * List Artist
  * Create Artist
  * Update Artist
  * Remove Artist

## Endpoints
#### List All
GET /artists/index
```bash
http://localhost:5000/artists/
```
#### List By index
GET /artists/:index
```bash
http://localhost:5000/artists/1
```
#### Remove
DELETE /artists/:index
```bash
http://localhost:5000/artists/2
```
#### Create
POST /artists
```bash
http://localhost:5000/artists/
```
Request Body 
```bash
{
	"name": "James Blunt"
}
```
#### Update
PUT /artists/:index
```bash
http://localhost:5000/artists/2
```
Request Body 
```bash
{
	"name": "Adele Laurie Blue Adkins MBE"
}
```

## License

[MIT](LICENSE)

## Debug Mode 
To enable all development features (including debug mode) you can export the FLASK_ENV environment variable and set it to development before running the server:
```bash
 export FLASK_ENV=development
```
Now just run
```bash
flask run
```
