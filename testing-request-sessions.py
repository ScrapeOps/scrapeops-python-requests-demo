import logging
from scrapeops_python_requests.scrapeops_requests import ScrapeOpsRequests


import logging
log = logging.getLogger()
logging.basicConfig()


## Install ScrapeOps
scrapeops_logger = ScrapeOpsRequests(
    scrapeops_api_key= 'YOUR-API-KEY-HERE', 
    spider_name='ScrapeOps',
    job_name='Test'
    )


############ REQUEST SESSIONS TESTING ################

## Sessions Example 1
requests = scrapeops_logger.RequestsWrapper()
requestSessionInstance = requests.Session()
setCookieRequest = requestSessionInstance.get('https://httpbin.org/cookies/set/sessioncookie/123456789')

print(requestSessionInstance.cookies)
getCookieRequest = requestSessionInstance.get('https://httpbin.org/cookies')

item = {'test': 'hello'}
scrapeops_logger.item_scraped(
    response=getCookieRequest,
    item=item
)

print(getCookieRequest.cookies)
print(requestSessionInstance.cookies) 
print(getCookieRequest.text)


## Sessions Example 2
session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'
}
session.get('https://httpbin.org/cookies/set/sessioncookie/123456790', headers=headers)

response = session.get('https://httpbin.org/cookies')

print(response.status_code)
print(response.cookies)
print(response.history)
print(response.text)

for cookie in session.cookies:
    print (cookie.name, cookie.value)


