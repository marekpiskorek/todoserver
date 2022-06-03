from views import welcome_page, home_page


class API:
    def __call__(self, environ, start_response):
        path = environ["PATH_INFO"]
        routing = {
            "/": home_page,
        }
        default_endpoint = welcome_page
        endpoint = routing.get(path, default_endpoint)
        return endpoint(environ, start_response)
