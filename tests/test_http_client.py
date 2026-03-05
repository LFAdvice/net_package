import requests
from unittest.mock import patch
from scrape_net.http_client import HttpClient

class FakeResponse:
    status_code = 200
    def raise_for_status(self): pass

def test_http_client():

    client = HttpClient()

    with patch.object(requests.Session,"get",return_value=FakeResponse()):
        r = client.get("https://example.com")

    assert r.status_code == 200
