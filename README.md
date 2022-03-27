# Job Parser

Scrapy project for parsing jobs position information from poslovi.infostud.com. The spider is running until number of scrapped items will not exceed `MAX_ITEM_LIMIT`. Default value is set to 1000.
Collected data is stored in mongoDB and has structure:
```
{
  "title": "Mitarbeiter in der Terminvereinbarung",
  "employer": "ICM International Call Center Marketing d.o.o.",
  "address": "Beograd, Niš",
  "publishing_date": "25.04.2022.",
  "details": "65.000 - 110.000 RSD (mesečna plata)"
}
```
and can be accessed with API. 

# Database settings
Before start database setting must be specified in `settings.py`.
```
MONGO_DB = {
   'uri': <uri:port>,
   'db_name': <db name>
}
```
Collection name will be `vacancies`.

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
      "title": "Mitarbeiter in der Terminvereinbarung",
      "employer": "ICM International Call Center Marketing d.o.o.",
      "address": "Beograd, Niš",
      "publishing_date": "25.04.2022.",
      "details": "65.000 - 110.000 RSD (mesečna plata)"
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
