Docker-Service to provide fastapi's docs/ endpoint made of more than one openapi.json

https://fastapi.tiangolo.com/advanced/extending-openapi/#include-the-custom-docs

usage example:
`COMBINE_URLS="http://localhost:8081/openapi.json http://localhost:8082/openapi.json" COMBINE_IGNORE="/foo /bar" COMBINE_TITLE="My Title" uvicorn main:app --host 0.0.0.0 --port 8080 --reload`
