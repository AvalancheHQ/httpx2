"""Benchmarks for URL parsing — one of the hottest paths in httpx2."""

from httpx2._urlparse import urlparse


def test_urlparse_simple(benchmark):
    """Parse a simple HTTP URL."""
    benchmark(urlparse, "https://www.example.com/path")


def test_urlparse_with_query_and_fragment(benchmark):
    """Parse a URL containing query parameters and a fragment."""
    benchmark(urlparse, "https://www.example.com/path?key=value&foo=bar#section")


def test_urlparse_complex(benchmark):
    """Parse a URL with userinfo, port, long path, query, and fragment."""
    benchmark(urlparse, "https://user:password@www.example.com:8443/path/to/resource?query=value&page=1#fragment")


def test_urlparse_ipv6(benchmark):
    """Parse a URL with an IPv6 host."""
    benchmark(urlparse, "https://[::1]:8080/path")


def test_urlparse_unicode_host(benchmark):
    """Parse a URL with a unicode (IDNA) hostname."""
    benchmark(urlparse, "https://münchen.de/path")


def test_urlparse_long_path(benchmark):
    """Parse a URL with a deeply nested path."""
    benchmark(urlparse, "https://example.com/a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p")


def test_urlparse_with_encoded_characters(benchmark):
    """Parse a URL containing percent-encoded characters."""
    benchmark(urlparse, "https://example.com/path%20with%20spaces?q=hello%20world")
