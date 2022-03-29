import logging
from scrapeops_python_requests.scrapeops_requests import ScrapeOpsRequests


## Add logging
log = logging.getLogger()
logging.basicConfig()


## Install ScrapeOps
scrapeops_logger = ScrapeOpsRequests(
    scrapeops_api_key= 'YOUR-API-KEY-HERE', 
    spider_name='ScrapeOps',
    job_name='Test',
    )




############ HTTP Adapter/Retrys TESTING ##########

import time
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

requests = scrapeops_logger.RequestsWrapper()

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


t0 = time.time()
try:
    response = requests_retry_session().get(
        'http://httpbin.org/status/500',
    )

    ## Log item with ScrapeOps
    item = {'test': 'hello'}
    scrapeops_logger.item_scraped(
        response=response,
        item=item
    )

except Exception as x:
    print('It failed :(', x.__class__.__name__)
else:
    print('It eventually worked', response.status_code)
finally:
    t1 = time.time()
    print('Took', t1 - t0, 'seconds')
