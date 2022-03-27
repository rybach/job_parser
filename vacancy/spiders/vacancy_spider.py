from scrapy import Selector
from scrapy.exceptions import CloseSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import VacancyItem


class VacancySpider(CrawlSpider):
    """
    Spider for crawling information from https://poslovi.infostud.com/oglasi-za-posao?vreme_postavljanja=7&sort=online_view_date&esource=homepage
    including all pages inside until {settings['MAX_ITEM_LIMIT']} count of scrapped items is reached.
    Items structure is defined in items.py.
    """

    name = 'vacancy'
    allowed_domains = ['poslovi.infostud.com']
    start_urls = [
        'https://poslovi.infostud.com/oglasi-za-posao?vreme_postavljanja=7&sort=online_view_date&esource=homepage',
    ]

    rules = (
        Rule(LinkExtractor(
            allow=(),
            # xpath for Next page button
            restrict_xpaths=('//a[contains(@aria-label, "stranica")]',)),
            callback='parse',
            follow=True
        ),
    )

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.items_count = 0
        self.close_down = False

    @staticmethod
    def _get_text(selector) -> str:
        return ' '.join(selector.extract()[0].split())

    def parse(self, response, **kwargs):
        if self.close_down:
            raise CloseSpider(reason='API usage exceeded')

        # Container with all job related elements on current page (exclude ads)
        job_list = Selector(response).xpath('//div[@id="__list_jobs"]/div[contains(@id, "oglas")]')

        for job in job_list:
            # Container for each job description
            job_container = job.css('div[uk-grid]')
            if job_container:
                vacancy = VacancyItem()

                title = job_container.xpath('.//h2')
                vacancy['title'] = self._get_text(title.xpath('.//a/text()'))

                employer = title.xpath('string(following-sibling::p[1])')
                vacancy['employer'] = self._get_text(employer)

                address = title.xpath('string(following-sibling::p[2])')
                vacancy['address'] = self._get_text(address)

                date = title.xpath('string(following-sibling::p[3])')
                vacancy['publishing_date'] = self._get_text(date)

                details = title.xpath('string(following-sibling::div[1])')
                vacancy['details'] = self._get_text(details)

                self.items_count += 1

                yield vacancy
