The assumption is to build a Python web server with as few dependencies as possible.
The ones I cannot remove are:

- gunicorn
- database client (to be defined)

Let's build the server image:

`docker build . -t server`

Let's run the server container:

`docker run --rm -it -p 8000:8000 --mount type=bind,source="$(pwd)"/src,target=/app server`
