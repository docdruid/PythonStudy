import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

#  ORM

#  Connect pool
@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global _pool
    pool = yield from aiomysql.create_pool(
        host=kw.get('host','127.0.0.1'),
        port=kw.get('port',3307),
        user=kw['root'],
        password=kw['google358599'],
        db=kw['pythonstudy'],
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )

#   Select
@asyncio.coroutine
def select(sql,args,size=None):
    log(sql,args)
    global _pool
    with(yield from _pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?','%s'),args or ())
        if size:
            rs=yield from cur.fetchmany(size)
        else:
            rs=yield from cur.fetchall()    
        yield from cur.close()
        logging.info('rows returned:%s' % len(rs))    
        return rs

#   Insert,Update,Delete
@asyncio.coroutine    
def excute(sql,args):
    log(sql)
    with (yield from _pool) as conn:
        try:
            cur=yield from conn.cursor()
            yield from cur.excute(sql.replace('?','%s'),args)
            affected=cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected    