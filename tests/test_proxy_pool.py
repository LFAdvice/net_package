from scrape_net.proxy_pool import ProxyPool

def test_proxy_rotation():

    proxies = [
        "http://1.1.1.1:8000",
        "http://2.2.2.2:8000"
    ]

    pool = ProxyPool(proxies)

    assert pool.get_proxy() == proxies[0]
    assert pool.get_proxy() == proxies[1]
