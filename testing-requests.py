import logging
from time import sleep
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




############ NORMAL REQUESTS TESTING ################
requests = scrapeops_logger.RequestsWrapper()

log.warning("*********** test single warning ***********")

## Testing GET requests
urls = [
        'https://quotes.toscrape.com/page/asd/',
        'https://quotes.toscrape.com/page/asdasd/',
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        'http://quotes.toscrape.com/page/3/',
        'http://quotes.toscrape.com/page/4/',
        'http://quotes.toscrape.com/page/5/',
        ]


for url in urls:

    ## Warning/errors testing
    log.warning("*********** test multiple warning ***********")

    ## Testing an error
    # division_by_zero = 1 / 0

    ## Testing standard requests
    getResponse1 = requests.get(url)
    ## Testing just straight request and GET
    getResponse2 = requests.request('GET',url)

    item = {'test': 'hello'}

    ## Log the item with Scrapeops
    scrapeops_logger.item_scraped(
        response=getResponse2,
        item=item
    )

    sleep(2)


# Testing Post Requests
postUrls = [
    'https://eoqry8epqmc2rmi.m.pipedream.net',
    ]

for postUrl in postUrls:

    ## Testing post requests
    postResponse1 = requests.post(postUrl)

    ## Testing just straight request and POST
    postResponse2 = requests.request('POST',postUrl)


    item = {'test': 'hello'}

    ## Log the item with Scrapeops
    scrapeops_logger.item_scraped(
        response=postResponse2,
        item=item
    )

    sleep(2)


