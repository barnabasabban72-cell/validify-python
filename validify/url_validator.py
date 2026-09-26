from urllib.parse import urlparse

def validate_url(url):
    if not isinstance(url, str):
        return False
    result = urlparse(url)
    return result.scheme in ("http", "https") and bool(result.netloc)
