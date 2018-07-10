#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = AL
__Link__ = 707279282@qq.com
__mtime__ = 2018/7/9 12:49
__version__ = python3.6

"""
import sys
import asyncio
import orm
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(user='root', password='Happy@1314', db='awesome', loop=loop)
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
	sys.exit(0)