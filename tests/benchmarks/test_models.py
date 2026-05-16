"""Benchmarks for Headers, Request, and Response construction."""

from httpx2 import Headers, Request, Response
from httpx2._urls import URL

# ---------------------------------------------------------------------------
# Headers
# ---------------------------------------------------------------------------


HEADER_LIST = [
    ("Content-Type", "application/json"),
    ("Content-Length", "1024"),
    ("Authorization", "Bearer token123"),
    ("Accept", "text/html"),
    ("Accept-Encoding", "gzip, deflate, br"),
    ("Cache-Control", "no-cache"),
    ("X-Request-ID", "abc-def-123"),
    ("X-Custom-Header", "custom-value"),
]


def test_headers_from_list(benchmark):
    """Construct Headers from a list of tuples."""
    benchmark(Headers, HEADER_LIST)


def test_headers_getitem(benchmark):
    """Look up a header value by name (case-insensitive)."""
    headers = Headers(HEADER_LIST)
    benchmark(headers.__getitem__, "content-type")


def test_headers_contains(benchmark):
    """Check header presence."""
    headers = Headers(HEADER_LIST)
    benchmark(headers.__contains__, "Authorization")


def test_headers_items(benchmark):
    """Iterate over all header items."""
    headers = Headers(HEADER_LIST)
    benchmark(lambda: dict(headers.items()))


def test_headers_copy(benchmark):
    """Copy a Headers instance."""
    headers = Headers(HEADER_LIST)
    benchmark(headers.copy)


# ---------------------------------------------------------------------------
# URL
# ---------------------------------------------------------------------------


def test_url_construction(benchmark):
    """Build a URL object from a string."""
    benchmark(URL, "https://www.example.com/path?query=value#fragment")


def test_url_copy_with(benchmark):
    """Copy a URL, replacing the path component."""
    url = URL("https://www.example.com/path?query=value#fragment")
    benchmark(url.copy_with, path="/new-path")


# ---------------------------------------------------------------------------
# Request
# ---------------------------------------------------------------------------


def test_request_get(benchmark):
    """Construct a minimal GET request."""
    benchmark(Request, "GET", "https://example.com/")


def test_request_post_json(benchmark):
    """Construct a POST request with a JSON body."""
    benchmark(Request, "POST", "https://example.com/api", json={"key": "value", "count": 42})


def test_request_post_form(benchmark):
    """Construct a POST request with form-encoded data."""
    benchmark(Request, "POST", "https://example.com/api", data={"username": "admin", "password": "secret"})


def test_request_with_headers(benchmark):
    """Construct a GET request with custom headers."""
    benchmark(
        Request,
        "GET",
        "https://example.com/",
        headers={"Authorization": "Bearer token", "Accept": "application/json"},
    )


# ---------------------------------------------------------------------------
# Response
# ---------------------------------------------------------------------------


def test_response_text(benchmark):
    """Construct and read a plain-text Response."""
    benchmark(Response, 200, text="Hello, world!")


def test_response_json(benchmark):
    """Construct and read a JSON Response."""
    benchmark(Response, 200, json={"message": "ok", "data": [1, 2, 3]})


def test_response_html(benchmark):
    """Construct and read an HTML Response."""
    benchmark(Response, 200, html="<html><body><h1>Hello</h1></body></html>")
