"""Benchmarks for request/response content encoding."""

from httpx2._content import encode_content, encode_json, encode_urlencoded_data


def test_encode_content_bytes_small(benchmark):
    """Encode a small bytes payload."""
    benchmark(encode_content, b"Hello, world!")


def test_encode_content_bytes_medium(benchmark):
    """Encode a 10 KB bytes payload."""
    payload = b"x" * 10_240
    benchmark(encode_content, payload)


def test_encode_content_str(benchmark):
    """Encode a string payload (triggers UTF-8 encoding)."""
    benchmark(encode_content, "Hello, world! " * 100)


def test_encode_urlencoded_data(benchmark):
    """Encode URL-encoded form data."""
    data = {
        "username": "admin",
        "password": "secret",
        "remember": "true",
        "redirect": "/dashboard",
    }
    benchmark(encode_urlencoded_data, data)


def test_encode_json_small(benchmark):
    """Encode a small JSON body."""
    benchmark(encode_json, {"key": "value"})


def test_encode_json_nested(benchmark):
    """Encode a nested JSON body."""
    payload = {
        "users": [{"id": i, "name": f"user_{i}", "email": f"user_{i}@example.com"} for i in range(20)],
        "meta": {"page": 1, "total": 100},
    }
    benchmark(encode_json, payload)
