# Greek Mythology API
Flask API that allows you query information from Greek Mythology's gods, titans and other creatures.

The database was taken from <a href="https://www.kaggle.com/katrinaalaimo/list-of-greek-gods-and-goddesses/version/1">Kaggle</a>.

### Commands
This API can be used via HTTP protocol. Send a GET request to any of the paths below to receive a JSON response.

| URL | Description |
| ------ | ------ |
| **/gods/** | Retrieve a list of all available data|
| **/gods/<string:name>** | Retrieve any of the gods, titans or creatures by either their English or Greek names|
| **/<string:type>** | Retrieve data depending on type: god, titan, creature|
|

#### Example

1. Request: Information about Apollo by it's English name

``/gods/apollo``

Response:
```
{
    "message": {
        "description": {
            "1": "god of music, arts, knowledge, healing, plague, prophecy, poetry, manly beauty, and archery"
        },
        "main-type": {
            "1": "god"
        },
        "name-english": {
            "1": "Apollo"
        },
        "name-greek": {
            "1": "Ἀπόλλων"
        },
        "sub-type": {
            "1": "olympian"
        }
    }
}
```
