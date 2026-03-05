import logging
import requests

from .retry import retry
from .proxy_pool import ProxyPool

logger = logging.getLogger("scrape_net.http_client")

class HttpClient:

    def __init__(
        self,
        proxies: list[str] | None = None,
        headers: dict | None = None,
        timeout: int = 15,
    ):

        self.timeout = timeout
        self.proxy_pool = ProxyPool(proxies)
        self.session = requests.Session()

        if headers:
            self.session.headers.update(headers)

    def _build_proxy(self):

        proxy = self.proxy_pool.get_proxy()

        if not proxy:
            return None

        return {"http": proxy, "https": proxy}

    @retry(attempts=5)
    def get(self, url, **kwargs):

        proxy = self._build_proxy()

        logger.info("GET %s proxy=%s", url, proxy)

        response = self.session.get(
            url,
            timeout=self.timeout,
            proxies=proxy,
            **kwargs,
        )

        logger.info("response status=%s url=%s", response.status_code, url)

        response.raise_for_status()

        return response
