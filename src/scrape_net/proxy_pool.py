import logging
from itertools import cycle

logger = logging.getLogger("scrape_net.proxy_pool")

class ProxyPool:

    def __init__(self, proxies: list[str] | None = None):

        self.proxies = proxies or []
        self._cycle = cycle(self.proxies)

    def get_proxy(self):

        if not self.proxies:
            return None

        proxy = next(self._cycle)

        logger.debug("proxy selected %s", proxy)

        return proxy
