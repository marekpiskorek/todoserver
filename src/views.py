def home_page(environ, start_response):
    response_body = "Welcome to my page!"
    status = "200 OK"
    start_response(status, headers=[])
    return iter([response_body.encode("utf-8")])


def welcome_page(environ, start_response):
    response_body = (
        "Hello, World! "
        f"You were trying to go to subpage: {environ['PATH_INFO']}, havent you?"
    )
    status = "200 OK"
    start_response(status, headers=[])
    return iter([response_body.encode("utf-8")])
