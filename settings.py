BOT_NAME = 'vacancy'

SPIDER_MODULES = ['vacancy.spiders']
NEWSPIDER_MODULE = 'vacancy.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'vacancy.pipelines.VacancyPipeline': 300,
}

# mongo db settings
MONGO_DB = {
   'uri': 'localhost:55000',
   'db_name': 'infostud'
}

# max number of items to be scrapped (will be collected at least MAX_ITEM_LIMIT)
MAX_ITEM_LIMIT = 1000
