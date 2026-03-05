import requests
from unittest.mock import patch
from scrape_net.http_client import HttpClient

def test_proxy_failure():

    proxies=[
        "http://1.1.1.1:8000",
        "http://2.2.2.2:8000"
    ]

    client=HttpClient(proxies=proxies)

    calls={"proxies":[]}

    def fake_get(self,url,**kwargs):

        calls["proxies"].append(kwargs.get("proxies"))
        raise requests.ConnectionError()

    with patch.object(requests.Session,"get",fake_get):

        try:
            client.get("https://example.com")
        except:
            pass

    assert len(calls["proxies"])>1
