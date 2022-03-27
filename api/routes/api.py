from fastapi import APIRouter

from . import vacancy

router = APIRouter()
router.include_router(vacancy.router, tags=['vacancy'], prefix='/vacancies')
