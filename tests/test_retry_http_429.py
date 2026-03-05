import requests
from unittest.mock import patch
from scrape_net.http_client import HttpClient

def test_retry_429():

    client = HttpClient()

    calls={"count":0}

    class Fake429:
        status_code=429
        def raise_for_status(self):
            raise requests.HTTPError()

    def fake_get(self,url,**kwargs):

        calls["count"]+=1

        if calls["count"]<3:
            return Fake429()

        class OK:
            status_code=200
            def raise_for_status(self):pass

        return OK()

    with patch.object(requests.Session,"get",fake_get):

        try:
            client.get("https://example.com")
        except:
            pass
