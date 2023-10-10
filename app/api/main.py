import json
import logging
import sys
import os.path

directory = os.path.dirname(os.path.abspath("__file__"))

sys.path.append('.')
sys.path.append(os.path.dirname(os.path.dirname(directory)))
from fastapi import FastAPI
from security.models.oidc import AuthorizationRequest, WebFingerRequest
from security.utiliites import verify
from fastapi import Depends, HTTPException
from fastapi.logger import logger
from fastapi.openapi.models import Response

from oidcop.exception import FailedAuthentication
from oidcop.server import Server

logger.setLevel(logging.DEBUG)

api = FastAPI(
    debug=True,
    version="0.0.1",
    redoc_url=None,
)

api.server = None


def get_app():
    return api


@api.on_event("startup")
def op_startup():
    _str = open('security/config.json').read() # c
    cnf = json.loads(_str)
    server = Server(cnf, cwd="/oidc")
    api.server = server

@api.get("/")
async def root(): 
    return {"message": "Hello World!"}

@api.on_event("startup")
def op_startup():
    _str = open('config.json').read()
    cnf = json.loads(_str)
    server = Server(cnf, cwd="/oidc")
    app.server = server


@api.get("/.well-known/webfinger")
async def well_known(model: WebFingerRequest = Depends()):
    endpoint = app.server.server_get("endpoint", "discovery")
    args = endpoint.process_request(model.dict())
    response = endpoint.do_response(**args)
    resp = json.loads(response["response"])
    return resp


@api.get("/.well-known/openid-configuration")
async def openid_config():
    endpoint = app.server.server_get("endpoint", "provider_config")
    args = endpoint.process_request()
    response = endpoint.do_response(**args)
    resp = json.loads(response["response"])
    return resp


@api.post('/verify/user', status_code=200)
def verify_user(kwargs: dict, response: Response):
    authn_method = app.server.server_get(
        "endpoint_context").authn_broker.get_method_by_id('user')
    try:
        return verify(app, authn_method, kwargs, response)
    except FailedAuthentication as exc:
        raise HTTPException(404, "Failed authentication")


@api.get('/authorization')
def authorization(model: AuthorizationRequest = Depends()):
    return service_endpoint(app.server.server_get("endpoint", 'authorization'))