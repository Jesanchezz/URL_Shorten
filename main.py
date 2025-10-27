from fastapi import FastAPI
from routers import url_shorter_route
from unittest import main

app = FastAPI()
app.include_router(url_shorter_route.router_url_shorter)

main(module='test', exit=False)