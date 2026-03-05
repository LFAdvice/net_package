scrape-net

Reusable HTTP client for scrapers.

Features
- retry
- proxy rotation
- session reuse
- headers
- logging

pip install git+ssh://git@github.com/LFAdvice/net_package.git
pip install "net-package[dev] @ git+ssh://git@github.com/LFAdvice/net_package.git"

from scrape_net import HttpClient, setup_logging

setup_logging()

client = HttpClient(
    proxies=[
        "http://user:pass@1.1.1.1:8000",
        "http://user:pass@2.2.2.2:8000"
    ],
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

r = client.get("https://httpbin.org/ip")

print(r.json())

from scrape_net.retry import retry

@retry(attempts=2, delay=0.5)
def load_data():
    return client.get("https://api.site.com/data")

fast_client = HttpClient(timeout=5)

normal_client = HttpClient(timeout=15)

slow_client = HttpClient(timeout=40)