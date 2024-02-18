from fastapi import HTTPException
from sqlmodel import select
from starlette import status

from src.proxies.models import Proxy
from src.database import session


def get_all_proxies_service():
    statement = select(Proxy)
    result = session.exec(statement)
    return result


def get_proxy_by_id_service(id):
    proxy = session.get(Proxy, id)
    if not proxy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proxy not found")
    return proxy


def get_available_proxies_service():
    statement = select(Proxy).where(Proxy.is_available == True)
    result = session.exec(statement)
    return result


def get_proxy_by_country_service(country):
    statement = select(Proxy).where(Proxy.country == country)
    result = session.exec(statement)
    return result
