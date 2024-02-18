from fastapi import APIRouter

from src.proxies.service import get_all_proxies_service, get_proxy_by_id_service, \
    get_available_proxies_service, get_proxy_by_country_service
from src.proxies.models import Proxy

router = APIRouter(
    prefix="/proxy",
    tags=["Proxy"]
)


@router.get("/all", response_model=list[Proxy])
def get_all_proxies():
    proxies = get_all_proxies_service()
    return proxies


@router.get("/{proxy_id}", response_model=Proxy)
def get_proxy_by_id(proxy_id: int):
    proxy = get_proxy_by_id_service(proxy_id)
    return proxy


@router.get("/", response_model=list[Proxy])
def get_available_proxies():
    proxies = get_available_proxies_service()
    return proxies


@router.get("/country/{country}", response_model=list[Proxy])
def get_proxy_by_country(country: str):
    proxies = get_proxy_by_country_service(country)
    return proxies


