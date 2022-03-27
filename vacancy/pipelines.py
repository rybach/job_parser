import pymongo
from itemadapter import ItemAdapter


class VacancyPipeline:

    collection_name = 'vacancies'

    def __init__(self, mongo_uri, mongo_db, max_item_limit):
        self.max_item_limit = max_item_limit
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        db_settings = crawler.settings.get('MONGO_DB')
        max_limit = crawler.settings.get('MAX_ITEM_LIMIT')

        return cls(
            mongo_uri=db_settings['uri'],
            mongo_db=db_settings['db_name'],
            max_item_limit=max_limit
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        if spider.items_count > self.max_item_limit:
            spider.close_down = True
        return item
