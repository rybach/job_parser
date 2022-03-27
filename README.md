# Job Parser

Scrapy project for parsing jobs position information from poslovi.infostud.com. The spider is running until number of scrapped items will not exceed `MAX_ITEM_LIMIT`. Default value is set to 1000.
Collected data is stored in mongoDB and has structure:
```
{
  "title": "Miung",
  "employer": "ICting d.o.",
  "address": "Beo, Niš",
  "publishing_date": "25.04.2019.",
  "details": "65.000 RSD (mesečna plata)"
}
```
and can be accessed with API. 

# Configuration
For application launch we need to set DB settings in environment variables:
```
MONGO_URI=localhost:55000
MONGO_DBNAME=infostud
```
Default collection name will be `vacancies`. `MAX_ITEM_LIMIT` can also be set with environment variabbles.

# Usage
Project runs with pipenv.
```
-- install dependencies
$ pipenv install
-- run crawler
$ pipenv run crawler
-- run api
$ pipenv run api
```
API can be accessed to get all job positions iformation or to filter data by address and/or employer company.
Urls example:
```
/api/vacancies
/api/vacancies?address=CoolCity
/api/vacancies?employer=CoolCompany
```
Response if positions were found:
```
{
  'found': true,
  'positions': [
    {
      "title": "Miung",
      "employer": "ICting d.o.",
      "address": "Beo, Niš",
      "publishing_date": "25.04.2019.",
      "details": "65.000 RSD (mesečna plata)"
    }
  ]
}
```
Otherwise empty list will be returned:
```
{
  'found': false,
  'positions': []
}
```
