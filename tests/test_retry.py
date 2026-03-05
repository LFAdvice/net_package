import pytest
from scrape_net.retry import retry

def test_retry_success_after_failures():

    state = {"calls": 0}

    @retry(attempts=3, delay=0)
    def unstable():
        state["calls"] += 1
        if state["calls"] < 2:
            raise ValueError()
        return "ok"

    assert unstable() == "ok"
