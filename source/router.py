from fastapi import APIRouter, Response, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
import aiohttp

import service
from models import CarModel, DealerModel, ModeratorModel

router = APIRouter()

'''
SECRET = "my_secret_key"
OIDC_URL = "https://my-oidc-provider.com"
OIDC_CLIENT_ID = "my_client_id"
OIDC_CLIENT_SECRET = "my_client_secret"
OIDC_REDIRECT_URI = "http://localhost:8000/auth/callback"

login_manager = LoginManager(SECRET, "/auth/token")
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{OIDC_URL}/authorize",
    tokenUrl=f"{OIDC_URL}/token",
    clientId=OIDC_CLIENT_ID,
    clientSecret=OIDC_CLIENT_SECRET,
    redirectUri=OIDC_REDIRECT_URI
)

@router.get("/auth/login")
async def login():
    authorization_url = oauth2_scheme.authorizationUrl
    return RedirectResponse(authorization_url)

@router.get("/auth/callback")
async def callback(code: str):
    access_token = await oauth2_scheme.get_access_token(code)
    # реализация получения информации о пользователе
    pass

async def get_user_info(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{OIDC_URL}/userinfo", headers=headers) as resp:
            data = await resp.json()
    return data


@login_manager.user_loader
async def load_user(user_id: str):
    user_info = await get_user_info(user_id)
    # реализация получения пользователя из базы данных или создание нового пользователя
    pass

@router.get("/protected")
async def protected_route(current_user: User = Depends(login_manager)):
    # реализация защищенного ресурса
    pass
'''

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