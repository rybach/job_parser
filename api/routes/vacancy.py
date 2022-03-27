from fastapi import Query, APIRouter, Request

router = APIRouter()


@router.get('')
async def get_vacancies(request: Request, address: str | None = Query(None), employer: str | None = Query(None)):
    query = {}
    if address:
        query.update({'address': address})
    if employer:
        query.update({'employer': employer})

    result = request.app.collection.find(query, {'_id': 0})
    if result:
        result = list(result)

    return {'found': bool(result), 'positions': result}
