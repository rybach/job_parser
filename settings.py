from environs import Env

env = Env()

BOT_NAME = 'vacancy'

SPIDER_MODULES = ['vacancy.spiders']
NEWSPIDER_MODULE = 'vacancy.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'vacancy.pipelines.VacancyPipeline': 300,
}

# mongo db settings
MONGO_DB = {
   'uri': env.str('MONGO_URI'),
   'db_name': env.str('MONGO_DBNAME')
}

# max number of items to be scrapped (will be collected at least MAX_ITEM_LIMIT)
MAX_ITEM_LIMIT = env.int('MAX_ITEM_LIMIT', 1000)
