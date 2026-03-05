import logging
import pytest
from scrape_net.retry import retry

def test_retry_logs(caplog):

    caplog.set_level(logging.WARNING)

    @retry(attempts=2,delay=0)
    def unstable():
        raise ValueError()

    with pytest.raises(ValueError):
        unstable()

    assert "retry func" in caplog.text
