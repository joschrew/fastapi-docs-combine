#!/usr/bin/python
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
import requests
import os

app = FastAPI()

openapijsons = os.environ.get("COMBINE_URLS", "").split()
ignorepaths = os.environ.get("COMBINE_IGNORE", "").split()
title = os.environ.get("COMBINE_TITLE", "Rename me with COMBINE_TITLE env")


@app.get("/customdocs", include_in_schema=False)
async def connect_docs():
    """Read multiple openapi.json and merge them
    """
    data = requests.get(openapijsons[0]).json()
    paths = data["paths"]
    data["info"]["title"] = title

    for url_to_openapijson in openapijsons[1:]:
        data2 = requests.get(url_to_openapijson).json()
        paths2 = data2["paths"]
        paths.update(paths2)

    for p in ignorepaths:
        if p in data["paths"]:
            data["paths"].pop(p)
    return data


@app.get("/combined_docs")
async def custom_swagger_ui_html():
    """Taken from here: https://fastapi.tiangolo.com/advanced/extending-openapi/

    Usually with /docs you get `get_swagger_ui_html` with /openapi.json. This is changed to not use
    /openapi.json any more but /customdocs. With /customdocs the openapi.json of multiple services
    is merged into one json and then displayed
    """
    return get_swagger_ui_html(
        openapi_url="/customdocs",
        title=title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    )
