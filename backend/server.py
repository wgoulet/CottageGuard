from typing import Optional
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import authlib
from starlette.applications import Starlette
from starlette_oauth2_api import AuthenticateMiddleware
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse, JSONResponse
from authlib.integrations.starlette_client import OAuth
import pprint
import json
from fastapi.logger import logger
import logging
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import datetime
import uuid

# This server is the backend server that will accept requests from Raspberry PI REST API clients
# that perform work as well as will act as the backend for the user facing web app that allows
# users to submit work requests to be performed by the Raspberry PI REST clients.

# Setup authentication for the API endpoints. API callers that will access the work queue must
# present a valid access token with the apicallers scope present.

app = FastAPI()
app.add_middleware(AuthenticateMiddleware,
    providers={
        'okta': {
            'issuer':"https://dev-4402362.okta.com/oauth2/default",
            'audience': '0oa3grqlbqp3FBmWF5d7',
            'keys':"https://dev-4402362.okta.com/oauth2/default/v1/keys"
        }
    },
    public_paths={'/public'},
)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.route("/public")
def read_public(request):
    return JSONResponse({"UserState":"unauthenticated"})
    
@app.route("/testauth")
def read_root(request):
    return JSONResponse({"you are": "authenticated"})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)