def app(environ, start_response):
    data = bytes(environ['QUERY_STRING'].replace('&', '\n'), 'ascii')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]