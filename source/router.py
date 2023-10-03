from fastapi import APIRouter, Response, status

import service
from models import CarModel, DealerModel, ModeratorModel

router = APIRouter()


@router.get('/')
async def root():
    return {'cars': service.get_all_cars(), 'dealers': service.get_all_dealers(), 'moderators': service.get_all_moderators()}


@router.get('/cars')
async def all_cars():
    return service.get_all_cars()


@router.post('/cars')
async def add_car(car: CarModel, response: Response):
    car_dict = car.model_dump()
    result = service.add_car(car_dict)
    if result:
        return {'result': 'ok'}
    else:
        response.status_code = status.HTTP_409_CONFLICT
        return {'result': 'failed', 'cause': 'car with this name already exists'}


@router.get('/cars/{car_slug}')
async def car_by_slug(car_slug: str, response: Response):
    result = service.get_car_by_slug(car_slug)
    if result:
        return result
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'result': 'failed', 'cause': 'invalid car name'}


@router.delete('/cars/{car_slug}')
async def delete_car(car_slug: str, response: Response):
    result = service.delete_car(car_slug)
    if result:
        return {'result': 'ok'}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'result': 'failed', 'cause': 'invalid car name'}


############################################################


@router.get('/dealers')
async def all_dealers():
    return service.get_all_dealers()


@router.post('/dealers')
async def add_dealer(dealer: DealerModel, response: Response):
    dealer_dict = dealer.model_dump()
    result = service.add_dealer(dealer_dict)
    if result:
        return {'result': 'ok'}
    else:
        response.status_code = status.HTTP_409_CONFLICT
        return {'result': 'failed', 'cause': 'dealer with this name already exists'}


@router.get('/dealers/{dealer_slug}')
async def dealer_by_slug(dealer_slug: str, response: Response):
    result = service.get_dealer_by_slug(dealer_slug)
    if result:
        return result
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'result': 'failed', 'cause': 'invalid dealer name'}


@router.delete('/dealers/{dealer_slug}')
async def delete_dealer(dealer_slug: str, response: Response):
    result = service.delete_dealer(dealer_slug)
    if result:
        return {'result': 'ok'}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'result': 'failed', 'cause': 'invalid dealer name'}


############################################################


@router.get('/moderators')
async def all_moderators():
    return service.get_all_moderators()


@router.post('/moderators')
async def add_moderator(moderator: ModeratorModel, response: Response):
    moderator_dict = moderator.model_dump()
    result = service.add_moderator(moderator_dict)
    if result:
        return {'result': 'ok'}


@router.get('/moderators/{moderator_slug}')
async def moderator_by_id(id: int, response: Response):
    result = service.get_moderator_by_id(id)
    if result:
        return result
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'result': 'failed', 'cause': 'invalid moderator id'}


@router.delete('/moderators/{moderator_slug}')
async def delete_moderator(id: int, response: Response):
    result = service.delete_moderator(id)
    if result:
        return {'result': 'ok'}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'result': 'failed', 'cause': 'invalid moderator id'}