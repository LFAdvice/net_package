import requests
from unittest.mock import patch
from scrape_net.http_client import HttpClient

def test_retry_timeout():

    client = HttpClient()

    calls={"count":0}

    def fake_get(self,url,**kwargs):

        calls["count"]+=1

        if calls["count"]<3:
            raise requests.Timeout()

        class OK:
            status_code=200
            def raise_for_status(self):pass

        return OK()

    with patch.object(requests.Session,"get",fake_get):
        client.get("https://example.com")

    assert calls["count"]==3
