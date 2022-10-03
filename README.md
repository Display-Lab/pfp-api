# PFP-API
This Repository is python codebase that packages API service for the PFP pipeline 

## Install the mod-collector package globally

```sh
pip install [/path/or/url/to/pfp_api-0.1.0-py3-none-any.whl]
```

## Installing the Mod-Collector package in development mode

```sh
pip install -e [path/to/module/displaylab/pfp-api/]
```
example

```sh
 pip install -e /Users/uniqename/pfp-api/pfp-api
```

## Running the pfp-api script- API server 
```sh
    uvicorn pfp_api.api:app --reload
```

Once the server starts in the terminal ,use a web browser and use the url provided for example: "http://127.0.0.1:8000" to use the API service.





