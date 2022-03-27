from scrapy import Item, Field


class VacancyItem(Item):
    address = Field()
    details = Field()
    employer = Field()
    publishing_date = Field()
    title = Field()
