import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html',charset='UTF-8')

#Run Server
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


#  ORM
@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global _pool
    pool = yield from aiomysql.create_pool(
        host=kw.get('host','tcp://10.10.32.51'),
        port=kw.get('port',3306),
        user=kw['uwGH89OUPa5NQi3Y'],
        password=kw['p5XHQh9Pja236LnTv'],
        db=kw[''],
    )
